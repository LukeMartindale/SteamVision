function get_data_emotion_past_twelve_months(id){

    let api_url = `/api/get-emotion/past-twelve-months/${id}/`

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

function emotion_past_twelve_months(id){

    let raw_data = get_data_emotion_past_twelve_months(id)

    let emotion = EmotionSection(raw_data, ["#006ee6","#CC8899","#ff683b","#6c3","#FFFF00"])
    let reviews_data = emotion.section_data

    if(emotion.status){

        $('#emotion-container-content').empty()

        //set the dimensions and margins of the graph
        let margin = 40
        let svgWidth = $('#emotion-container-content').width()
        let svgHeight = $('#emotion-container-content').height()
    
        //radius of the pieplot is half the width or half the height(smallest one)
        let radius = Math.min(svgWidth, svgHeight) / 2 - margin
    
        //appened svg to div
        let svg = d3.select("#emotion-container-content")
            .append("svg")
                .attr("width", svgWidth)
                .attr("height", svgHeight)
            .append("g")
                .attr("transform", `translate(${svgWidth/2}, ${svgHeight/2})`);
    
        //set the colour scale
        let colour = d3.scaleOrdinal()
            .range(emotion.section_colour)
    
        //compute poisition of each group in the chart
        let pie = d3.pie()
            .value(function(data) {return data[1];})
            .sort(null)
        let data_ready = pie(Object.entries(reviews_data))
    
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
            .classed('pie-part', true)
            .append('title')
            .text((data) => `Emotion: ${data.data[0]}\nEmotion Percentage: ${(data.data[1]/emotion.total * 100).toFixed(1)}%`);
    
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
            .style("text-shadow", "-1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000")
            .append('title')
            .text((data) => `Emotion: ${data.data[0]}\nEmotion Percentage: ${(data.data[1]/emotion.total * 100).toFixed(1)}%`);

    } else {
        $('#emotion-container-content').empty()
        $('#emotion-container-content').append('<div class="visualisation-container-content-no-data">No data for this timeframe!</div>')
    }



}