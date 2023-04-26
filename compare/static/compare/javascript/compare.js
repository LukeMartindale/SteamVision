let compare_game_ids = []
let searched_game_data = []
let compare_game_data = []

let active_tab = "review"

// ON LOAD AUTO LOAD PRE SELECTED GAMES
$(function(){

    let params = new URLSearchParams(document.location.search);
    let games = params.get("games");
    
    // Check games is not null or empty
    if(games){

        split_games = games.split(",");
        let game_data = getGame(split_games)

        game_data.forEach(function(value, index){
            compare_game_ids.push(value[0]["app_id"])
            compare_game_data.push(value[0])
            selectedItemDisplayAppend(value[0])
        })

        reviewsGraphsHandler(active_review_vis)

    }

})

// Vis info button functionality
$(function(){

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

//COMPARISON TAB SECTIONS FUNCTIONALITY
$(function(){

    // REVIEWS TAB
    $("#review-selector-button").click(function(){

        let ids = ["sentiment-block", "emotion-block", "player-block"]
        let button_ids = ["sentiment-selector-button", "emotion-selector-button", "player-selector-button"]

        ids.forEach(function(id, index){
            $("#" + id).addClass("hide-section")
        })

        button_ids.forEach(function(id, index){
            $("#" + id).removeClass("content-selected")
        })

        $("#review-block").removeClass("hide-section")
        $("#review-selector-button").addClass("content-selected")

        active_tab = "review"

        reviewsGraphsHandler(active_review_vis)


    })
    // SENTIMENT TAB
    $("#sentiment-selector-button").click(function(){

        let ids = ["review-block", "emotion-block", "player-block"]
        let button_ids = ["review-selector-button", "emotion-selector-button", "player-selector-button"]

        ids.forEach(function(id, index){
            $("#" + id).addClass("hide-section")
        })

        button_ids.forEach(function(id, index){
            $("#" + id).removeClass("content-selected")
        })

        $("#sentiment-block").removeClass("hide-section")
        $("#sentiment-selector-button").addClass("content-selected")

        active_tab = "sentiment"

        sentimentGraphsHandler(active_sentiment_vis)

    })
    // EMOTION TAB
    $("#emotion-selector-button").click(function(){
        

        let ids = ["review-block", "sentiment-block", "player-block"]
        let button_ids = ["review-selector-button", "sentiment-selector-button", "player-selector-button"]

        ids.forEach(function(id, index){
            $("#" + id).addClass("hide-section")
        })

        button_ids.forEach(function(id, index){
            $("#" + id).removeClass("content-selected")
        })

        $("#emotion-block").removeClass("hide-section")
        $("#emotion-selector-button").addClass("content-selected")

        active_tab = "emotion"

    })
    // PLAYER TAB
    $("#player-selector-button").click(function(){

        let ids = ["review-block", "sentiment-block", "emotion-block"]
        let button_ids = ["review-selector-button", "sentiment-selector-button", "emotion-selector-button"]

        ids.forEach(function(id, index){
            $("#" + id).addClass("hide-section")
        })

        button_ids.forEach(function(id, index){
            $("#" + id).removeClass("content-selected")
        })

        $("#player-block").removeClass("hide-section")
        $("#player-selector-button").addClass("content-selected")

        active_tab = "player"

        playerGraphsHandler(active_player_vis)

    })

})


//GET DATA FOR SELECTED GAMES
function getGame(ids){

    let api_url = "/api/get-games/"
    let temp_data = []
    let game_data = []

    ids.forEach(function(value, index){

        api_url = `/api/get-games/${value}/`

        temp_data = function(){
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

        if(temp_data.length > 0){
            game_data.push(temp_data)
        }
    })
    
    return game_data

}

//GET THE OLDEST PLAYER RECORD FOR EACH SELECTED GAME
function getPlayerCountOldestDates(ids){

    let temp_data
    let oldest_dates = []

    ids.forEach(function(value, index){

        let api_url = `/api/compare/oldest-date-player-count/${value}/`

        temp_data = function(){
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

        oldest_dates.push(temp_data)

    })

    return oldest_dates
}

//COMPARE OLDEST PLAYER RECORD TO DETERMINE WHICH ONE IS OLDER
function comparePlayerCountOldestDates(){

    let oldest_dates = getPlayerCountOldestDates(compare_game_ids)
    let oldest_date = new Date()
    let oldest_id

    oldest_dates.forEach(function(value, index){
        oldest_dates[index].oldest_date = new Date(value.oldest_date)
        if (oldest_dates[index].oldest_date < oldest_date){
            oldest_date = oldest_dates[index].oldest_date
            oldest_id = oldest_dates[index].app_id
        }
    })

    return oldest_id

}
