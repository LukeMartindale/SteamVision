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
})
