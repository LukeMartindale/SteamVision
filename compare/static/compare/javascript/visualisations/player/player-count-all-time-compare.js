function player_count_all_time_compare(ids){

    console.log("TEST")

    let player_data = get_data_player_count_all_time_compare(ids)
    console.log(player_data)

    player_data.forEach(function(data, index){
        player_data[index].timestamp = new Date(data.timestamp)
    })

    $("#player-graph").empty()

    let margins = {top: 0, bottom: 0, left: 0, right: 0}

    // MARGINS
    if ($(window).width() <= 475) {

        margins = {top: 15, bottom: 5, left: 25, right: 0}

    } else {

        margins = {top: 15, bottom: 5, left: 50, right: 0}

    }

    let svgWidth = $('#player-graph').width() - margins.left - margins.right
    let svgHeight = 440 - margins.top - margins.bottom

}