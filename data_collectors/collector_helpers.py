import datetime
from bs4 import BeautifulSoup
from home.models import Descriptor

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

def tagStripper(response):
    soup = BeautifulSoup(response.text, 'lxml')
    html = soup.find_all('div', {"class": "app_tag"})

    tags = []

    for tag in html:
        tags.append(tag.get_text())

    return tags

def newDescriptors(descriptors_genre, descriptors_tags, descriptors_categories):

    for genre in descriptors_genre:
        if not Descriptor.objects.filter(type="Genres", name=genre).exists():
            print(genre)
            desc = Descriptor()
            desc.type = "Genres"
            desc.name = genre
            desc.save()

    for tag in descriptors_tags:
        if not Descriptor.objects.filter(type="Tags", name=tag).exists():
            print(tag)
            desc = Descriptor()
            desc.type = "Tags"
            desc.name = tag
            desc.save()

    for category in descriptors_categories:
        if not Descriptor.objects.filter(type="Categories", name=category).exists():
            print(category)
            desc = Descriptor()
            desc.type = "Categories"
            desc.name = category
            desc.save()
