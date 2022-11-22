const sentiment_data = [
    {'label': '-1', 'value': 2}, 
    {'label': '-0.9', 'value': 3}, 
    {'label': '-0.8', 'value': 1}, 
    {'label': '-0.7', 'value': 3}, 
    {'label': '-0.6', 'value': 5}, 
    {'label': '-0.5', 'value': 14}, 
    {'label': '-0.4', 'value': 59}, 
    {'label': '-0.3', 'value': 9}, 
    {'label': '-0.2', 'value': 41}, 
    {'label': '-0.1', 'value': 55}, 
    {'label': '0', 'value': 539}, 
    {'label': '0.1', 'value': 199}, 
    {'label': '0.2', 'value': 141}, 
    {'label': '0.3', 'value': 178}, 
    {'label': '0.4', 'value': 47}, 
    {'label': '0.5', 'value': 99}, 
    {'label': '0.6', 'value': 47}, 
    {'label': '0.7', 'value': 60}, 
    {'label': '0.8', 'value': 21}, 
    {'label': '0.9', 'value': 13}, 
    {'label': '1', 'value': 64},
]

let margins = {top: 20, bottom: 10, left: 40, right: 20}
let svgWidth = $('#sentiment-box').width() - margins.left - margins.right
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
    .attr('y', data => y(data.value));