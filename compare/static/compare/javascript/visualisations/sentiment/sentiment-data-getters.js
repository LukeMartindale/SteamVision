function get_data_sentiment_all_time_compare(ids){

    let temp_data
    let formatted_data = sentiment_format_base

    ids.forEach(function(value, index){
        let api_url = `/api/get-sentiment/all-time/${value}/`

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

        // Formatt data
        formatted_data.forEach(function(data, data_index){
            data[compare_game_data[index].name] = temp_data[data_index]['value']
        })
        
    })

    return formatted_data
    
}