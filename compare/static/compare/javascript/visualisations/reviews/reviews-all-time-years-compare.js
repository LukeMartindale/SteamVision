function reviews_all_time_year_compare(ids) {

    let reviews_data = get_data_reviews_all_time_compare(ids)

    console.log(reviews_data)

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
            .select('#sentiment-graph')
            .attr('width', svgWidth + margins.left + margins.right)
            .attr('height', svgHeight + margins.top + margins.bottom);


        let chart = chartContainer
            .append('g')
            .attr("transform", `translate(${margins.left},${margins.top})`);

    } else {
        $('#reviews-graph').empty()
    }

}