function player_count_past_one_month_compare(ids){

    let player_data = get_data_player_count_past_one_month_compare(ids)

    if(player_data.length > 0) {

        player_data.forEach(function(data, index){
            data.forEach(function(value, data_index){
                player_data[index][data_index].timestamp = new Date(value.timestamp)
            })
        })

        let highest_count = 0
        let highest_set = []
        let earliest_id = comparePlayerCountOldestDates()
        let earliest_set = []

        // find which data set has the earliest data to use for x scale values
        // find which data set has the highest player count to use for y scale values
        if(player_data.length > 1){
            player_data.forEach(function(data, index){
                data.forEach(function(value, data_index){
                    if(value.player_count > highest_count){
                        highest_count = value.player_count
                        highest_set = data
                    }
                })
                if(data[0].app_id == earliest_id){
                    earliest_set = data
                }
            })
        } else {
            player_data[0].forEach(function(value, index){
                if(value.player_count > highest_count){
                    highest_count = value.player_count
                }
            })
            highest_set = player_data[0]
            earliest_set = player_data[0]
        }
    
        $("#player-graph").empty()
    
        let margins = {top: 0, bottom: 0, left: 0, right: 0}
    
        // MARGINS
        if ($(window).width() <= 475) {
    
            margins = {top: 15, bottom: 5, left: 25, right: 0}
    
        } else {
    
            margins = {top: 15, bottom: 5, left: 50, right: 0}
    
        }
    
        let svgWidth = $('#player-graph').width() - margins.left - margins.right
        let svgHeight = 440 - margins.top - margins.bottom
    
        let chartContainer = d3
            .select('#player-graph')
            .attr('width', svgWidth + margins.left + margins.right)
            .attr('height', svgHeight + margins.top + margins.bottom);
    
    
        let x = d3.scaleTime()
            .domain(d3.extent(earliest_set, function(data) {return data.timestamp; }))
            .range([0, svgWidth])
    
        let y = d3.scaleLinear()
            .domain([0, d3.max(highest_set, function(data) {return data.player_count})])
            .range([svgHeight, 0]);
    
        let chart = chartContainer
            .append("g")
            .attr("transform", `translate(${margins.left},${margins.top})`)
    
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
                .attr("dy", "-.4em")
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
                .attr('transform', `translate(${svgWidth/2 - margins.left + 20}, ${svgHeight + 100})`)
                .attr('fill', '#bec5cb')
                .attr('font-size', 20)
                .attr('font-weight', 'bold')
                .text("Time");
        } else if ($(window).width() <= 400) {
            // X AXIS LABELS 
            chart
                .append('text')
                .attr('transform', `translate(${svgWidth/2 - margins.left}, ${svgHeight + 80})`)
                .attr('fill', '#bec5cb')
                .attr('font-size', 15)
                .attr('font-weight', 'bold')
                .text("Time");
        } else {
            // X AXIS LABELS 
            chart
                .append('text')
                .attr('transform', `translate(${svgWidth/2 - margins.left}, ${svgHeight + 80})`)
                .attr('fill', '#bec5cb')
                .attr('font-size', 20)
                .attr('font-weight', 'bold')
                .text("Time");
        }
    
    
    
        // Y AXIS TICKS
        if ($(window).width() <= 400) {
            //Y-AXIS TICKS
            chart
                .append('g')
                .call(d3.axisLeft(y).tickSizeInner(-svgWidth).tickValues(y.ticks().filter(Number.isInteger)).tickFormat(d3.format('d')))
                .attr('color', '#bec5cb')
                .attr('font-size', 12);
    
        } else {
            //Y-AXIS TICKS
            chart
                .append('g')
                .call(d3.axisLeft(y).tickSizeInner(-svgWidth).tickValues(y.ticks().filter(Number.isInteger)).tickFormat(d3.format('d')))
                .attr('color', '#bec5cb')
                .attr('font-size', 15);
        }
    
        // Y AXIS LABELS
        if ($(window).width() <= 475) {
            chartContainer
                .append('text')
                .attr('y', -12.5)
                .attr('x', -($("#player-count-container-content").height()/1.95))
                .attr("transform", "rotate(-90)")
                .attr('fill', '#bec5cb')
                .attr('font-size', 15)
                .attr('font-weight', 'bold')
                .text("Number of Players");
        } else {
            chartContainer
                .append('text')
                .attr('y', 0)
                .attr('x', -($("#player-count-container-content").height()/1.95))
                .attr("transform", "rotate(-90)")
                .attr('fill', '#bec5cb')
                .attr('font-size', 20)
                .attr('font-weight', 'bold')
                .text("Number of Players");
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
                .text("Past One Month");
        } else {
            // GRAPH TITLE
            chartContainer
                .append('text')
                .attr('y', 10)
                .attr('x', svgWidth/1.92)
                .attr('fill', '#bec5cb')
                .attr('font-size', 16)
                .attr('font-weight', 'bold')
                .text("Past One Month");
        }
    
        player_data.forEach(function(value, index){
            // ADD CHART LINE
            chart
                .append("path")
                .datum(value)
                .attr("fill", "none")
                .attr("stroke", compare_players_colours[index])
                .attr("stroke-width", 1.5)
                .attr("d", d3.line()
                    .x(function(data) {return x(data.timestamp)})
                    .y(function(data) {return y(data.player_count)})
                )
        })

        // HOVER TOOLTIP
        let bisect = d3.bisector(function(data) {return data.timestamp }).left;

        let focus_all = []

        player_data.forEach(function(value, index){
            let focus = chart.append('g').append('circle').style("fill", "none").attr("stroke", "black").attr('r', 8.5).style("opacity", 0)
            focus_all.push(focus)
        })

        // let focus = chart
        //     .append('g')
        //     .append('circle')
        //         .style("fill", "none")
        //         .attr("stroke", "black")
        //         .attr('r', 8.5)
        //         .style("opacity", 0)

        let focusText = chart
            .append('g')
            .append('text')
                .style("opacity", 0)
                .attr("text-anchor", "left")
                .attr("alignment-baseline", "middle")

        chart
            .append('rect')
            .style("fill", "none")
            .style("pointer-events", "all")
            .attr('width', svgWidth)
            .attr('height', svgHeight)
            .on('mouseover', mouseover)
            .on('mousemove', mousemove)
            .on('mouseout', mouseout)

        function mouseover() {
            focus_all.forEach(function(value, index){
                value.style("opacity", 1)
            })
            focusText.style("opacity", 1)
        }

        function mousemove(event){
            let x0 = x.invert(d3.pointer(event, this)[0]);
            let is = []
            player_data.forEach(function(value, index){
                is.push(bisect(player_data[index], x0, 0))
            })
            let i = bisect(player_data[0], x0, 0);
            selectedData = player_data[0][i]
            focus_all.forEach(function(value, index){
                value
                    .attr("cx", function(value) { 
                        let ci = is[index]
                        if(player_data[index].length < player_data[0].length){
                            return x(player_data[index][ci].timestamp) 
                        } else {
                            return x(player_data[index][ci].timestamp)
                        }
                    })
                    .attr("cy", function(value) { 
                        let ci = is[index]
                        return y(player_data[index][ci].player_count) 
                    })
            })
            focus_all.forEach(function(value, index){
                let ci = is[index]
                let width_scale = 15
                let time = new Date(player_data[index][ci].timestamp)
                time = time.getFullYear() + "/" + time.getMonth() + "/" + time.getDate();
                if(index == 0){
                    if(x(player_data[index][ci].timestamp)+15 > $("#player-graph").width()/2){
                        width_scale = -175
                    } else {
                        width_scale = 15
                    }
                    focusText
                        .attr("x", x(player_data[index][ci].timestamp)+width_scale)
                        .attr("y", y(highest_count/1.2))
                        .attr("display", "block")
                        .attr("white-space", "nowrap")
                        .attr("text-anchor", "start")
                        .html("")
                        .append('tspan')
                            .attr("white-space", "inherit")
                            .text(compare_game_data[index].name + ": " + player_data[index][ci].player_count + " (" + time + ")")
                            .attr("fill", compare_players_colours[index])
                            .style("text-shadow", "rgb(0, 0, 0) -1px -1px 0px, rgb(0, 0, 0) 1px -1px 0px, rgb(0, 0, 0) -1px 1px 0px, rgb(0, 0, 0) 1px 1px 0px");
                } else {
                    if(x(player_data[index][ci].timestamp)+15 > $("#player-graph").width()/2){
                        width_scale = -175
                    } else {
                        width_scale = 15
                    }
                    focusText
                    .append('tspan')
                        .attr("white-space", "inherit")
                        .text(compare_game_data[index].name + ": " + player_data[index][ci].player_count + " (" + time + ")")
                        .attr("fill", compare_players_colours[index])
                        .attr("x", x(player_data[index][ci].timestamp)+width_scale)
                        .attr("dy", "1.2em")
                        .style("text-shadow", "rgb(0, 0, 0) -1px -1px 0px, rgb(0, 0, 0) 1px -1px 0px, rgb(0, 0, 0) -1px 1px 0px, rgb(0, 0, 0) 1px 1px 0px");
                }
            })
        }

        function mouseout(){
            focus_all.forEach(function(value, index){
                value.style("opacity", 0)
            })
            focusText.style("opacity", 0)
        }

    } else {
        $("#player-graph").empty()
    }

}