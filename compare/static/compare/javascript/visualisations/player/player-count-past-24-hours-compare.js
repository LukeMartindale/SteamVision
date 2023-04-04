function get_data_player_count_past_24_hours_compare(ids) {

    console.log(ids)

    let api_url = "/api/get-player-count/past-24-hours/"
    let temp_data = []
    let player_data = []

    ids.forEach(function(value, index){

        api_url = `/api/get-player-count/past-24-hours/${value}/`
        console.log(api_url)

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

        console.log(temp_data)

        player_data.push(temp_data)

    })

    return player_data

}