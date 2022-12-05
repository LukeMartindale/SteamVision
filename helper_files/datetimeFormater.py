import datetime

dates = {
    "Jan": '1',
    "Feb": '2',
    "Mar": '3',
    "Apr": '4',
    "May": '5',
    "Jun": '6',
    "Jul": '7',
    "Aug": '8',
    "Sep": '9',
    "Oct": '10',
    "Nov": '11',
    "Dec": '12'
}

def convertDate(string_date):

    split = string_date.split(" ")
    split[1] = dates[split[1].replace(',', '')]

    date_time = datetime.datetime(int(split[2]), int(split[1]), int(split[0]))

    return date_time
