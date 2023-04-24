function sentiment_past_two_weeks_compare(ids){

    let reviews_data = get_data_sentiment_past_two_weeks_compare(ids)

    if(reviews_data.length > 0) {
        $('#sentiment-graph').empty()
        $('#sentiment-container-content').find(".tooltip").remove()
    
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
    
        // GET MAX VALUE FOR Y AXIS SCALING
        let max_value = 0
        subgroups.forEach(function(value, index){
            reviews_data.forEach(function(data, data_index){
                if(data[value] > max_value){
                    max_value = data[value]
                }
            })
        })
        
        // X, Y AND Xsub SETUP
        let x = d3.scaleBand()
            .domain(groups)
            .range([0, svgWidth])
            .padding(0.1)
        let y = d3.scaleLinear()
            .domain([0, (max_value + max_value*0.1)])
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
                .text("Past Two Weeks");
        } else {
            // GRAPH TITLE
            chartContainer
                .append('text')
                .attr('y', 10)
                .attr('x', svgWidth/1.92)
                .attr('fill', '#bec5cb')
                .attr('font-size', 16)
                .attr('font-weight', 'bold')
                .text("Past Two Weeks");
        }
        
        //COLOURS
        let colour = d3.scaleOrdinal()
            .domain(subgroups)
            .range(compare_sentiment_colours)
    
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
            if(max_value < 10) {
            //Y-AXIS TICKS
            chart
                .append('g')
                .call(d3.axisLeft(y).tickSizeInner(-svgWidth).ticks(max_value+1))
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
            if(max_value < 10) {
            //Y-AXIS TICKS
            chart
                .append('g')
                .call(d3.axisLeft(y).tickSizeInner(-svgWidth).ticks(max_value+1))
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
    
        // Y AXIS LABELS
        if ($(window).width() <= 475) {
            chartContainer
                .append('text')
                .attr('y', -12.5)
                .attr('x', -($("#sentiment-container-content").height()/1.75))
                .attr("transform", "rotate(-90)")
                .attr('fill', '#bec5cb')
                .attr('font-size', 15)
                .attr('font-weight', 'bold')
                .text("Number of Reviews");
        } else {
            chartContainer
                .append('text')
                .attr('y', 0)
                .attr('x', -($("#sentiment-container-content").height()/1.75))
                .attr("transform", "rotate(-90)")
                .attr('fill', '#bec5cb')
                .attr('font-size', 20)
                .attr('font-weight', 'bold')
                .text("Number of Reviews");
        }
    
    
        // CREATE TOOLTIP
        let tooltip = d3.select('#sentiment-container-content')
            .append("div")
            .style("opacity", 0)
            .attr("class", "tooltip")
            .style("background-color", "white")
            .style("border", "solid")
            .style("border-wdith", "1px")
            .style("border-radius", "5px")
            .style("padding", "10px")
    
        let mouseover = function(event, data) {
            tooltip
                .html("Game: " + this.__data__.key + "<br>" + "Value: " + this.__data__.value)
                .style("display", "block")
                .style("opacity", 1)
        }
    
        let mousemove = function(event, data) {
            tooltip
                .style("transform", "translateY(-55%)")
                .style("left", (event.x) + "px")
                .style("top", (event.y) - 30 + "px")
        }
    
        let mouseleave = function(event, data) {
            tooltip
                .style("display", "none")
                .style("opacity", 0)
        }
        
        let gChart = chart
            .append('g')
    
        //BARS
        gChart
            .selectAll("g")
            .data(reviews_data)
            .join("g")
                .attr("transform", data => `translate(${x(data.label)}, 0)` )
            .selectAll("rect")
            .data(function(data) {return subgroups.map(function(key) { return {key: key, value: data[key]}; }); })
            .join("rect")
                .classed('bar', true)
                .attr("x", data => xsub(data.key))
                .attr("y", data => y(data.value))
                .attr("width", xsub.bandwidth())
                .attr("height", data => svgHeight - y(data.value))
                .attr("fill", data => colour(data.key))
            .on('mouseover', mouseover)
            .on('mousemove', mousemove)
            .on('mouseout', mouseleave)
    
    } else {
        $('#sentiment-graph').empty()
        $('#sentiment-container-content').find(".tooltip").remove()
    }

}