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

    let margins = {top: 0, bottom: 0, left: 40, right: 20}
    let svgWidth = $('#reviews-container-content').width() - margins.left - margins.right
    let svgHeight = 400 - margins.top - margins.bottom

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
        .attr("transform", `translate(${margins.left})`);
        
    //X-AXIS LABELS
    chart
        .append('g')
        .call(d3.axisBottom(x).tickSizeOuter(0))
        .attr('transform', `translate(0, ${svgHeight})`)
        .attr('color', '#bec5cb')
        .attr('font-size', 21)
        .selectAll("text")  
        .style("text-anchor", "end")
        .attr("dx", "-.8em")
        .attr("dy", ".15em")
        .attr("transform", "rotate(-65)");
    
    //Y-AXIS LABELS
    chart
        .append('g')
        .call(d3.axisLeft(y))
        .attr('color', '#bec5cb')
        .attr('font-size', 15);

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

    no_reviews_neutral_bar()

}
