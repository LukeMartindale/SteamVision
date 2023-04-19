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
        })

        console.log(compare_game_data)

        player_count_past_24_hours_compare(compare_game_ids)

    }

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
