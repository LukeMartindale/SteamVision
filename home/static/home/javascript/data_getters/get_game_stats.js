let host_url = window.location.host

console.log(game_id)

let api_url = `/api/get-games-stats/${game_id}/`

console.log(game_id)

const reviews_data = function(){
    let data = null;
    $.ajax({
        async: false,
        type: 'GET',
        dataType: 'json',
        url: api_url,
        success: function(result){
            data = result
            console.log(result)
        }
    });
    return data[0]
}();

console.log(reviews_data)
