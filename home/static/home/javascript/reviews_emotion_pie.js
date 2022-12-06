function emotion_graph(){

    let emotion_data = reviews_data.emotion[0]

    console.log(emotion_data)

    $('#emotion-box').empty()

    //set the dimensions and margins of the graph
    let margin = 40
    let svgWidth = $('#emotion-box').width()
    let svgHeight = $('#emotion-box').height()

    //radius of the pieplot is half the width or half the height(smallest one)
    let radius = Math.min(svgWidth, svgHeight) / 2 - margin

    //appened svg to div
    let svg = d3.select("#emotion-box")
        .append("svg")
            .attr("width", svgWidth)
            .attr("height", svgHeight)
        .append("g")
            .attr("transform", `translate(${svgWidth/2}, ${svgHeight/2})`);

    //set the colour scale
    let colour = d3.scaleOrdinal()
        .range(["#0000FF","#0052FF","#007AFF","#00A3FF","#00CCFF"])

    //compute poisition of each group in the chart
    let pie = d3.pie()
        .value(function(data) {return data[1];})
    let data_ready = pie(Object.entries(emotion_data))

    //generates arcs, used for adding the notation to the graph
    let arcGenerator = d3.arc()
        .innerRadius(0)
        .outerRadius(radius)

    svg
        .selectAll("slices")
        .data(data_ready)
        .join('path')
        .attr('d', d3.arc()
            .innerRadius(0)
            .outerRadius(radius)
        )
        .attr('fill', function(d){return(colour(d.data[1])) })
        .style("stroke-width", "2px")
        .style("opacity", 0.7)

    //add labels to the chart
    svg
        .selectAll("slices")
        .data(data_ready)
        .join('text')
        .text(function(data){ return(data.data[0]) })
        .attr("transform", function(data) { return `translate(${arcGenerator.centroid(data)})` })
        .style("text-anchor", "middle")
        .style("font-size", 17)
        .style("font-weight","bold")
        .style("text-transform", "uppercase")
        .style("fill", "#bec5cb")

}

emotion_graph()
