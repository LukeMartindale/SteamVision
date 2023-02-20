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

function no_reviews_neutral_bar(){

    $(".neg-bar").each(function(){

        if($(this).val() == 0){
            $(this).css("fill", "rgba(217, 217, 217, 0.3)")
            $(this).children("title").html("No Reviews")
        }

    })

}

function reviews_update_current_total(data){

    let total_reviews = 0

    data.forEach(function(item){
        total_reviews += item.number_of_reviews
    })

    $(".visualisation-container-header-detail-widget-right").text(total_reviews)

}
