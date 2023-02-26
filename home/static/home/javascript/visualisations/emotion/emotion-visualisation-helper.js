function EmotionSection(data, colour){

    let section_data = {}
    let section_colour = []
    let index = 0
    let status = false

    for(let [emotion, value] of Object.entries(data)){
        obj = {}
        if(value > 0){
            status = true
            section_data[emotion] = value
            section_colour.push(colour[index])
        }
        index++
    }

    return {"section_data": section_data, "section_colour": section_colour, "status": status}
}


function noEmotionForFilter(data){
    return "Not Yet Implemented"
}
