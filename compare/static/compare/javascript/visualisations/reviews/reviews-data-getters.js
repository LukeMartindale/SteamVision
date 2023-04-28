function get_data_reviews_all_time_compare(ids) {

    let temp_data
    let reviews_data = []

    ids.forEach(function(value, index){

        let api_url = `/api/get-reviews/all-time-year/${value}/`

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
        
        reviews_data.push(temp_data)

    })

    let values = [] //Stores the years from the data
    let dates = []
    let formatted_data = []

    // Get All dates from all datasets
    reviews_data.forEach(function(value, index){
        values.push(value.map(function(data){
            return data.label
        }))
    })

    // Organise all the dates into a single array so there are no duplicated
    values.forEach(function(value, index){
        value.forEach(function(data, data_index){
            if(!dates.includes(data)){
                dates.push(data)
            }
        })
    })

    // Sort array in order of dates earliest first
    dates.sort(function(a, b) {
        return a - b
    })

    // Generate data object with correct labels
    dates.forEach(function(value, index){
        formatted_data.push({"label": value})
    })

    reviews_data.forEach(function(value, index){
        dates.forEach(function(data, data_index){
            let temp = value.filter(obj => {
                return obj.label === data
            })
            if(temp.length > 0){
                formatted_data[data_index][compare_game_data[index].name] = {
                    "percentage": temp[0].percentage,
                    "number_of_reviews": temp[0].number_of_reviews,
                }
            } else {
                formatted_data[data_index][compare_game_data[index].name] = {
                    "percentage": 0,
                    "number_of_reviews": 0,
                }
            }
        })

    })

    return formatted_data

}

function get_data_reviews_past_twelve_months_compare(ids) {

    let temp_data
    let reviews_data = []

    ids.forEach(function(value, index){

        let api_url = `/api/get-reviews/past-twelve-months/${value}/`

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
        
        reviews_data.push(temp_data)

    })

    let values = [] //Stores the years from the data
    let dates = []
    let formatted_data = []

    // Get All dates from all datasets
    reviews_data.forEach(function(value, index){
        values.push(value.map(function(data){
            return data.label
        }))
    })

    // Organise all the dates into a single array so there are no duplicated
    values.forEach(function(value, index){
        value.forEach(function(data, data_index){
            if(!dates.includes(data)){
                dates.push(data)
            }
        })
    })

    // Sort array in order of dates earliest first
    dates.sort(function(a, b) {
        return a - b
    })

    // Generate data object with correct labels
    dates.forEach(function(value, index){
        formatted_data.push({"label": value})
    })

    reviews_data.forEach(function(value, index){
        dates.forEach(function(data, data_index){
            let temp = value.filter(obj => {
                return obj.label === data
            })
            if(temp.length > 0){
                formatted_data[data_index][compare_game_data[index].name] = {
                    "percentage": temp[0].percentage,
                    "number_of_reviews": temp[0].number_of_reviews,
                }
            } else {
                formatted_data[data_index][compare_game_data[index].name] = {
                    "percentage": 0,
                    "number_of_reviews": 0,
                }
            }
        })

    })

    return formatted_data

}

function get_data_reviews_past_six_months_compare(ids) {

    let temp_data
    let reviews_data = []

    ids.forEach(function(value, index){

        let api_url = `/api/get-reviews/past-six-months/${value}/`

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
        
        reviews_data.push(temp_data)

    })

    let values = [] //Stores the years from the data
    let dates = []
    let formatted_data = []

    // Get All dates from all datasets
    reviews_data.forEach(function(value, index){
        values.push(value.map(function(data){
            return data.label
        }))
    })

    // Organise all the dates into a single array so there are no duplicated
    values.forEach(function(value, index){
        value.forEach(function(data, data_index){
            if(!dates.includes(data)){
                dates.push(data)
            }
        })
    })

    // Sort array in order of dates earliest first
    dates.sort(function(a, b) {
        return a - b
    })

    // Generate data object with correct labels
    dates.forEach(function(value, index){
        formatted_data.push({"label": value})
    })

    reviews_data.forEach(function(value, index){
        dates.forEach(function(data, data_index){
            let temp = value.filter(obj => {
                return obj.label === data
            })
            if(temp.length > 0){
                formatted_data[data_index][compare_game_data[index].name] = {
                    "percentage": temp[0].percentage,
                    "number_of_reviews": temp[0].number_of_reviews,
                }
            } else {
                formatted_data[data_index][compare_game_data[index].name] = {
                    "percentage": 0,
                    "number_of_reviews": 0,
                }
            }
        })

    })

    return formatted_data

}

