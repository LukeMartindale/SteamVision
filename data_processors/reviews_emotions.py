import text2emotion as te

def reviews_emotions(review_text):
    value = te.get_emotion(str(review_text))

    emotions = {
        "scores": value,
        "prominent": []
    }

    #Any score above 20 is considered to be a major emotion of the text
    for emotion, score in value.items():
        if score >= 0.25:
            emotions["prominent"].append(emotion)

    return emotions
