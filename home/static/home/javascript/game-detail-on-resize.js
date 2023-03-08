// On page resize handler
$(function(){

    let resizeTimer;

    $(window).resize(function () { 

        clearTimeout(resizeTimer)
        resizeTimer = setTimeout(function() {

            reviews_resize_handler(active_review_vis)
            sentiment_resize_handler(active_sentiment_vis)
            emotion_resize_handler(active_emotion_vis)

        }, 100)
    
    });

})

// Review resize function
function reviews_resize_handler(active_vis){

    if (active_vis == "all_time_year"){
        review_all_time_year(game_id)
    } else if (active_vis == "past_twelve_months"){
        reviews_past_twelve_months(game_id)
    } else if (active_vis == "past_six_months"){
        reviews_past_six_months(game_id)
    } else if (active_vis == "past_one_month"){
        reviews_past_one_month(game_id)
    } else if (active_vis == "past_two_weeks"){
        reviews_past_two_weeks(game_id)
    } else if (active_vis == "past_one_week"){
        reviews_past_one_week(game_id)
    }
}
// Sentiment resize function
function sentiment_resize_handler(active_vis){

    if (active_vis == "all_time"){
        sentiment_all_time(game_id)
    } else if (active_vis == "past_twelve_months"){
        sentiment_past_twelve_months(game_id)
    } else if (active_vis == "past_six_months"){
        sentiment_past_six_months(game_id)
    } else if (active_vis == "past_one_month"){
        sentiment_past_one_month(game_id)
    } else if (active_vis == "past_two_weeks"){
        sentiment_past_two_weeks(game_id)
    } else if (active_vis == "past_one_week"){
        sentiment_past_one_week(game_id)
    }

}
// Emotion resize function
function emotion_resize_handler(active_vis){

    if (active_vis == "all_time"){
        emotion_all_time(game_id)
    } else if (active_vis == "past_twelve_months"){
        emotion_past_twelve_months(game_id)
    } else if (active_vis == "past_six_months"){
        emotion_past_six_months(game_id)
    } else if (active_vis == "past_one_month"){
        emotion_past_one_month(game_id)
    } else if (active_vis == "past_two_weeks"){
        emotion_past_two_weeks(game_id)
    } else if (active_vis == "past_one_week"){
        emotion_past_one_week(game_id)
    }

}
