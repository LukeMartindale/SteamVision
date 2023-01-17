import datetime

def convertDate(string_date):

    dates = {"Jan": '1',"Feb": '2',"Mar": '3',"Apr": '4', "May": '5',"Jun": '6',
        "Jul": '7',"Aug": '8',"Sep": '9',"Oct": '10',"Nov": '11',"Dec": '12'}

    split = string_date.split(" ")
    split[1] = dates[split[1].replace(',', '')]

    date_time = datetime.datetime(int(split[2]), int(split[1]), int(split[0]))
    return date_time

def descriptionStripper(items):
    descriptions = []
    for item in items:
        descriptions.append(item['description'])
    return descriptions
