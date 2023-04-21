// SET Variables
let follow_status = "unknown"

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

    // Visualisation info widget
    $(".visualisation-legend-bar-info-cirlce").on({
        mouseenter: function() {
            $(this).parents().siblings(".absolute-anchor").find(".vis-info-box-wrapper").removeClass("hide-section")
        },
        mouseleave: function() {
            $(this).parents().siblings(".absolute-anchor").find(".vis-info-box-wrapper").addClass("hide-section")
        }
    })

})

// CHECK IF USER IF FOLLOWING GAME
$(function(){

    let api_url = `/api/user/checkfollowgame/${game_id}`

    let response = function(){
        let data = null;
        $.ajax({
            async: false,
            type: 'GET',
            dataType: 'json',
            url: api_url,
            success: function(result){
                data = result
            }
        });
        return data
    }();

    if(response.code == 1){
        follow_status = "following"
        $('#follow-game-button').text("Unfollow")
        $('#follow-game-button').addClass("alternate-detail-button")
    } else if (response.code == 2) {
        follow_status = "not following"
    }

    console.log(follow_status)

})

function FollowButton(){

    console.log("Follow Button")
    console.log(follow_status)

    if (follow_status == "not following") {
        console.log("TEST 1")
        let api_url = `/api/user/followgame/${game_id}/`

        let response = function(){
            let data = null;
            $.ajax({
                async: false,
                type: 'GET',
                dataType: 'json',
                url: api_url,
                success: function(result){
                    data = result
                }
            });
            return data
        }();

        console.log("1")

        follow_status = "following"

        $('#follow-game-button').text("Unfollow")
        $('#follow-game-button').addClass("alternate-detail-button")

    } else if (follow_status == "following") {
        console.log("TEST 2")
        let api_url = `/api/user/unfollowgame/${game_id}/`

        let response = function(){
            let data = null;
            $.ajax({
                async: false,
                type: 'GET',
                dataType: 'json',
                url: api_url,
                success: function(result){
                    data = result
                }
            });
            return data
        }();

        console.log("2")

        follow_status = "not following"
        
        $('#follow-game-button').text("Follow")
        $('#follow-game-button').removeClass("alternate-detail-button")
    }

}

function CompareButton(){

    console.log("Compare Button")

    let url = `/compare/?games=${game_id}`

    window.location.href = url
    
}


// Set specific colours of parts of the page
$(function(){

    // Review percentages colour
    let widget = $("#top-widget-current-review-score")
    let percentage = reviews_percentage

    console.log(percentage)

    if (percentage >= 70){
        widget.css("color", "#80a45c")
        widget.text(`${(percentage * 100).toFixed(1)}%`)
    } else if (percentage >= 60) {
        widget.css("color", "#c0d4ac")
        widget.text(`${(percentage * 100).toFixed(1)}%`)
    } else if (percentage >= 50) {
        widget.css("color", "#f4ff50")
        widget.text(`${(percentage * 100).toFixed(1)}%`)
    } else if (percentage >= 40) {
        widget.css("color", "#f89c3c")
        widget.text(`${(percentage * 100).toFixed(1)}%`)
    } else {
        widget.css("color", "#f03424")
        widget.text(`${(percentage * 100).toFixed(1)}%`)
    }

    // Sentiment score colour
    let current_sentiment_widget = $("#widget-section-current-sentiment-score")
    let current_sentiment_value = current_sentiment_widget.text()
    let highest_sentiment_value = current_sentiment_widget.text()

    let sentiment_percentage = (current_sentiment_value / highest_sentiment_value) * 100

    if (sentiment_percentage >= 70){
        current_sentiment_widget.css("color", "#80a45c")
    } else if (sentiment_percentage >= 60) {
        current_sentiment_widget.css("color", "#c0d4ac")
    } else if (sentiment_percentage >= 50) {
        current_sentiment_widget.css("color", "#f4ff50")
    } else if (sentiment_percentage >= 40) {
        current_sentiment_widget.css("color", "#f89c3c")
    } else {
        current_sentiment_widget.css("color", "#f03424")
    }

    // emotion emoji display
    let emotion_data = get_data_emotion_all_time(game_id)
    let emotions_base = ["Happy", "Angry", "Surprise", "Sad", "Fear"]
    let total_emotion = 0
    let prominent = []

    console.log(emotion_data)

    emotions_base.forEach(function(value, index){
        total_emotion += emotion_data[value]
    })

    if(total_emotion > 0){

        // Get the prominent emotions, prominent emotions are those with a percentage of 20% or higher
        emotions_base.forEach(function(value, index){
            // Get the prominent emotions
            if(emotion_data[value] / total_emotion >= 0.15){
                prominent.push(value)
            }
        })

        prominent.forEach(function(value, index){

            let emotion_widget = $("#content-widgets-prominent-emotions")

            if(value == "Happy"){
                // Happy
                emotion_widget.append('<div class="emotion-icon-wrapper" id="top-emotion-icon-happy"></div>')
                emotion_widget.find("#top-emotion-icon-happy").append('<i class="bi bi-emoji-smile-fill emotion-icon emotion-happy" title="Happy"></i>')
            } else if (value == "Angry") {
                // Angry
                emotion_widget.append('<div class="emotion-icon-wrapper" id="top-emotion-icon-angry"></div>')
                emotion_widget.find("#top-emotion-icon-angry").append('<i class="bi bi-emoji-angry-fill emotion-icon emotion-angry" title="Angry"></i>')
            } else if (value == "Surprise") {
                // laughing
                emotion_widget.append('<div class="emotion-icon-wrapper" id="top-emotion-icon-surprise"></div>')
                emotion_widget.find("#top-emotion-icon-surprise").append('<i class="bi bi-emoji-laughing-fill emotion-icon emotion-surprise" title="Surprise"></i>')
            } else if (value == "Sad") {
                // unhappy
                emotion_widget.append('<div class="emotion-icon-wrapper" id="top-emotion-icon-sad"></div>')
                emotion_widget.find("#top-emotion-icon-sad").append('<i class="bi bi-emoji-frown-fill emotion-icon emotion-sad" title="Sad"></i>')
            } else if (value == "Fear") {
                // dizzy
                emotion_widget.append('<div class="emotion-icon-wrapper" id="top-emotion-icon-fear"></div>')
                emotion_widget.find("#top-emotion-icon-fear").append('<i class="bi bi-emoji-dizzy-fill emotion-icon emotion-fear" title="Fear"></i>')
            }

        })

    } else {
        console.log("Not Yet Implemented")
        // Put a message that states no promient emotions found
    }


    console.log(prominent)


})
