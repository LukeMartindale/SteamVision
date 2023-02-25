function get_data_sentiment_past_two_weeks(id){

    let api_url = `/api/get-sentiment/past-two-weeks/${id}/`

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

function sentiment_past_two_weeks(id){

    let reviews_data = get_data_sentiment_past_two_weeks(id)

    console.log(reviews_data)

    $('#sentiment-graph').empty()

    let margins = {top: 10, bottom: 0, left: 40, right: 20}
    let svgWidth = $('#sentiment-container-content').width() - margins.left - margins.right
    let svgHeight = 400 - margins.top - margins.bottom
    // let svgHeight = ($('#sentiment-box').width()*0.7) - margins.top - margins.bottom
    
    let x = d3.scaleBand().rangeRound([0, svgWidth]).padding(0.1);
    let y = d3.scaleLinear().range([svgHeight, 0]);
    
    let chartContainer = d3
        .select('#sentiment-graph')
        .attr('width', svgWidth + margins.left + margins.right)
        .attr('height', svgHeight + margins.top + margins.bottom);
    
    x.domain(reviews_data.map(data => data.label));
    y.domain([0, Math.floor((d3.max(reviews_data, data=> data.value) + (d3.max(reviews_data, data => data.value))*0.1))]);
    
    let chart = chartContainer
        .append('g')
        .attr("transform", `translate(${margins.left})`);
    
    //X-AXIS LABELS
    chart
        .append('g')
        .call(d3.axisBottom(x).tickSizeOuter(0))
        .attr('transform', `translate(0, ${svgHeight})`)
        .attr('color', '#bec5cb')
        .attr('font-size', 20);
    
    //Y-AXIS LABELS
    chart
        .append('g')
        .call(d3.axisLeft(y))
        .attr('color', '#bec5cb')
        .attr('font-size', 15);
    
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

    sentiment_update_current_value(reviews_data)

}