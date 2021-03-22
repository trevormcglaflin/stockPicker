function pick(onSuccess) {
    $.ajax({
        url: "pick_stocks",
        data: {

        },
        dataType: "json",
        type: "GET",
        success: function(response) {
            onSuccess(response);
        }
    });
}

$("#get-picks").on("click", function() {
    pick(function(message) {
        first_pick_tick = message[0][0];
        first_pick_percent = message[0][1];
        first_pick = "1. " + first_pick_tick + "->" + first_pick_percent + "%";
        second_pick_tick = message[1][0];
        second_pick_percent = message[1][1];
        second_pick = "1. " + second_pick_tick + "->" + second_pick_percent + "%";
        third_pick_tick = message[2][0];
        third_pick_percent = message[2][1];
        third_pick = "1. " + third_pick_tick + "->" + third_pick_percent + "%";
        fourth_pick_tick = message[3][0];
        fourth_pick_percent = message[3][1];
        fourth_pick = "1. " + fourth_pick_tick + "->" + fourth_pick_percent + "%";
        fifth_pick_tick = message[4][0];
        fifth_pick_percent = message[4][1];
        fifth_pick = "1. " + fifth_pick_tick + "->" + fifth_pick_percent + "%";
        $("#first-pick").text(first_pick);
        $("#second-pick").text(second_pick);
        $("#third-pick").text(third_pick);
        $("#fourth-pick").text(fourth_pick);
        $("#fifth-pick").text(fifth_pick);
    });
});