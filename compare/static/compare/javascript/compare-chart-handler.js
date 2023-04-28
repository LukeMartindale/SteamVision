// Set the default options for what graph is active for page refresh use.
let active_review_vis = "all_time_year"
let active_sentiment_vis = "all_time"
let active_emotion_vis = "all_time"
let active_player_vis = "all_time"

function drawGraphs(){

    if(active_tab == "review") {
        reviewsGraphsHandler(active_review_vis)
    } else if (active_tab == "sentiment") {
        // Draw Sentiment Graph
        sentimentGraphsHandler(active_sentiment_vis)
    } else if (active_tab == "emotion") {
        console.log("Not yet Implemented")
    } else if (active_tab == "player") {
        // Draw Players Graph
        playerGraphsHandler(active_player_vis)
    }

}

function reviewsGraphsHandler(active_vis){

    if (active_vis == "all_time_year"){
        reviews_all_time_year_compare(compare_game_ids)
        LegendHandler("review")
    } else if (active_vis == "past_twelve_months") {
        reviews_past_twelve_months_compare(compare_game_ids)
        LegendHandler("review")
    } else if (active_vis == "past_six_months") {
        reviews_past_six_months_compare(compare_game_ids)
        LegendHandler("review")
    } else if (active_vis == "past_one_month"){
        reviews_past_one_month_compare(compare_game_ids)
        LegendHandler("review")
    } else if (active_vis == "past_two_weeks") {
        reviews_past_two_weeks_compare(compare_game_ids)
        LegendHandler("review")
    } else if (active_vis == "past_one_week") {
        reviews_past_one_week_compare(compare_game_ids)
        LegendHandler("review")
    }

}

function sentimentGraphsHandler(active_vis){

    if (active_vis == "all_time"){
        sentiment_all_time_compare(compare_game_ids)
        LegendHandler("sentiment")
    } else if (active_vis == "past_twelve_months") {
        sentiment_past_twelve_months_compare(compare_game_ids)
        LegendHandler("sentiment")
    } else if (active_vis == "past_six_months") {
        sentiment_past_six_months_compare(compare_game_ids)
        LegendHandler("sentiment")
    } else if (active_vis == "past_one_month"){
        sentiment_past_one_month_compare(compare_game_ids)
        LegendHandler("sentiment")
    } else if (active_vis == "past_two_weeks") {
        sentiment_past_two_weeks_compare(compare_game_ids)
        LegendHandler("sentiment")
    } else if (active_vis == "past_one_week") {
        sentiment_past_one_week_compare(compare_game_ids)
        LegendHandler("sentiment")
    }

}

function playerGraphsHandler(active_vis){

    if(active_vis == "all_time"){
        player_count_all_time_compare(compare_game_ids)
        LegendHandler("player")
    } else if (active_vis == "past_one_month"){
        player_count_past_one_month_compare(compare_game_ids)
        LegendHandler("player")
    } else if (active_vis == "past_two_weeks") {
        player_count_past_two_weeks_compare(compare_game_ids)
        LegendHandler("player")
    } else if (active_vis == "past_one_week") {
        player_count_past_one_week_compare(compare_game_ids)
        LegendHandler("player")
    } else if(active_vis == "past_72_hours") {
        player_count_past_72_hours_compare(compare_game_ids)
        LegendHandler("player")
    } else if(active_vis == "past_48_hours") {
        player_count_past_48_hours_compare(compare_game_ids)
        LegendHandler("player")
    } else if(active_vis == "past_24_hours") {
        player_count_past_24_hours_compare(compare_game_ids)
        LegendHandler("player")
    }

}

function LegendHandler(graph) {

    let legend_bar
    let legend_colours

    // Figure out which graph legend needs updating
    if (graph == "review"){
        legend_bar = $("#review-vis-legend-bar")
        legend_colours = compare_review_colours
    } else if (graph == "sentiment") {
        legend_bar = $("#sentiment-vis-legend-bar")
        legend_colours = compare_sentiment_colours
    } else if (graph == "emotion") {
        legend_bar = $("#emotion-vis-legend-bar")
    } else if (graph == "player") {
        legend_bar = $("#player-vis-legend-bar")
        legend_colours = compare_players_colours
    }

    legend_bar.empty()

    compare_game_data.forEach(function(value, index){
        legend_bar
            .append(`<div class="visualisation-legend-widget-wrapper" id="legend-widget-wrapper-${index}" style="border: 2px solid ${legend_colours[index]}; background-color: ${legend_colours[index] + "4d"};"></div>`)

        legend_bar
            .find(`#legend-widget-wrapper-${index}`)
            .append(`<div class="visualisation-legend-widget-minor-section" id="legend-widget-minor-${index}"></div>`)
            .append(`<div class="visualisation-legend-widget-major-section" id="legend-widget-major-${index}"></div>`)

        legend_bar
            .find(`#legend-widget-minor-${index}`)
            .append(`<div class="visualisation-legend-widget-colour-circle" style="background-color: ${legend_colours[index]}"></div>`)

        legend_bar
            .find(`#legend-widget-major-${index}`)
            .append(value.name)

    })
}

