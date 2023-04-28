$(function(){

    let resizeTimer

    $(window).resize(function(){

        clearTimeout(resizeTimer)
        resizeTimer = setTimeout(function(){

            if(active_tab == "review") {
                review_compare_resize_handler(active_review_vis)
            } else if (active_tab == "sentiment") {
                sentiemnt_compare_resize_handler(active_sentiment_vis)
            } else if (active_tab == "emotion") {
                console.log("Not yet Implemented")
            } else if (active_tab == "player") {
                player_compare_resize_handler(active_player_vis)
            }

        }, 100)

    })

})

function review_compare_resize_handler(active_vis) {
    if (active_vis == "all_time_year"){
        reviews_all_time_year_compare(compare_game_ids)
    } else if (active_vis == "past_twelve_months"){
        reviews_past_twelve_months_compare(compare_game_ids)
    } else if (active_vis == "past_six_months"){
        reviews_past_six_months_compare(compare_game_ids)
    } else if (active_vis == "past_one_month"){
        reviews_past_one_month_compare(compare_game_ids)
    } else if (active_vis == "past_two_weeks"){
        reviews_past_two_weeks_compare(compare_game_ids)
    } else if (active_vis == "past_one_week"){
        reviews_past_one_week_compare(compare_game_ids)
    }
}


function sentiemnt_compare_resize_handler(active_vis) {
    if (active_vis == "all_time"){
        sentiment_all_time_compare(compare_game_ids)
    } else if (active_vis == "past_twelve_months"){
        sentiment_past_twelve_months_compare(compare_game_ids)
    } else if (active_vis == "past_six_months"){
        sentiment_past_six_months_compare(compare_game_ids)
    } else if (active_vis == "past_one_month"){
        sentiment_past_one_month_compare(compare_game_ids)
    } else if (active_vis == "past_two_weeks"){
        sentiment_past_two_weeks_compare(compare_game_ids)
    } else if (active_vis == "past_one_week"){
        sentiment_past_one_week_compare(compare_game_ids)
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
