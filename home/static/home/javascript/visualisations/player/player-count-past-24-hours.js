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

let temp_data = [
    {
        "id": 9193,
        "player_count": 3,
        "timestamp": "2023-03-14T13:02:32.928615Z",
        "app_id": 542050
    },
    {
        "id": 9217,
        "player_count": 1,
        "timestamp": "2023-03-14T14:02:38.236588Z",
        "app_id": 542050
    },
    {
        "id": 9241,
        "player_count": 0,
        "timestamp": "2023-03-14T15:02:58.923479Z",
        "app_id": 542050
    },
    {
        "id": 9265,
        "player_count": 2,
        "timestamp": "2023-03-14T16:02:41.235735Z",
        "app_id": 542050
    },
    {
        "id": 9289,
        "player_count": 0,
        "timestamp": "2023-03-14T17:03:21.406404Z",
        "app_id": 542050
    },
    {
        "id": 9313,
        "player_count": 3,
        "timestamp": "2023-03-14T18:02:40.055425Z",
        "app_id": 542050
    },
    {
        "id": 9337,
        "player_count": 2,
        "timestamp": "2023-03-14T19:03:24.312965Z",
        "app_id": 542050
    },
    {
        "id": 9361,
        "player_count": 3,
        "timestamp": "2023-03-14T20:03:14.448389Z",
        "app_id": 542050
    },
    {
        "id": 9385,
        "player_count": 2,
        "timestamp": "2023-03-14T21:03:14.599040Z",
        "app_id": 542050
    },
    {
        "id": 9409,
        "player_count": 2,
        "timestamp": "2023-03-14T22:03:05.828535Z",
        "app_id": 542050
    },
    {
        "id": 9433,
        "player_count": 2,
        "timestamp": "2023-03-14T23:02:48.136706Z",
        "app_id": 542050
    },
    {
        "id": 9457,
        "player_count": 2,
        "timestamp": "2023-03-15T01:04:09.490972Z",
        "app_id": 542050
    },
    {
        "id": 9481,
        "player_count": 0,
        "timestamp": "2023-03-15T04:04:05.083872Z",
        "app_id": 542050
    },
    {
        "id": 9505,
        "player_count": 1,
        "timestamp": "2023-03-15T05:02:55.733516Z",
        "app_id": 542050
    },
    {
        "id": 9529,
        "player_count": 2,
        "timestamp": "2023-03-15T06:04:15.875585Z",
        "app_id": 542050
    },
    {
        "id": 9553,
        "player_count": 0,
        "timestamp": "2023-03-15T07:04:06.199747Z",
        "app_id": 542050
    },
    {
        "id": 9577,
        "player_count": 1,
        "timestamp": "2023-03-15T08:02:50.065325Z",
        "app_id": 542050
    },
    {
        "id": 9601,
        "player_count": 1,
        "timestamp": "2023-03-15T09:03:46.216606Z",
        "app_id": 542050
    },
    {
        "id": 9625,
        "player_count": 1,
        "timestamp": "2023-03-15T10:03:06.072924Z",
        "app_id": 542050
    },
    {
        "id": 9649,
        "player_count": 1,
        "timestamp": "2023-03-15T11:03:27.001082Z",
        "app_id": 542050
    },
    {
        "id": 9673,
        "player_count": 1,
        "timestamp": "2023-03-15T12:03:09.621421Z",
        "app_id": 542050
    },
    {
        "id": 9697,
        "player_count": 1,
        "timestamp": "2023-03-15T13:03:26.771644Z",
        "app_id": 542050
    }
]

