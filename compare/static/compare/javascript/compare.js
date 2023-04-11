$(function(){

    console.log("COMPARE LOAD TEST")

    let numbers = []

    $("#test-button").click(function(){
        numbers.push($("#test-number").val())
        let player = player_count_past_24_hours_compare(numbers)

        console.log(player)

    })

})

$(function(){

    console.log("TEST")

    let params = new URLSearchParams(document.location.search);
    let games = params.get("games");

    let game_ids = []
    let numbers = []
    
    // Check games is not null or empty
    if(games){

        split_games = games.split(",");
        let game_data = getGame(split_games)

        console.log("True")
        console.log(game_data)

        game_data.forEach(function(value, index){
            game_ids.push(value[0]["app_id"])
        })

        console.log(game_ids)
        numbers = game_ids

    }

    console.log(games)
    player_count_past_24_hours_compare(numbers)

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
