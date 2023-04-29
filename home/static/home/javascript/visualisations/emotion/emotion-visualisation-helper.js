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

function ProminentEmotionPlacer(emotion_data){

    let emotions_base = ["Happy", "Angry", "Surprise", "Sad", "Fear"]
    let total_emotion = 0
    let prominent = []

    let emotion_widget = $("#emotion-prominent-info")

    emotion_widget.empty()

    // $("#emotion-prominent-info").append('<div class="emotion-legend-container">TEST</div>')

    emotions_base.forEach(function(value, index){
        total_emotion += emotion_data[value]
    })

    if(total_emotion > 0){

        // Get the prominent emotions, prominent emotions are those with a percentage of 20% or higher
        emotions_base.forEach(function(value, index){
            // Get the prominent emotions
            if(emotion_data[value] / total_emotion >= 0.15){
                prominent.push(value)
            }
        })

        prominent.forEach(function(value, index){

            if(value == "Happy"){
                // Happy
                emotion_widget.append('<div class="emotion-icon-small-wrapper" id="top-emotion-icon-happy"></div>')
                emotion_widget.find("#top-emotion-icon-happy").append('<i class="bi bi-emoji-smile-fill emotion-small-icon emotion-happy" title="Happy"></i>')
            } else if (value == "Angry") {
                // Angry
                emotion_widget.append('<div class="emotion-icon-small-wrapper" id="top-emotion-icon-angry"></div>')
                emotion_widget.find("#top-emotion-icon-angry").append('<i class="bi bi-emoji-angry-fill emotion-small-icon emotion-angry" title="Angry"></i>')
            } else if (value == "Surprise") {
                // laughing
                emotion_widget.append('<div class="emotion-icon-small-wrapper" id="top-emotion-icon-surprise"></div>')
                emotion_widget.find("#top-emotion-icon-surprise").append('<i class="bi bi-emoji-laughing-fill emotion-small-icon emotion-surprise" title="Surprise"></i>')
            } else if (value == "Sad") {
                // unhappy
                emotion_widget.append('<div class="emotion-icon-small-wrapper" id="top-emotion-icon-sad"></div>')
                emotion_widget.find("#top-emotion-icon-sad").append('<i class="bi bi-emoji-frown-fill emotion-small-icon emotion-sad" title="Sad"></i>')
            } else if (value == "Fear") {
                // dizzy
                emotion_widget.append('<div class="emotion-icon-small-wrapper" id="top-emotion-icon-fear"></div>')
                emotion_widget.find("#top-emotion-icon-fear").append('<i class="bi bi-emoji-dizzy-fill emotion-small-icon emotion-fear" title="Fear"></i>')
            }

        })

    } else {
        console.log("Not Yet Implemented")
        // Put a message that states no promient emotions found
    }

}
