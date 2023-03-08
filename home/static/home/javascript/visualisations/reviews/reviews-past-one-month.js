function get_data_reviews_past_one_month(id){

    let api_url = `/api/get-reviews/past-one-month/${id}/`

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

function reviews_past_one_month(id){

    let reviews_data = get_data_reviews_past_one_month(id)

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

    let x = d3.scaleBand().rangeRound([0, svgWidth]).padding(0.1);
    let y = d3.scaleLinear().range([svgHeight, 0]);

    let chartContainer = d3
        .select("#reviews-graph")
        .attr('width', svgWidth + margins.left + margins.right)
        .attr('height', svgHeight + margins.top + margins.bottom);

    x.domain(reviews_data.map(data => data.label));
    y.domain([0, 100]);

    let chart = chartContainer
        .append('g')
        .attr("transform", `translate(${margins.left},${margins.top})`);
        
    if($(window).width() <= 800 && $(window).width() > 400){
        //X-AXIS TICKS
        chart
            .append('g')
            .call(d3.axisBottom(x).tickSizeOuter(5))
            .attr('transform', `translate(0, ${svgHeight})`)
            .attr('color', '#bec5cb')
            .attr('font-size', 10)
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
            .attr('font-size', 8)
            .attr('font-weight', 'bold')
            .selectAll("text")  
            .style("text-anchor", "end")
            .attr("dx", "-.8em")
            .attr("dy", "-.15em")
            .attr("transform", "rotate(-65)");
    } else {
        //X-AXIS TICKS
        chart
            .append('g')
            .call(d3.axisBottom(x).tickSize(5))
            .attr('transform', `translate(0, ${svgHeight})`)
            .attr('color', '#bec5cb')
            .attr('font-size', 12)
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
            .attr('font-size', 20)
            .attr('font-weight', 'bold')
            .text("Day");
    } else {
        // X AXIS LABELS 
        chart
            .append('text')
            .attr('transform', `translate(${svgWidth/2 - margins.left + 10}, ${svgHeight + 125})`)
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
            .text("Past Month");
    } else {
        // GRAPH TITLE
        chartContainer
            .append('text')
            .attr('y', 10)
            .attr('x', svgWidth/1.92)
            .attr('fill', '#bec5cb')
            .attr('font-size', 16)
            .attr('font-weight', 'bold')
            .text("Past Month");
    }

    //NEG BARS
    chart
        .selectAll('.neg-bar')
        .data(reviews_data, data => data.label)
        .enter()
        .append('rect')
            .classed('neg-bar', true)
            .attr('width', x.bandwidth())
            .attr('height', svgHeight - y(100))
            .attr('x', data => x(data.label))
            .attr('y', y(100))
            .attr('id', data => data.label + "-")
            .property('value', data => Math.round(data.number_of_reviews * (((100 - data.percentage) / 100))))
            .append('title')
            .text((data) => `Percentage negative reviews: ${(100 - data.percentage).toFixed(1)}%\nNumber of negative reviews: ${Math.round(data.number_of_reviews * (((100 - data.percentage) / 100)))}\nDate: ${data.label}`);
    
    //BARS
    chart
        .selectAll('.bar')
        .data(reviews_data, data => data.label)
        .enter()
        .append('rect')
            .classed('bar', true)
            .attr('width', x.bandwidth())
            .attr('height', data => svgHeight - y(data.percentage))
            .attr('x', data => x(data.label))
            .attr('y', data => y(data.percentage))
            .attr('id', data => data.label + "+")
            .append('title')
            .text((data) => `Percentage positive reviews: ${data.percentage}%\nNumber of positive reviews: ${Math.round(data.number_of_reviews * (data.percentage / 100))}\nDate: ${data.label}`);

    reviews_update_current_total(reviews_data)
    no_reviews_neutral_bar()

}