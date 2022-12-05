api_url = "http://localhost:8000/api/get-reviews/"

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
    return data['730']
}();