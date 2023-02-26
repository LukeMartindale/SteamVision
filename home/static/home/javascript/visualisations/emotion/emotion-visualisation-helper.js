function EmotionSection(data, colour){

    let section_data = {}
    let section_colour = []
    let index = 0
    let status = false
    let total = 0

    for(let [emotion, value] of Object.entries(data)){
        obj = {}
        if(value > 0){
            status = true
            section_data[emotion] = value
            section_colour.push(colour[index])
            total += value
        }
        index++
    }

    return {"section_data": section_data, "section_colour": section_colour, "status": status, "total": total}
}

function EmotionLegend(data, colour){

    $("#emotion-container-content").append('<div class="emotion-legend-container">TEST</div>')

}
