let host_url = window.location.hostname

let api_url = `http://${host_url}:8000/api/get-reviews-stats/${game_id}/`

const reviews_sentiment_data = function(){
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