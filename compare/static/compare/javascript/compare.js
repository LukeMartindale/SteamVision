let compare_game_ids = []
let searched_game_data = []
let compare_game_data = []

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

        console.log(compare_game_data)

        player_count_all_time_compare(compare_game_ids)
        playerLegendHandler("player")

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

function getPlayerCountOldestDates(ids){

    let temp_data
    let oldest_dates = []

    console.log(compare_game_ids)

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

function comparePlayerCountOldestDates(){

    console.log("comparepPlayerCountOldestDates")

    let oldest_dates = getPlayerCountOldestDates(compare_game_ids)
    let oldest_date = new Date()
    let oldest_id

    console.log(oldest_dates)

    oldest_dates.forEach(function(value, index){
        oldest_dates[index].oldest_date = new Date(value.oldest_date)
        console.log()
        if (oldest_dates[index].oldest_date < oldest_date){
            oldest_date = oldest_dates[index].oldest_date
            oldest_id = oldest_dates[index].app_id
        }
    })

    console.log(oldest_date)
    console.log(oldest_id)

    return oldest_id

}
