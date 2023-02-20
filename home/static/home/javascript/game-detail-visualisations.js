// VISUALISATION SELECT OPTIONS
$(function(){

    $('select').on('change', function (e) {

        let option = $(this).children("option:selected").val()

        if(option == "all-time"){

            review_all_time_year(game_id)

        } else if (option == "past-12-months"){

            reviews_past_twelve_months(game_id)

        } else if (option == "past-6-months"){

            reviews_past_six_months(game_id)
            
        } else if (option == "past-1-month"){

            reviews_past_one_month(game_id)
            
        } else if (option == "past-2-weeks"){

            reviews_past_two_weeks(game_id)
            
        } else if (option == "past-1-week"){

            reviews_past_one_week(game_id)
            
        } 

    })

})