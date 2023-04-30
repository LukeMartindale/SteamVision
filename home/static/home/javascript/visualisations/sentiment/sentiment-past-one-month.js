function get_data_sentiment_past_one_month(id){

    let api_url = `/api/get-sentiment/past-one-month/${id}/`

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

function sentiment_past_one_month(id){

    let reviews_data = get_data_sentiment_past_one_month(id)

    // CHECK WHAT MAX VALUE IS
    let max_value = 0
    reviews_data.forEach(function(item, index){
        if(item.value > max_value){
            max_value = item.value
        }
    })

    
    if(max_value > 0){

        $('#sentiment-graph').empty()
        $("#sentiment-container-content").find(".tooltip").remove()
        $("#sentiment-container-content").find(".no-data").remove()

        let margins = {top: 0, bottom: 0, left: 0, right: 0}

        // MARGINS
        if ($(window).width() <= 475) {

            margins = {top: 15, bottom: 25, left: 25, right: 0}

        } else {

            margins = {top: 15, bottom: 25, left: 50, right: 0}

        }

        let svgWidth = $('#sentiment-container-content').width() - margins.left - margins.right
        let svgHeight = 440 - margins.top - margins.bottom
        // let svgHeight = ($('#sentiment-box').width()*0.7) - margins.top - margins.bottom
        
        let chartContainer = d3
            .select('#sentiment-graph')
            .attr('width', svgWidth + margins.left + margins.right)
            .attr('height', svgHeight + margins.top + margins.bottom);

        let x = d3.scaleBand().rangeRound([0, svgWidth]).padding(0.1);
        let y = d3.scaleLinear().range([svgHeight, 0]);
        
        x.domain(reviews_data.map(data => data.label));
        y.domain([0, Math.floor((d3.max(reviews_data, data=> data.value) + (d3.max(reviews_data, data => data.value))*0.1))]);

        // let max_val = Math.floor((d3.max(reviews_data, data=> data.value) + ((d3.max(reviews_data, data => data.value))*0.1)) / 10) * 10
        
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

        // GRAPH TITLE
        if ($(window).width() <= 475) {
            // GRAPH TITLE
            chartContainer
                .append('text')
                .attr('y', 12)
                .attr('x', svgWidth/2.25)
                .attr('fill', '#bec5cb')
                .attr('font-size', 14)
                .attr('font-weight', 'bold')
                .text("Past One Month");
        } else {
            // GRAPH TITLE
            chartContainer
                .append('text')
                .attr('y', 10)
                .attr('x', svgWidth/2)
                .attr('fill', '#bec5cb')
                .attr('font-size', 16)
                .attr('font-weight', 'bold')
                .text("Past One Month");
        }

        //BARS
        chart
            .selectAll('.bar')
            .data(reviews_data, data => data.id)
            .enter()
            .append('rect')
            .classed('bar', true)
            .attr('width', x.bandwidth())
            .attr('height', data => svgHeight - y(data.value))
            .attr('x', data => x(data.label))
            .attr('y', data => y(data.value))
            .attr('id', data => (("sentiment-bar-" + data.label).replace(".", '')))
            .append('title')
            .text((data) => `Sentiment Value: ${data.label}\nNumber of Reviews: ${data.value}`);

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
            mouseleave()
            if (event.target.classList.contains("bar")){
                tooltip
                    .html("Sentiment Score: " + event.target.__data__.label + "<br>" + "Number of Reviews: " + event.target.__data__.value)
                    .style("display", "block")
                    .style("opacity", 1)
            }
        }

        let mousemove = function(event, data) {
            let x_co = -50
            if(event.x > ($(window).width()/2)){
                x_co = 250
            }
            let y_co = $(".detail-block-wrapper").height() + $("#reviews-game-section").height() - $(".game-content-selector").height()
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

        sentiment_update_current_value(reviews_data, "one-month")

    } else {
        $('#sentiment-graph').empty()
        $("#sentiment-container-content").find(".tooltip").remove()
        $("#sentiment-container-content").find(".no-data").remove()

        $("#sentiment-container-content").prepend('<div class="no-data">Sorry there was no data for this timeframe</div>')
        sentiment_update_current_value(reviews_data, "one-month")
    }
    
}