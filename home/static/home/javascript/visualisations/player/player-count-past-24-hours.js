function get_data_player_count_past_24_hours(id){

    let api_url = `/api/get-player-count/past-24-hours/${id}/`

    let reviews = function(){
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

    return reviews

}

function player_count_past_24_hours(id){

    let player_data = get_data_player_count_past_24_hours(id)

    console.log(player_data)

    $("#player-count-container-content").empty()

    let margins = {top: 10, bottom: 0, left: 40, right: 20}
    let svgWidth = $('.visualisation-container-content').width()
    let svgHeight = 400 - margins.top - margins.bottom

    function test (data){
        data.forEach(function(d){
            console.log(Date(d.timestamp))
        })
    }

    test(player_data)
    

    let x = d3.scaleTime()
        .domain(d3.extent(player_data, function(data) {return data.timestamp; }))
        .range([0, svgWidth])

    let y = d3.scaleLinear()
        .domain([0, d3.max(player_data, function(data) {return data.player_count})])
        .range([svgHeight, 0]);

    let svg = d3.select('#player-count-container-content')
        .append("svg")
            .attr("width", svgWidth)
            .attr("height", svgHeight)
        .append("g")
            .attr("transform", `translate(${margins.left},${margins.top})`);

    //X-AXIS LABELS
    svg
        .append('g')
        .call(d3.axisBottom(x).tickSizeOuter(0))
        .attr('transform', `translate(0, ${svgHeight})`)
        .attr('color', '#bec5cb')
        .attr('font-size', 20);
    
    //Y-AXIS LABELS
    svg
        .append('g')
        .call(d3.axisLeft(y))
        .attr('color', '#bec5cb')
        .attr('font-size', 15);

}
