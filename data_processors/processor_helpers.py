import re

def split_list(list, end_range, start_range):
    split = list[start_range:end_range]
    return split

def calc_sentiment_score_from_data(sentiment_data):
    pos_labels = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1"]
    neg_labels = ["-0.1", "-0.2", "-0.3", "-0.4", "-0.5", "-0.6", "-0.7", "-0.8", "-0.9", "-1"]

    pos_total = 0
    neg_total = 0
    neu_total = 0

    # Calculate each total for type of sentiment
    for sentiment in sentiment_data:
        if sentiment["label"] in pos_labels:
            pos_total += sentiment["value"]
        if sentiment["label"] in neg_labels:
            neg_total += sentiment["value"]
        if sentiment["label"] == "0":
            neu_total += sentiment["value"]

    net_total = pos_total - neg_total
    sub_total = pos_total + neg_total + neu_total

    # Check is not zero so dont try to divide by zero
    if sub_total > 0:
        net_percent = round(net_total / sub_total, 3)
    else:
        net_percent = 0

    return net_percent

def sentiment_past_time_calc(sentiment_data):

    sentiment_calc = [
        {"label": "-1","value": 0},
        {"label": "-0.9","value": 0},
        {"label": "-0.8","value": 0},
        {"label": "-0.7","value": 0},
        {"label": "-0.6","value": 0},
        {"label": "-0.5","value": 0},
        {"label": "-0.4","value": 0},
        {"label": "-0.3","value": 0},
        {"label": "-0.2","value": 0},
        {"label": "-0.1","value": 0},
        {"label": "0","value": 0},
        {"label": "0.1","value": 0},
        {"label": "0.2", "value": 0},
        {"label": "0.3","value": 0},
        {"label": "0.4","value": 0},
        {"label": "0.5","value": 0},
        {"label": "0.6","value": 0},
        {"label": "0.7","value": 0},
        {"label": "0.8","value": 0},
        {"label": "0.9","value": 0},
        {"label": "1","value": 0}
    ]

    for sentiment in sentiment_calc:
        for data in sentiment_data:
            for data_sentiment in data["sentiment"]:
                if data_sentiment["label"] == sentiment["label"]:
                    sentiment["value"] += data_sentiment["value"]

    return sentiment_calc

def format_review_text(review_text):

    reviews_format = ["[list]", "[/list]", "[i]", "[/i]", "[b]", "[/b]", "[h1]", "[/h1]", "[code]", "[/code]", "[/url]", "[spoiler]", "[/spoiler]"]
    reg = "\[url=[^\]]*]"

    # Formated reviews by removing unecceseray content
    for format in reviews_format:
        formatted_text = review_text.replace(format, '')

    formatted_text = re.sub(reg, '', formatted_text)

    print("formatted")
    print(formatted_text)

    return formatted_text
