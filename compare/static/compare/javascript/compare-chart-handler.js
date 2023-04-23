// Set the default options for what graph is active for page refresh use.
let active_review_vis = "all_time_year"
let active_sentiment_vis = "all_time"
let active_emotion_vis = "all_time"
let active_player_vis = "all_time"

function drawGraphs(){
    // Draw Players Graph
    playerGraphsHandler(active_player_vis)
}

function playerGraphsHandler(active_vis){

    console.log(compare_game_ids)

    if(active_vis == "all_time"){
        console.log("all time")
        player_count_all_time_compare(compare_game_ids)
        playerLegendHandler("player")
    } else if(active_vis == "past_24_hours") {
        console.log("past 24 hours")
        player_count_past_24_hours_compare(compare_game_ids)
        playerLegendHandler("player")
    }

}

function playerLegendHandler(graph) {

    let legend_bar

    // Figure out which graph legend needs updating
    if(graph == "player"){
        legend_bar = $("#player-vis-legend-bar")
    }

    legend_bar.empty()

    compare_game_data.forEach(function(value, index){
        legend_bar
            .append(`<div class="visualisation-legend-widget-wrapper" id="legend-widget-wrapper-${index}" style="border: 2px solid ${compare_players_colours[index]}; background-color: ${compare_players_colours[index] + "4d"};"></div>`)

        legend_bar
            .find(`#legend-widget-wrapper-${index}`)
            .append(`<div class="visualisation-legend-widget-minor-section" id="legend-widget-minor-${index}"></div>`)
            .append(`<div class="visualisation-legend-widget-major-section" id="legend-widget-major-${index}"></div>`)

        legend_bar
            .find(`#legend-widget-minor-${index}`)
            .append(`<div class="visualisation-legend-widget-colour-circle" style="background-color: ${compare_players_colours[index]}"></div>`)

        legend_bar
            .find(`#legend-widget-major-${index}`)
            .append(value.name)

    })
}

// PLAYER VISUALISATION SELECT OPTIONS
$(function(){

    $('#player-select').on('change', function (e) {

        let option = $(this).children("option:selected").val()

        if(option == "player-all-time"){

            player_count_all_time_compare(compare_game_ids)
            playerLegendHandler("player")
            active_player_vis = "all_time"

        } else if (option == "player-past-1-month"){

            active_player_vis = "past_one_month"

        } else if (option == "player-past-2-weeks"){

            active_player_vis = "past_two_weeks"
            
        } else if (option == "player-past-1-week"){
            active_player_vis = "past_one_week"
            
        } else if (option == "player-past-72-hours"){

            active_player_vis = "past_72_hours"
            
        } else if (option == "player-past-48-hours"){

            active_player_vis = "past_48_hours"
            
        } else if (option == "player-past-24-hours"){

            player_count_past_24_hours_compare(compare_game_ids)
            playerLegendHandler("player")
            active_player_vis = "past_24_hours"
            
        } 

    })
    
})
