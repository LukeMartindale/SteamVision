console.log("Resize handler load test")
$(function(){

    let resizeTimer

    $(window).resize(function(){

        clearTimeout(resizeTimer)
        resizeTimer = setTimeout(function(){

            sentiemnt_compare_resize_handler(active_sentiment_vis)
            player_compare_resize_handler(active_player_vis)

        }, 100)

    })

})

function sentiemnt_compare_resize_handler(active_vis) {
    if (active_vis == "all_time"){
        sentiment_all_time_compare(compare_game_ids)
    } else if (active_vis == "past_one_month"){

    } else if (active_vis == "past_two_weeks"){

    } else if (active_vis == "past_one_week"){

    } else if (active_vis == "past_72_hours"){

    } else if (active_vis == "past_48_hours"){

    } else if (active_vis == "past_24_hours"){

    }
}

function player_compare_resize_handler(active_vis) {
    if (active_vis == "all_time"){
        player_count_all_time_compare(compare_game_ids)
    } else if (active_vis == "past_one_month"){
        player_count_past_one_month_compare(compare_game_ids)
    } else if (active_vis == "past_two_weeks"){
        player_count_past_two_weeks_compare(compare_game_ids)
    } else if (active_vis == "past_one_week"){
        player_count_past_one_week_compare(compare_game_ids)
    } else if (active_vis == "past_72_hours"){
        player_count_past_72_hours_compare(compare_game_ids)
    } else if (active_vis == "past_48_hours"){
        player_count_past_48_hours_compare(compare_game_ids)
    } else if (active_vis == "past_24_hours"){
        player_count_past_24_hours_compare(compare_game_ids)
    }
}
