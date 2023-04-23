console.log("Resize handler load test")
$(function(){

    let resizeTimer

    $(window).resize(function(){

        clearTimeout(resizeTimer)
        resizeTimer = setTimeout(function(){

            player_compare_resize_handler(active_player_vis)

        }, 100)

    })

})

function player_compare_resize_handler(active_vis) {
    if (active_vis == "all_time"){
        player_count_all_time_compare(compare_game_ids)
    } else if (active_vis == "past_one_month"){
        // player_count_past_one_month(game_id)
    } else if (active_vis == "past_two_weeks"){
        // player_count_past_two_weeks(game_id)
    } else if (active_vis == "past_one_week"){
        // player_count_past_one_week(game_id)
    } else if (active_vis == "past_72_hours"){
        // player_count_past_72_hours(game_id)
    } else if (active_vis == "past_48_hours"){
        // player_count_past_48_hours(game_id)
    } else if (active_vis == "past_24_hours"){
        player_count_past_24_hours_compare(compare_game_ids)
    }
}
