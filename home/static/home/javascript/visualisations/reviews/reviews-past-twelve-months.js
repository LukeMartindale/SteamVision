function get_data_reviews_past_twelve_months(id){

    let api_url = `/api/get-reviews/past-twelve-months/${id}/`

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

function reviews_past_twelve_months(id){

    let reviews_data = get_data_reviews_past_twelve_months(id)

    $('#reviews-graph').empty()
    $("#reviews-container-content").find(".tooltip").remove()

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
            .text("Dates");
    } else if ($(window).width() <= 450) {
        // X AXIS LABELS 
        chart
            .append('text')
            .attr('transform', `translate(${svgWidth/2 - margins.left}, ${svgHeight + 115})`)
            .attr('fill', '#bec5cb')
            .attr('font-size', 15)
            .attr('font-weight', 'bold')
            .text("Dates");
    } else {
        // X AXIS LABELS 
        chart
            .append('text')
            .attr('transform', `translate(${svgWidth/2 - margins.left + 10}, ${svgHeight + 115})`)
            .attr('fill', '#bec5cb')
            .attr('font-size', 20)
            .attr('font-weight', 'bold')
            .text("Dates");
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
            .attr('x', svgWidth/2.55)
            .attr('fill', '#bec5cb')
            .attr('font-size', 14)
            .attr('font-weight', 'bold')
            .text("Past 12 Months");
    } else {
        // GRAPH TITLE
        chartContainer
            .append('text')
            .attr('y', 10)
            .attr('x', svgWidth/2.25)
            .attr('fill', '#bec5cb')
            .attr('font-size', 16)
            .attr('font-weight', 'bold')
            .text("Past 12 Months");
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

    let mouseover = function(event, data) {
        mouseleave()
        if(event.target.classList.contains("neutral-bar")){
            tooltip
                .html("No Reviews")
                .style("display", "block")
                .style("opacity", 1)
        } else if (event.target.classList.contains("bar")){
            tooltip
                .html("Positive Reviews" + "<br>" + "Percentage Positive Reviews: " + (event.target.__data__.percentage).toFixed(1) + "%" + "<br>" + "Number of Reviews: " + Math.round(event.target.__data__.number_of_reviews * (event.target.__data__.percentage / 100)))
                .style("display", "block")
                .style("opacity", 1)
        } else if (event.target.classList.contains("neg-bar")) {
            if(event.target.__data__.number_of_reviews > 0){
                neg_percentage = (100 - event.target.__data__.percentage).toFixed(1)
                neg_reviews = Math.round(event.target.__data__.number_of_reviews * (neg_percentage / 100))
            }
            tooltip
                .html("Negative Reviews" + "<br>" + "Percentage Negative Reviews: " + neg_percentage + "%" + "<br>" + "Number of Reviews: " + neg_reviews)
                .style("display", "block")
                .style("opacity", 1)
        }
    }


    let mousemove = function(event, data) {
        let x_co = -50
        if(event.x > ($(window).width()/2)){
            x_co = 250
        }
        let y_co = $(".detail-block-wrapper").height()/1.5
        tooltip
            .style("transform", "translateY(-55%)")
            .style("left", (event.x) - x_co + "px")
            .style("top", (event.y) + y_co + "px")
    }

    let mouseleave = function(event, data) {
        tooltip
            .style("display", "none")
            .style("opacity", 0)
    }


    chart
        .on("mouseover", mouseover)
        .on("mousemove", mousemove)
        .on("mouseleave", mouseleave)


    reviews_update_current_total(reviews_data)
    no_reviews_neutral_bar()

}
