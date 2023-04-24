function sentiment_all_time_compare(ids){

    let reviews_data = get_data_sentiment_all_time_compare(ids)

    $('#sentiment-graph').empty()

    let margins = {top: 0, bottom: 0, left: 0, right: 0}

    // MARGINS
    if ($(window).width() <= 475) {

        margins = {top: 15, bottom: 25, left: 25, right: 0}

    } else {

        margins = {top: 15, bottom: 25, left: 50, right: 0}

    }

    let svgWidth = $('#sentiment-container-content').width() - margins.left - margins.right
    let svgHeight = 440 - margins.top - margins.bottom

    let chartContainer = d3
        .select('#sentiment-graph')
        .attr('width', svgWidth + margins.left + margins.right)
        .attr('height', svgHeight + margins.top + margins.bottom);


    let chart = chartContainer
        .append('g')
        .attr("transform", `translate(${margins.left},${margins.top})`);
    
    // GROUP AND SUBGROUPS
    let groups = reviews_data.map(data => data.label)
    let subgroups = Object.keys(reviews_data[0])
    subgroups.shift()
    
    // X, Y AND Xsub SETUP
    let x = d3.scaleBand()
        .domain(groups)
        .range([0, svgWidth])
        .padding(0.1)
    let y = d3.scaleLinear()
        .domain([0, 1200])
        .range([svgHeight, 0]);
    let xsub = d3.scaleBand()
        .domain(subgroups)
        .range([0, x.bandwidth()])
        .padding([0.05])

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
            .text("All Time");
    } else {
        // GRAPH TITLE
        chartContainer
            .append('text')
            .attr('y', 10)
            .attr('x', svgWidth/1.92)
            .attr('fill', '#bec5cb')
            .attr('font-size', 16)
            .attr('font-weight', 'bold')
            .text("All Time");
    }

    
    //COLOURS
    let colour = d3.scaleOrdinal()
        .domain(subgroups)
        .range(['#e41a1c','#377eb8','#4daf4a'])

    //BARS
    chart
        .selectAll("g")
        .data(reviews_data)
        .join("g")
            .attr("transform", data => `translate(${x(data.label)}, 0)` )
        .selectAll("rect")
        .data(function(data) {return subgroups.map(function(key) { return {key: key, value: data[key]}; }); })
        .join("rect")
            .attr("x", data => xsub(data.key))
            .attr("y", data => y(data.value))
            .attr("width", xsub.bandwidth())
            .attr("height", data => svgHeight - y(data.value))
            .attr("fill", data => colour(data.key))

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
            .attr("dy", ".15em")
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
            .attr('transform', `translate(${svgWidth/2 - margins.left - 20}, ${svgHeight + 58})`)
            .attr('fill', '#bec5cb')
            .attr('font-size', 20)
            .attr('font-weight', 'bold')
            .text("Sentiment Score");
    } else if ($(window).width() <= 400) {
        // X AXIS LABELS 
        chart
            .append('text')
            .attr('transform', `translate(${svgWidth/2 - margins.left - 20}, ${svgHeight + 58})`)
            .attr('fill', '#bec5cb')
            .attr('font-size', 15)
            .attr('font-weight', 'bold')
            .text("Sentiment Score");
    } else {
        // X AXIS LABELS 
        chart
            .append('text')
            .attr('transform', `translate(${svgWidth/2 - margins.left - 20}, ${svgHeight + 50})`)
            .attr('fill', '#bec5cb')
            .attr('font-size', 20)
            .attr('font-weight', 'bold')
            .text("Sentiment Score");
    }


    // Y AXIS TICKS
    if ($(window).width() <= 400) {
        if(1200 < 10) {
        //Y-AXIS TICKS
        chart
            .append('g')
            .call(d3.axisLeft(y).tickSizeInner(-svgWidth).ticks(1200+1))
            .attr('color', '#bec5cb')
            .attr('font-size', 12);
        } else {
            chart
            .append('g')
            .call(d3.axisLeft(y).tickSizeInner(-svgWidth).ticks(10))
            .attr('color', '#bec5cb')
            .attr('font-size', 12);
        }
    } else {
        if(1200 < 10) {
        //Y-AXIS TICKS
        chart
            .append('g')
            .call(d3.axisLeft(y).tickSizeInner(-svgWidth).ticks(1200+1))
            .attr('color', '#bec5cb')
            .attr('font-size', 15)
        } else {
            chart
            .append('g')
            .call(d3.axisLeft(y).tickSizeInner(-svgWidth).ticks(10))
            .attr('color', '#bec5cb')
            .attr('font-size', 15)
        }

    }

}