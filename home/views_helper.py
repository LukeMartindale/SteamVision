def reviews_score_search_filter_value(review_score):

    review_filter = [True, False]

    # set correct search params
    if review_score == "all-reviews":
        review_filter = [True, False]
    elif review_score == "positive-reviews":
        review_filter = [True]
    elif review_score == "negative-reviews":
        review_filter = [False]

    return review_filter

def sentiment_score_search_filter_value(sentiment_score):

    sentiment_filter = {"top-range": 1, "bottom-range": -1}

    if sentiment_score == "all-sentiment":
        # ALL
        sentiment_filter = {"top-range": 1, "bottom-range": -1}
    elif sentiment_score == "sentiment-positive":
        # POS
        sentiment_filter = {"top-range": 1, "bottom-range": 0.05000000000000001}
    elif sentiment_score == "sentiment-negative":
        # NEG
        sentiment_filter = {"top-range": -0.05000000000000001, "bottom-range": -1}
    elif sentiment_score == "sentiment-neutral":
        # NEU
        sentiment_filter = {"top-range": 0.04999999999999999, "bottom-range": -0.05000000000000000}
    elif sentiment_score == "positive-high":
        # POS HIGH
        sentiment_filter = {"top-range": 1, "bottom-range": 0.75000000000000000}
    elif sentiment_score == "positive-mid":
        # POS MID
        sentiment_filter = {"top-range": 0.74999999999999999, "bottom-range": 0.45000000000000000}
    elif sentiment_score == "positive-low":
        # POS LOW
        sentiment_filter = {"top-range": 0.44999999999999999, "bottom-range": 0.05000000000000000}
    elif sentiment_score == "negative-high":
        # NEG HIGH
        sentiment_filter = {"top-range": -0.75000000000000001, "bottom-range": -1}
    elif sentiment_score == "negative-mid":
        # NEG MID
        sentiment_filter = {"top-range": -0.45000000000000001, "bottom-range": -0.74999999999999999}
    elif sentiment_score == "negative-low":
        # NEG LOW
        sentiment_filter = {"top-range": -0.05000000000000001, "bottom-range": -0.44999999999999999}

    return sentiment_filter

def emotion_prominent_search_filter_value(prominent_emotion):

    emotions = ""

    if prominent_emotion == "all-emotions":
        emotions = ""
    elif prominent_emotion == "emotion-happy":
        emotions = "happy"
    elif prominent_emotion == "emotion-angry":
        emotions = "angry"
    elif prominent_emotion == "emotion-surprise":
        emotions = "surprise"
    elif prominent_emotion == "emotion-sad":
        emotions = "sad"
    elif prominent_emotion == "emotion-fear":
        emotions = "angry"

    print(prominent_emotion)

    return emotions
