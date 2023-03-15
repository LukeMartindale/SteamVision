// REVIEW VISUALISATION SELECT OPTIONS
$(function(){

    $('#reviews-select').on('change', function (e) {

        let option = $(this).children("option:selected").val()

        if(option == "review-all-time"){

            review_all_time_year(game_id)
            active_review_vis = "all_time_year"

        } else if (option == "review-past-12-months"){

            reviews_past_twelve_months(game_id)
            active_review_vis = "past_twelve_months"

        } else if (option == "review-past-6-months"){

            reviews_past_six_months(game_id)
            active_review_vis = "past_six_months"
            
        } else if (option == "review-past-1-month"){

            reviews_past_one_month(game_id)
            active_review_vis = "past_one_month"
            
        } else if (option == "review-past-2-weeks"){

            reviews_past_two_weeks(game_id)
            active_review_vis = "past_two_weeks"
            
        } else if (option == "review-past-1-week"){

            reviews_past_one_week(game_id)
            active_review_vis = "past_one_week"
            
        } 

    })

})

// SENTIMENT VISUALISATION SELECT OPTIONS
$(function(){

    $('#sentiment-select').on('change', function (e) {

        let option = $(this).children("option:selected").val()

        if(option == "sentiment-all-time"){

            sentiment_all_time(game_id)
            active_sentiment_vis = "all_time"

        } else if (option == "sentiment-past-12-months"){

            sentiment_past_twelve_months(game_id)
            active_sentiment_vis = "past_twelve_months"

        } else if (option == "sentiment-past-6-months"){

            sentiment_past_six_months(game_id)
            active_sentiment_vis = "past_six_months"
            
        } else if (option == "sentiment-past-1-month"){

            sentiment_past_one_month(game_id)
            active_sentiment_vis = "past_one_month"
            
        } else if (option == "sentiment-past-2-weeks"){

            sentiment_past_two_weeks(game_id)
            active_sentiment_vis = "past_two_weeks"
            
        } else if (option == "sentiment-past-1-week"){

            sentiment_past_one_week(game_id)
            active_sentiment_vis = "past_one_week"
            
        } 

    })

})

// EMOTION VISUALISATION SELECT OPTIONS
$(function(){

    $('#emotion-select').on('change', function (e) {

        let option = $(this).children("option:selected").val()

        if(option == "emotion-all-time"){

            emotion_all_time(game_id)
            active_emotion_vis = "all_time"

        } else if (option == "emotion-past-12-months"){

            emotion_past_twelve_months(game_id)
            active_emotion_vis = "past_twelve_months"

        } else if (option == "emotion-past-6-months"){

            emotion_past_six_months(game_id)
            active_emotion_vis = "past_six_months"
            
        } else if (option == "emotion-past-1-month"){

            emotion_past_one_month(game_id)
            active_emotion_vis = "past_one_month"
            
        } else if (option == "emotion-past-2-weeks"){

            emotion_past_two_weeks(game_id)
            active_emotion_vis = "past_two_weeks"
            
        } else if (option == "emotion-past-1-week"){

            emotion_past_one_week(game_id)
            active_emotion_vis = "past_one_week"
            
        } 

    })
    
})

// PLAYER VISUALISATION SELECT OPTIONS
$(function(){

    $('#player-select').on('change', function (e) {

        let option = $(this).children("option:selected").val()

        if(option == "player-all-time"){

            player_count_all_time(game_id)
            active_player_vis = "all_time"

        } else if (option == "player-past-1-month"){

            player_count_past_one_month(game_id)
            active_player_vis = "past_one_month"

        } else if (option == "player-past-2-weeks"){

            player_count_past_two_weeks(game_id)
            active_player_vis = "past_two_weeks"
            
        } else if (option == "player-past-1-week"){

            player_count_past_one_week(game_id)
            active_player_vis = "past_one_week"
            
        } else if (option == "player-past-72-hours"){

            player_count_past_72_hours(game_id)
            active_player_vis = "past_72_hours"
            
        } else if (option == "player-past-48-hours"){

            player_count_past_48_hours(game_id)
            active_player_vis = "past_48_hours"
            
        } else if (option == "player-past-24-hours"){

            player_count_past_24_hours(game_id)
            active_player_vis = "past_24_hours"
            
        } 

    })
    
})

function no_reviews_neutral_bar(){

    $(".neg-bar").each(function(){

        if($(this).val() == 0){
            let reg = new RegExp("Date:(.*)")
            $(this).css("fill", "rgba(217, 217, 217, 0.3)")
            let title = $(this).children("title").html()
            title = reg.exec(title)
            $(this).children("title").html("Info: No Reviews\nDate:" + title[1])
        }

    })

}

function reviews_update_current_total(data){

    let total_reviews = 0

    data.forEach(function(item){
        total_reviews += item.number_of_reviews
    })

    $("#reviews-total-info").text(total_reviews)

}

function sentiment_update_current_value(data){

    let sentiment_score = 0
    let num_of_reviews = 0
    let pos_counter = 0
    let neg_counter = 0

    pos_labels = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1"]
    neg_labels = ["-0.1", "-0.2", "-0.3", "-0.4", "-0.5", "-0.6", "-0.7", "-0.8", "-0.9", "-1"]

    data.forEach(function(item){

        num_of_reviews += item.value

        if(pos_labels.includes(item.label)){
            pos_counter += item.value
        } else if (neg_labels.includes(item.label)){
            neg_counter += item.value
        }

    })

    let sub_total = pos_counter - neg_counter

    if (num_of_reviews > 0){
        sentiment_score = (sub_total / num_of_reviews).toFixed(3)
    } else {
        sentiment_score = 0.000
    }

    $("#sentiment-value-info").text(sentiment_score)

}