function get_data_reviews_past_one_month_compare(ids) {

    let temp_data
    let reviews_data = []

    ids.forEach(function(value, index){

        let api_url = `/api/get-reviews/past-one-month/${value}/`

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
        
        reviews_data.push(temp_data)

    })

    let values = [] //Stores the years from the data
    let dates = []
    let formatted_data = []

    // Get All dates from all datasets
    reviews_data.forEach(function(value, index){
        values.push(value.map(function(data){
            return data.label
        }))
    })

    // Organise all the dates into a single array so there are no duplicated
    values.forEach(function(value, index){
        value.forEach(function(data, data_index){
            if(!dates.includes(data)){
                dates.push(data)
            }
        })
    })

    // Sort array in order of dates earliest first
    dates.sort(function(a, b) {
        return a - b
    })

    // Generate data object with correct labels
    dates.forEach(function(value, index){
        formatted_data.push({"label": value})
    })

    reviews_data.forEach(function(value, index){
        dates.forEach(function(data, data_index){
            let temp = value.filter(obj => {
                return obj.label === data
            })
            if(temp.length > 0){
                formatted_data[data_index][compare_game_data[index].name] = {
                    "percentage": temp[0].percentage,
                    "number_of_reviews": temp[0].number_of_reviews,
                }
            } else {
                formatted_data[data_index][compare_game_data[index].name] = {
                    "percentage": 0,
                    "number_of_reviews": 0,
                }
            }
        })

    })

    return formatted_data

}

function get_data_reviews_past_two_weeks_compare(ids) {

    let temp_data
    let reviews_data = []

    ids.forEach(function(value, index){

        let api_url = `/api/get-reviews/past-two-weeks/${value}/`

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
        
        reviews_data.push(temp_data)

    })

    let values = [] //Stores the years from the data
    let dates = []
    let formatted_data = []

    // Get All dates from all datasets
    reviews_data.forEach(function(value, index){
        values.push(value.map(function(data){
            return data.label
        }))
    })

    // Organise all the dates into a single array so there are no duplicated
    values.forEach(function(value, index){
        value.forEach(function(data, data_index){
            if(!dates.includes(data)){
                dates.push(data)
            }
        })
    })

    // Sort array in order of dates earliest first
    dates.sort(function(a, b) {
        return a - b
    })

    // Generate data object with correct labels
    dates.forEach(function(value, index){
        formatted_data.push({"label": value})
    })

    reviews_data.forEach(function(value, index){
        dates.forEach(function(data, data_index){
            let temp = value.filter(obj => {
                return obj.label === data
            })
            if(temp.length > 0){
                formatted_data[data_index][compare_game_data[index].name] = {
                    "percentage": temp[0].percentage,
                    "number_of_reviews": temp[0].number_of_reviews,
                }
            } else {
                formatted_data[data_index][compare_game_data[index].name] = {
                    "percentage": 0,
                    "number_of_reviews": 0,
                }
            }
        })

    })

    return formatted_data

}

function get_data_reviews_past_one_week_compare(ids) {

    let temp_data
    let reviews_data = []

    ids.forEach(function(value, index){

        let api_url = `/api/get-reviews/past-one-week/${value}/`

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
        
        reviews_data.push(temp_data)

    })

    let values = [] //Stores the years from the data
    let dates = []
    let formatted_data = []

    // Get All dates from all datasets
    reviews_data.forEach(function(value, index){
        values.push(value.map(function(data){
            return data.label
        }))
    })

    // Organise all the dates into a single array so there are no duplicated
    values.forEach(function(value, index){
        value.forEach(function(data, data_index){
            if(!dates.includes(data)){
                dates.push(data)
            }
        })
    })

    // Sort array in order of dates earliest first
    dates.sort(function(a, b) {
        return a - b
    })

    // Generate data object with correct labels
    dates.forEach(function(value, index){
        formatted_data.push({"label": value})
    })

    reviews_data.forEach(function(value, index){
        dates.forEach(function(data, data_index){
            let temp = value.filter(obj => {
                return obj.label === data
            })
            if(temp.length > 0){
                formatted_data[data_index][compare_game_data[index].name] = {
                    "percentage": temp[0].percentage,
                    "number_of_reviews": temp[0].number_of_reviews,
                }
            } else {
                formatted_data[data_index][compare_game_data[index].name] = {
                    "percentage": 0,
                    "number_of_reviews": 0,
                }
            }
        })

    })

    return formatted_data

}