// REVIEW VISUALISATION SELECT OPTIONS
$(function(){

    $('#reviews-select').on('change', function (e) {
        
        let option = $("#reviews-select").children("option:selected").val()

        if(option == "review-all-time"){

            reviews_all_time_year_compare(compare_game_ids)
            active_review_vis = "all_time_year"

        } else if (option == "review-past-12-months"){

            reviews_past_twelve_months_compare(compare_game_ids)
            active_review_vis = "past_twelve_months"

        } else if (option == "review-past-6-months"){

            reviews_past_six_months_compare(compare_game_ids)
            active_review_vis = "past_six_months"
            
        } else if (option == "review-past-1-month"){

            reviews_past_one_month_compare(compare_game_ids)
            active_review_vis = "past_one_month"
        
        } else if (option == "review-past-2-weeks"){

            reviews_past_two_weeks_compare(compare_game_ids)
            active_review_vis = "past_two_weeks"

        } else if (option == "review-past-1-week"){

            reviews_past_one_week_compare(compare_game_ids)
            active_review_vis = "past_one_week"

        }
        
    })
})

// SENTIMENT VISUALISATION SELECT OPTIONS
$(function(){

    $('#sentiment-select').on('change', function (e) {

        let option = $(this).children("option:selected").val()

        if(option == "sentiment-all-time"){

            sentiment_all_time_compare(compare_game_ids)
            active_sentiment_vis = "all_time"

        } else if (option == "sentiment-past-12-months"){

            sentiment_past_twelve_months_compare(compare_game_ids)
            active_sentiment_vis = "past_twelve_months"

        } else if (option == "sentiment-past-6-months"){

            sentiment_past_six_months_compare(compare_game_ids)
            active_sentiment_vis = "past_six_months"
            
        } else if (option == "sentiment-past-1-month"){

            sentiment_past_one_month_compare(compare_game_ids)
            active_sentiment_vis = "past_one_month"
            
        } else if (option == "sentiment-past-2-weeks"){

            sentiment_past_two_weeks_compare(compare_game_ids)
            active_sentiment_vis = "past_two_weeks"
            
        } else if (option == "sentiment-past-1-week"){

            sentiment_past_one_week_compare(compare_game_ids)
            active_sentiment_vis = "past_one_week"
            
        } 

    })

})

// PLAYER VISUALISATION SELECT OPTIONS
$(function(){

    $('#player-select').on('change', function (e) {

        let option = $(this).children("option:selected").val()

        if(option == "player-all-time"){

            player_count_all_time_compare(compare_game_ids)
            LegendHandler("player")
            active_player_vis = "all_time"

        } else if (option == "player-past-1-month"){

            player_count_past_one_month_compare(compare_game_ids)
            LegendHandler("player")
            active_player_vis = "past_one_month"

        } else if (option == "player-past-2-weeks"){

            player_count_past_two_weeks_compare(compare_game_ids)
            LegendHandler("player")
            active_player_vis = "past_two_weeks"
            
        } else if (option == "player-past-1-week"){

            player_count_past_one_week_compare(compare_game_ids)
            LegendHandler("player")
            active_player_vis = "past_one_week"
            
        } else if (option == "player-past-72-hours"){

            player_count_past_72_hours_compare(compare_game_ids)
            LegendHandler("player")
            active_player_vis = "past_72_hours"
            
        } else if (option == "player-past-48-hours"){

            player_count_past_48_hours_compare(compare_game_ids)
            LegendHandler("player")
            active_player_vis = "past_48_hours"
            
        } else if (option == "player-past-24-hours"){

            player_count_past_24_hours_compare(compare_game_ids)
            rLegendHandler("player")
            active_player_vis = "past_24_hours"
            
        } 

    })
    
})
