// GENERAL PAGE FUNCTIONALITY
$(function(){

    // Content Section Change "Tab"
    $("#review-selector-button").click(function(){

        let ids = ["players-section"]
        let button_ids = ["players-selector-button"]

        ids.forEach(function(id, index){
            if(!$("#" + id).hasClass("hide-section")){
                $("#" + id).addClass("hide-section")
            }
        })

        button_ids.forEach(function(id, index){
            if($("#" + id).hasClass("content-selected")){
                $("#" + id).removeClass("content-selected")
            }
        })

        $("#reviews-section").removeClass("hide-section")
        $("#review-selector-button").addClass("content-selected")

    })


    $("#players-selector-button").click(function(){

        let ids = ["reviews-section"]
        let button_ids = ["review-selector-button"]

        ids.forEach(function(id, index){
            if(!$("#" + id).hasClass("hide-section")){
                $("#" + id).addClass("hide-section")
            }
        })

        button_ids.forEach(function(id, index){
            if($("#" + id).hasClass("content-selected")){
                $("#" + id).removeClass("content-selected")
            }
        })

        $("#players-section").removeClass("hide-section")
        $("#players-selector-button").addClass("content-selected")

    })

    // Content Section Widegt Dropdown
    $(".widgets-draw-icon-wrapper").click(function(){
        $(this).closest(".game-section").find(".visualisation-widgets-wrapper").toggleClass("hide-ani")
        $(this).children().toggleClass("widgets-icon-up")
    })

})

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
            
        }

    })

})
