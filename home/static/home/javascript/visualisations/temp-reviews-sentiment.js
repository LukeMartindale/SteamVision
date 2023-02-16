function sentiment_graph(){

    sentiment_data = reviews_data.sentiment

    $('#sentiment-graph').empty()

    console.log(sentiment_data)

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
    
    x.domain(sentiment_data.map(data => data.label));
    y.domain([0, d3.max(sentiment_data, data=> data.value) + ((d3.max(sentiment_data, data => data.value))*0.1)]);
    
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
        .data(sentiment_data, data => data.id)
        .enter()
        .append('rect')
        .classed('bar', true)
        .attr('width', x.bandwidth())
        .attr('height', data => svgHeight - y(data.value))
        .attr('x', data => x(data.label))
        .attr('y', data => y(data.value))
        .append('title')
        .text((data) => `Sentiment: ${data.label}\nNumber of Reviews: ${data.value}`);
}
