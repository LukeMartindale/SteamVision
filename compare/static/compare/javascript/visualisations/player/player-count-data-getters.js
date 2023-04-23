function get_data_player_count_all_time_compare(ids){

    let temp_data
    let player_data = []

    ids.forEach(function(value, index){

        let api_url = `/api/get-player-count/all-time/${value}/`

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

        player_data.push(temp_data)

    })

    return player_data

}

function get_data_player_count_past_24_hours_compare(ids) {

    let api_url = "/api/get-player-count/past-24-hours/"
    let temp_data = []
    let player_data = []

    ids.forEach(function(value, index){

        api_url = `/api/get-player-count/past-24-hours/${value}/`

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

        player_data.push(temp_data)

    })

    return player_data

}
