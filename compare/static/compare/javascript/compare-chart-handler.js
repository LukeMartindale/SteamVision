// Set the default options for what graph is active for page refresh use.
let active_review_vis = "all_time_year"
let active_sentiment_vis = "all_time"
let active_emotion_vis = "all_time"
let active_player_vis = "past_24_hours"

function drawGraphs(){
    // Draw Players Graph
    playerGraphsHandler(active_player_vis)
}

function playerGraphsHandler(active_vis){

    console.log(compare_game_ids)

    if(active_vis == "all_time"){
        console.log("all time")
    } else if(active_vis == "past_24_hours") {
        console.log("past 24 hours")
        player_count_past_24_hours_compare(compare_game_ids)
    }

}

// // PLAYER VISUALISATION SELECT OPTIONS
// $(function(){

//     $('#player-select').on('change', function (e) {

//         let option = $(this).children("option:selected").val()

//         if(option == "player-all-time"){

//             player_count_all_time(game_id)
//             active_player_vis = "all_time"

//         } else if (option == "player-past-1-month"){

//             player_count_past_one_month(game_id)
//             active_player_vis = "past_one_month"

//         } else if (option == "player-past-2-weeks"){

//             player_count_past_two_weeks(game_id)
//             active_player_vis = "past_two_weeks"
            
//         } else if (option == "player-past-1-week"){

//             player_count_past_one_week(game_id)
//             active_player_vis = "past_one_week"
            
//         } else if (option == "player-past-72-hours"){

//             player_count_past_72_hours(game_id)
//             active_player_vis = "past_72_hours"
            
//         } else if (option == "player-past-48-hours"){

//             player_count_past_48_hours(game_id)
//             active_player_vis = "past_48_hours"
            
//         } else if (option == "player-past-24-hours"){

//             player_count_past_24_hours(game_id)
//             active_player_vis = "past_24_hours"
            
//         } 

//     })
    
// })
