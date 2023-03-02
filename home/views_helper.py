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

    # set correct search params
    if sentiment_score == "all-sentiment":
        sentiment_filter = {"top-range": 1, "bottom-range": -1}
    elif sentiment_score == "sentiment-neutral":
        sentiment_filter = {"top-range": 0, "bottom-range": 0}
    elif sentiment_score == "sentiment-positive":
        sentiment_filter = {"top-range": 1, "bottom-range": 0.00000000000000000000000001}
    elif sentiment_score == "sentiment-negative":
        sentiment_filter = {"top-range": -0.00000000000000000000000001, "bottom-range": -1}

    return sentiment_filter
