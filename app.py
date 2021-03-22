from flask import Flask, render_template
import json
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    return render_template("stockpicker.html")

@app.route("/pick_stocks", methods=["GET"])
def pick_stocks():
    start_date = get_start_date(14)
    tickers = get_tickers()
    stocks = get_stocks(tickers, start_date)
    top_picks = get_top_picks(stocks, 5)
    top_picks_2d = []
    for pick in top_picks:
        top_picks_2d.append([pick.ticker, round(pick.total_return, 2) * 100])
    return json.dumps(top_picks_2d)

def get_return(ticker, start_date):
    try:
        adj_close = wb.DataReader(ticker, data_source='yahoo', start=start_date)['Adj Close']
        start_price = adj_close[0]
        current_price = adj_close[len(adj_close) - 1]
        return ((current_price - start_price) / (start_price))
    except:
        return None

def get_start_date(days):
    today = datetime.today()
    start_date = today - timedelta(days=days)
    return start_date.date()

def get_tickers():
    pick_list = ["APPN", "NET", "FVVR", "FLGT", "LMND", "MELI", "OKTA", "PINS", "SHOP", "ZM", "KNSL",
                 "KS", "ATNM", "CWH", "INSP", "MGNI", "SHSP", "PAR", "XNYS", "TENB", "CYBR", "RUN",
                 "TPIC", "AES", "AY", "ICLN", "PLUG", "XYL", "DHR", "ECL", "ANET", "ICE", "SQ",
                 "NVDA", "PYPL", "UFO", "SPCE", "MAXR", "LORL", "TSCO", "VICI", "MRNA", "BCLI",
                 "VKTX", "ATRA", "DVAX", "ENPH", "REGN", "TWST", "ACAD", "ALEC", "KPTI", "RGNX",
                 "TSHA", "ALVR", "MRCI"]
    return pick_list

def get_stocks(tickers, start_date):
    stocks = []
    for ticker in tickers:
        stocks.append(Stock(ticker, start_date))
    return stocks

def get_top_picks(stocks, num_picks):
    picks = []
    for stock in stocks:
        if stock.total_return is not None:
            if len(picks) < num_picks:
                picks.append(stock)
            else:
                index = 0
                for pick in picks:
                    if stock.total_return > pick.total_return and stock not in picks:
                        picks[index] = stock
                    index += 1
    return picks

class Stock:
    def __init__(self, ticker, start_date):
        self.ticker = ticker
        self.total_return = get_return(self.ticker, start_date)



if __name__ == '__main__':
    app.run()