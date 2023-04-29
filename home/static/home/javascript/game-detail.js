// SET Variables
let follow_status = "unknown"
let follow_timeout

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

        redrawReviewsGraphs()
        redrawSentimentgraph()
        redrawEmotionGraph()

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

        redrawPlayerGraph()

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
    } else if (response.code == 0) {
        follow_status = "not logged in"
    }

})

function FollowButton(){

    if (follow_status == "not following") {
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

        follow_status = "following"

        $('#follow-game-button').text("Unfollow")
        $('#follow-game-button').addClass("alternate-detail-button")

        let widget = $(".detail-message-section")

        widget.empty()
        widget.append('<b style="margin-top: 7.5px; color: royalblue;">Successfully followed game</b>').hide().fadeIn()

        clearTimeout(follow_timeout)

        follow_timeout = setTimeout(function(){
            widget.empty()
        }, 2500)

        console.log("Not Logged In")

    } else if (follow_status == "following") {
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

        follow_status = "not following"
        
        $('#follow-game-button').text("Follow")
        $('#follow-game-button').removeClass("alternate-detail-button")

        let widget = $(".detail-message-section")

        widget.empty()
        widget.append('<b style="margin-top: 7.5px; color: royalblue;">Game has been unfollowed</b>').hide().fadeIn()

        clearTimeout(follow_timeout)

        follow_timeout = setTimeout(function(){
            widget.empty()
        }, 2500)

        console.log("Not Logged In")

    } else if (follow_status == "not logged in"){

        let widget = $(".detail-message-section")

        widget.empty()
        widget.append('<b style="margin-top: 7.5px; color: crimson;">You must be logged in to use this feature</b>').hide().fadeIn()

        clearTimeout(follow_timeout)

        follow_timeout = setTimeout(function(){
            widget.empty()
        }, 2500)

    }

}

function CompareButton(){

    let url = `/compare/?games=${game_id}`

    window.location.href = url
    
}

// Set specific colours of parts of the page
$(function(){

    // Review percentages colour
    let widget = $("#top-widget-current-review-score")

    let percentage = reviews_percentage

    if (percentage >= 0.70){
        widget.css("color", "#80a45c")
        widget.text(`${(percentage * 100).toFixed(1)}%`)
    } else if (percentage >= 0.60) {
        widget.css("color", "#c0d4ac")
        widget.text(`${(percentage * 100).toFixed(1)}%`)
    } else if (percentage >= 0.50) {
        widget.css("color", "#f4ff50")
        widget.text(`${(percentage * 100).toFixed(1)}%`)
    } else if (percentage >= 0.40) {
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


})

function redrawReviewsGraphs(){
    // Reviews redraw
    let option = $("#reviews-select").children("option:selected").val()

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

}

function redrawSentimentgraph() {
    // Sentiment Redraw
    let option = $("#sentiment-select").children("option:selected").val()

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

}

function redrawEmotionGraph(){
    // Emotion Redraw
    let option = $("#emotion-select").children("option:selected").val()

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
}

function redrawPlayerGraph() {
    // Player Redraw
    let option = $("#player-select").children("option:selected").val()

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
}

// DRAWER WIDGETS STUFF

// REVIEW DRAWER WIDGETS
$(function(){

    let api_url = `/api/visualisation/review-widgets/${game_id}/`

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

    console.log(response)

    // All time
    $("#reviews-drawer-all-time-positive").text(`${(response.all_time).toFixed(1)}%`)
    $("#reviews-drawer-all-time-negative").text(`${(response.all_time_neg).toFixed(1)}%`)
    // Past twelve months
    $("#reviews-drawer-twelve-months-positive").text(`${(response.twelve_months).toFixed(1)}%`)
    $("#reviews-drawer-twelve-months-negative").text(`${(response.twelve_months_neg).toFixed(1)}%`)
    // Past six months
    $("#reviews-drawer-six-months-positive").text(`${(response.six_months).toFixed(1)}%`)
    $("#reviews-drawer-six-months-negative").text(`${(response.six_months_neg).toFixed(1)}%`)
    // Past one month
    $("#reviews-drawer-past-month-positive").text(`${(response.thirty_days).toFixed(1)}%`)
    $("#reviews-drawer-past-month-negative").text(`${(response.thirty_days_neg).toFixed(1)}%`)
    // past two weeks
    $("#reviews-drawer-two-weeks-positive").text(`${(response.two_weeks).toFixed(1)}%`)
    $("#reviews-drawer-two-weeks-negative").text(`${(response.two_weeks_neg).toFixed(1)}%`)
    // Past one week
    $("#reviews-drawer-one-week-positive").text(`${(response.one_week).toFixed(1)}%`)
    $("#reviews-drawer-one-week-negative").text(`${(response.one_week_neg).toFixed(1)}%`)

})
