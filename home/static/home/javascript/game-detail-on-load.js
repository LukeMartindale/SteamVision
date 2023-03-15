// Set the default options for what graph is active for page refresh use.
let active_review_vis = "all_time_year"
let active_sentiment_vis = "all_time"
let active_emotion_vis = "all_time"

$(function(){
    // Draw reviews graph
    review_all_time_year(game_id)
    // Draw sentiment graph
    sentiment_all_time(game_id)
    // Draw emotion graph
    emotion_all_time(game_id)
    // Draw Player Count
    player_count_past_24_hours(game_id)
})

// make reviews collapse if they are too big
$(function(){

    $(".review-text-section").each(function(){

        if($(this).height() > 350){
            $(this).append('<button class="more-review-button">Show More</button>')
            $(this).find(".more-review-button").css(
                {
                    "background-color": "#4169E1",
                    "border-radius": "6px",
                    "border": "0",
                    "color": "#bec5cb",
                    "cursor": "pointer",
                    "width": "90px",
                    "height": "25px",
                    "margin-top": "10px"
                }
            )
        }

    })

    $(".more-review-button").click(function(){

        $(this)
            .parent(".review-text-section")
            .children(".review-text-pre")
            .toggleClass("review-expanded")

    })

})


// Hide Sections
$(function(){

    $("#recent-reviews-section").addClass("hide-section")
    $("#players-section").addClass("hide-section")

})

window.onbeforeunload = function () {
    window.scrollTo(0, 0);
  }
