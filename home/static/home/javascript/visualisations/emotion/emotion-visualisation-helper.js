function EmotionSection(data, colour){

    let section_data = {}
    let section_colour = []
    let index = 0

    for(let [emotion, value] of Object.entries(data)){
        obj = {}
        if(value > 0){
            section_data[emotion] = value
            section_colour.push(colour[index])
        }
        index++
    }

    return {"section_data": section_data, "section_colour": section_colour}
}


function noEmotionForFilter(data){
    return "Not Yet Implemented"
}
