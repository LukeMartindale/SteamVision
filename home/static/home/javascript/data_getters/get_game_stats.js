let host_url = window.location.host

let api_url = `/api/get-games-stats/${game_id}/`

const reviews_data = function(){
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
    return data[0]
}();
