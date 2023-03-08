// GENERAL PAGE FUNCTIONALITY
$(function(){

    // Content Section Change "Tab"
    $("#review-selector-button").click(function(){

        let ids = ["players-section", "recent-reviews-section"]
        let button_ids = ["players-selector-button", "recent-reviews-selector-button"]

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

    $("#recent-reviews-selector-button").click(function(){

        let ids = ["players-section", "reviews-section"]
        let button_ids = ["players-selector-button", "review-selector-button"]

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

        $("#recent-reviews-section").removeClass("hide-section")
        $("#recent-reviews-selector-button").addClass("content-selected")

    })


    $("#players-selector-button").click(function(){

        let ids = ["reviews-section", "recent-reviews-section"]
        let button_ids = ["review-selector-button", "recent-reviews-selector-button"]

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