function player_count_past_24_hours(id){

    let player_data = get_data_player_count_past_24_hours(id)

    player_data.forEach(function(data, index){
        player_data[index].timestamp = new Date(data.timestamp)
    })

    temp_data.forEach(function(data, index){
        temp_data[index].timestamp = new Date(data.timestamp)
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

    console.log(svgWidth)


    let chartContainer = d3
        .select('#player-graph')
        .attr('width', svgWidth + margins.left + margins.right)
        .attr('height', svgHeight + margins.top + margins.bottom);

    
    let x = d3.scaleTime()
        .domain(d3.extent(player_data, function(data) {return data.timestamp; }))
        .range([0, svgWidth])

    let y = d3.scaleLinear()
        .domain([0, d3.max(player_data, function(data) {return data.player_count})])
        .range([svgHeight, 0]);

    let chart = chartContainer
        .append("g")
        .attr("transform", `translate(${margins.left},${margins.top})`);



    if($(window).width() <= 800 && $(window).width() > 400){
        //X-AXIS TICKS
        chart
            .append('g')
            .call(d3.axisBottom(x).tickSizeOuter(5))
            .attr('transform', `translate(0, ${svgHeight})`)
            .attr('color', '#bec5cb')
            .attr('font-size', 15)
            .attr('font-weight', 'bold')
            .selectAll("text")  
            .style("text-anchor", "end")
            .attr("dx", "-.8em")
            .attr("dy", ".15em")
            .attr("transform", "rotate(-90)");

    } else if ($(window).width() <= 400) {
        //X-AXIS TICKS
        chart
            .append('g')
            .call(d3.axisBottom(x).tickSizeOuter(5))
            .attr('transform', `translate(0, ${svgHeight})`)
            .attr('color', '#bec5cb')
            .attr('font-size', 11)
            .attr('font-weight', 'bold')
            .selectAll("text")  
            .style("text-anchor", "end")
            .attr("dx", "-.8em")
            .attr("dy", "-.4em")
            .attr("transform", "rotate(-90)");
    } else {
        //X-AXIS TICKS
        chart
            .append('g')
            .call(d3.axisBottom(x).tickSize(5))
            .attr('transform', `translate(0, ${svgHeight})`)
            .attr('color', '#bec5cb')
            .attr('font-size', 15)
            .attr('font-weight', 'bold');
    }



    // X-AXIS LABELS
    if($(window).width() <= 800 && $(window).width() > 400){
        // X AXIS LABELS 
        chart
            .append('text')
            .attr('transform', `translate(${svgWidth/2 - margins.left + 20}, ${svgHeight + 100})`)
            .attr('fill', '#bec5cb')
            .attr('font-size', 20)
            .attr('font-weight', 'bold')
            .text("Time");
    } else if ($(window).width() <= 400) {
        // X AXIS LABELS 
        chart
            .append('text')
            .attr('transform', `translate(${svgWidth/2 - margins.left}, ${svgHeight + 80})`)
            .attr('fill', '#bec5cb')
            .attr('font-size', 15)
            .attr('font-weight', 'bold')
            .text("Time");
    } else {
        // X AXIS LABELS 
        chart
            .append('text')
            .attr('transform', `translate(${svgWidth/2 - margins.left}, ${svgHeight + 80})`)
            .attr('fill', '#bec5cb')
            .attr('font-size', 20)
            .attr('font-weight', 'bold')
            .text("Time");
    }



    // Y AXIS TICKS
    if ($(window).width() <= 400) {
        //Y-AXIS TICKS
        chart
            .append('g')
            .call(d3.axisLeft(y).tickSizeInner(-svgWidth).tickValues(y.ticks().filter(Number.isInteger)).tickFormat(d3.format('d')))
            .attr('color', '#bec5cb')
            .attr('font-size', 12);

    } else {
        //Y-AXIS TICKS
        chart
            .append('g')
            .call(d3.axisLeft(y).tickSizeInner(-svgWidth).tickValues(y.ticks().filter(Number.isInteger)).tickFormat(d3.format('d')))
            .attr('color', '#bec5cb')
            .attr('font-size', 15);
    }

    // Y AXIS LABELS
    if ($(window).width() <= 475) {
        chartContainer
            .append('text')
            .attr('y', -12.5)
            .attr('x', -($("#player-count-container-content").height()/1.95))
            .attr("transform", "rotate(-90)")
            .attr('fill', '#bec5cb')
            .attr('font-size', 15)
            .attr('font-weight', 'bold')
            .text("Number of Players");
    } else {
        chartContainer
            .append('text')
            .attr('y', 0)
            .attr('x', -($("#player-count-container-content").height()/1.95))
            .attr("transform", "rotate(-90)")
            .attr('fill', '#bec5cb')
            .attr('font-size', 20)
            .attr('font-weight', 'bold')
            .text("Number of Players");
    }

    // GRAPH TITLE
    if ($(window).width() <= 475) {
        // GRAPH TITLE
        chartContainer
            .append('text')
            .attr('y', 12)
            .attr('x', svgWidth/2.05)
            .attr('fill', '#bec5cb')
            .attr('font-size', 14)
            .attr('font-weight', 'bold')
            .text("Past 24 Hours");
    } else {
        // GRAPH TITLE
        chartContainer
            .append('text')
            .attr('y', 10)
            .attr('x', svgWidth/1.92)
            .attr('fill', '#bec5cb')
            .attr('font-size', 16)
            .attr('font-weight', 'bold')
            .text("Past 24 Hours");
    }

    // ADD CHART LINE
    chart
        .append("path")
        .datum(player_data)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 4)
        .attr("d", d3.line()
            .x(function(data) {return x(data.timestamp)})
            .y(function(data) {return y(data.player_count)})
        )

    // // ADD RED CIRCLES
    // chart.selectAll("myCircles")
    //     .data(player_data)
    //     .join("circle")
    //       .attr("fill", "red")
    //       .attr("stroke", "none")
    //       .attr("cx", d => x(d.timestamp))
    //       .attr("cy", d => y(d.player_count))
    //       .attr("r", 3)

}
