function reviews_past_two_weeks_compare(ids) {

    let reviews_data = get_data_reviews_past_two_weeks_compare(ids)

    if(reviews_data.length > 0) {
    
        $('#reviews-graph').empty()

        let margins = {top: 0, bottom: 0, left: 0, right: 0}

        // MARGINS
        if ($(window).width() <= 475) {
    
            margins = {top: 25, bottom: 35, left: 25, right: 0}
    
        } else {
    
            margins = {top: 25, bottom: 35, left: 50, right: 0}
    
        }

        let svgWidth = $('#reviews-container-content').width() - margins.left - margins.right
        let svgHeight = 440 - margins.top - margins.bottom

        let chartContainer = d3
            .select('#reviews-graph')
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
            .domain([0, 100])
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
                .text("Past 2 Weeks");
        } else {
            // GRAPH TITLE
            chartContainer
                .append('text')
                .attr('y', 10)
                .attr('x', svgWidth/1.92)
                .attr('fill', '#bec5cb')
                .attr('font-size', 16)
                .attr('font-weight', 'bold')
                .text("Past 2 Weeks");
        }

        //COLOURS
        let colour = d3.scaleOrdinal()
            .domain(subgroups)
            .range(compare_review_colours)


        if($(window).width() <= 800 && $(window).width() > 400){
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
                .attr("transform", "rotate(-65)");
    
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
                .attr("transform", "rotate(-65)");
        } else {
            //X-AXIS TICKS
            chart
                .append('g')
                .call(d3.axisBottom(x).tickSize(5))
                .attr('transform', `translate(0, ${svgHeight})`)
                .attr('color', '#bec5cb')
                .attr('font-size', 11)
                .attr('font-weight', 'bold')
                .selectAll("text")  
                .style("text-anchor", "end")
                .attr("dx", "-.8em")
                .attr("dy", ".15em")
                .attr("transform", "rotate(-65)");
        }
    
        // X-AXIS LABELS
        if($(window).width() <= 800 && $(window).width() > 450){
            // X AXIS LABELS 
            chart
                .append('text')
                .attr('transform', `translate(${svgWidth/2 - margins.left + 10}, ${svgHeight + 115})`)
                .attr('fill', '#bec5cb')
                .attr('font-size', 20)
                .attr('font-weight', 'bold')
                .text("Day");
        } else if ($(window).width() <= 450) {
            // X AXIS LABELS 
            chart
                .append('text')
                .attr('transform', `translate(${svgWidth/2 - margins.left}, ${svgHeight + 115})`)
                .attr('fill', '#bec5cb')
                .attr('font-size', 15)
                .attr('font-weight', 'bold')
                .text("Day");
        } else {
            // X AXIS LABELS 
            chart
                .append('text')
                .attr('transform', `translate(${svgWidth/2 - margins.left + 10}, ${svgHeight + 115})`)
                .attr('fill', '#bec5cb')
                .attr('font-size', 20)
                .attr('font-weight', 'bold')
                .text("Day");
        }

        // Y AXIS TICKS
        if ($(window).width() <= 400) {
            chart
                .append('g')
                .call(d3.axisLeft(y).tickSizeInner(-svgWidth).ticks(10))
                .attr('color', '#bec5cb')
                .attr('font-size', 12);
        } else {
            chart
                .append('g')
                .call(d3.axisLeft(y).tickSizeInner(-svgWidth).ticks(10))
                .attr('color', '#bec5cb')
                .attr('font-size', 15)
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
                .text("Reviews Percentage");
        } else {
            chartContainer
                .append('text')
                .attr('y', 0)
                .attr('x', -($("#sentiment-container-content").height()/1.75))
                .attr("transform", "rotate(-90)")
                .attr('fill', '#bec5cb')
                .attr('font-size', 20)
                .attr('font-weight', 'bold')
                .text("Reviews Percentage");
        }

        // CREATE TOOLTIP
        let tooltip = d3.select('#reviews-container-content')
            .append("div")
            .style("opacity", 0)
            .attr("class", "tooltip")
            .style("background-color", "white")
            .style("border", "solid")
            .style("border-wdith", "1px")
            .style("border-radius", "5px")
            .style("padding", "10px")

        // CREATE NEGATIVE TOOLTIP
        let tooltip_negative = d3.select('#reviews-container-content')
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
                .html("Positive Reviews" + "<br>" + "Game: " + this.__data__.key + "<br>" + "Percentage Positive Reviews: " + (this.__data__.value.percentage).toFixed(1) + "%" + "<br>" + "Number of Reviews: " + Math.round(this.__data__.value.number_of_reviews * (this.__data__.value.percentage / 100)))
                .style("display", "block")
                .style("opacity", 1)
        }

        let mouseover_negative = function(event, data) {
            let html
            if(this.__data__.value.number_of_reviews > 0){
                html = "Negative Reviews" + "<br>" + "Game: " + this.__data__.key + "<br>" + "Percentage Negative Reviews: " + (100 - this.__data__.value.percentage).toFixed(1) + "%" + "<br>" + "Number of Reviews: " + Math.round(this.__data__.value.number_of_reviews * (((100 - this.__data__.value.percentage) / 100)))
            } else {
                html = "No Reviews" + "<br>" + "Game: " + this.__data__.key
            }
            tooltip_negative
                .html(html)
                .style("display", "block")
                .style("opacity", 1)
        }
    
        let mousemove = function(event, data) {
            let x_co = 0
            if(event.x > ($(window).width()/2)){
                x_co = 150
            }
            tooltip
                .style("transform", "translateY(-55%)")
                .style("left", (event.x) - x_co + "px")
                .style("top", (event.y) - 65 + "px")
        }

        let mousemove_negative = function(event, data) {
            let x_co = 0
            if(event.x > ($(window).width()/2)){
                x_co = 150
            }
            tooltip_negative
                .style("transform", "translateY(-55%)")
                .style("left", (event.x) - x_co + "px")
                .style("top", (event.y) - 65 + "px")
        }
    
        let mouseleave = function(event, data) {
            tooltip
                .style("display", "none")
                .style("opacity", 0)
        }

        let mouseleave_negative = function(event, data) {
            tooltip_negative
                .style("display", "none")
                .style("opacity", 0)
        }

                
        let gChart = chart
            .append('g')

        // NEGATIVE BARS
        gChart
            .selectAll("g")
            .data(reviews_data)
            .join("g")
                .attr("transform", data => `translate(${x(data.label)}, 0)` )
            .selectAll('.neg-bar')
            .data(function(data) { return subgroups.map(function(key) { return {key: key, value: data[key]}; }); })
            .enter()
            .append('rect')
                .classed('neg-bar', true)
                .attr('width', xsub.bandwidth())
                .attr('height', svgHeight - y(100))
                .attr('x', data => xsub(data.key))
                .attr('y', y(100))
                .property('value', data => data.value.number_of_reviews)
            .on('mouseover', mouseover_negative)
            .on('mousemove', mousemove_negative)
            .on('mouseout', mouseleave_negative)

        // BARS
        gChart
            .selectAll("g")
            .data(reviews_data)
            .join("g")
                .attr("transform", data => `translate(${x(data.label)}, 0)` )
            .selectAll("bar")
            .data(function(data) { return subgroups.map(function(key) { return {key: key, value: data[key]}; }); })
            .join("rect")
                .classed('bar', true)
                .attr("x", data => xsub(data.key))
                .attr("y", data => y(data.value.percentage))
                .attr("width", xsub.bandwidth())
                .attr("height", data => svgHeight - y(data.value.percentage))
                .attr("fill", data => colour(data.key))
            .on('mouseover', mouseover)
            .on('mousemove', mousemove)
            .on('mouseout', mouseleave)

        no_reviews_neutral_bar()

    } else {
        $('#reviews-graph').empty()
    }

}