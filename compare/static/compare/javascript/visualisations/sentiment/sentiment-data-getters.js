function get_data_sentiment_all_time_compare(ids){

    let temp_data
    let formatted_data = [
        {label: '-1'},
        {label: '-0.9'},
        {label: '-0.8'},
        {label: '-0.7'},
        {label: '-0.6'},
        {label: '-0.5'},
        {label: '-0.4'},
        {label: '-0.3'},
        {label: '-0.2'},
        {label: '-0.1'},
        {label: '0'},
        {label: '0.1'},
        {label: '0.2'},
        {label: '0.3'},
        {label: '0.4'},
        {label: '0.5'},
        {label: '0.6'},
        {label: '0.7'},
        {label: '0.8'},
        {label: '0.9'},
        {label: '1'},
    ]

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

function get_data_sentiment_past_twelve_months_compare(ids) {
    
    let temp_data
    let formatted_data = [
        {label: '-1'},
        {label: '-0.9'},
        {label: '-0.8'},
        {label: '-0.7'},
        {label: '-0.6'},
        {label: '-0.5'},
        {label: '-0.4'},
        {label: '-0.3'},
        {label: '-0.2'},
        {label: '-0.1'},
        {label: '0'},
        {label: '0.1'},
        {label: '0.2'},
        {label: '0.3'},
        {label: '0.4'},
        {label: '0.5'},
        {label: '0.6'},
        {label: '0.7'},
        {label: '0.8'},
        {label: '0.9'},
        {label: '1'},
    ]

    ids.forEach(function(value, index){
        let api_url = `/api/get-sentiment/past-twelve-months/${value}/`

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

function get_data_sentiment_past_six_months_compare(ids) {
    
    let temp_data
    let formatted_data = [
        {label: '-1'},
        {label: '-0.9'},
        {label: '-0.8'},
        {label: '-0.7'},
        {label: '-0.6'},
        {label: '-0.5'},
        {label: '-0.4'},
        {label: '-0.3'},
        {label: '-0.2'},
        {label: '-0.1'},
        {label: '0'},
        {label: '0.1'},
        {label: '0.2'},
        {label: '0.3'},
        {label: '0.4'},
        {label: '0.5'},
        {label: '0.6'},
        {label: '0.7'},
        {label: '0.8'},
        {label: '0.9'},
        {label: '1'},
    ]

    ids.forEach(function(value, index){
        let api_url = `/api/get-sentiment/past-six-months/${value}/`

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

function get_data_sentiment_past_one_month_compare(ids) {
    
    let temp_data
    let formatted_data = [
        {label: '-1'},
        {label: '-0.9'},
        {label: '-0.8'},
        {label: '-0.7'},
        {label: '-0.6'},
        {label: '-0.5'},
        {label: '-0.4'},
        {label: '-0.3'},
        {label: '-0.2'},
        {label: '-0.1'},
        {label: '0'},
        {label: '0.1'},
        {label: '0.2'},
        {label: '0.3'},
        {label: '0.4'},
        {label: '0.5'},
        {label: '0.6'},
        {label: '0.7'},
        {label: '0.8'},
        {label: '0.9'},
        {label: '1'},
    ]

    ids.forEach(function(value, index){
        let api_url = `/api/get-sentiment/past-one-month/${value}/`

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
