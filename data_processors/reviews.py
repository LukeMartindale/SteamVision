from home.models import Game, Review, GameStat
from django.utils import timezone
import datetime
import calendar

def reviews_all_time_year_legacy(id):

    reviews = Review.objects.filter(app_id__app_id__contains=id).order_by("time_created")
    stats = GameStat.objects.get(app_id__app_id__contains=id)

    years = [y.year for y in Review.objects.filter(app_id__app_id__contains=id).dates('time_created', 'year')]

    reviews_percentages = []

    for year in years:

        pos_counter = 0
        neg_counter = 0

        for review in reviews:
            if(review.time_created.year == year):
                if(review.voted_up):
                    pos_counter += 1
                else:
                    neg_counter += 1

        num_of_reviews = pos_counter + neg_counter
        reviews_percentages.append({'label': year, 'percentage': round(pos_counter / num_of_reviews * 100, 1), 'number_of_reviews': num_of_reviews})

    stats.reviews_all_time_year = reviews_percentages
    stats.save()

def reviews_all_time_year_legacy_all():

    games = Game.objects.all()

    for game in games:
        reviews = Review.objects.filter(app_id=game).order_by("time_created")
        stats = GameStat.objects.get(app_id=game)

        years = [y.year for y in Review.objects.filter(app_id=game).dates('time_created', 'year')]

        reviews_percentages = []

        for year in years:

            pos_counter = 0
            neg_counter = 0

            for review in reviews:
                if(review.time_created.year == year):
                    if(review.voted_up):
                        pos_counter += 1
                    else:
                        neg_counter += 1

            num_of_reviews = pos_counter + neg_counter
            reviews_percentages.append({'label': year, 'percentage': round(pos_counter / num_of_reviews * 100, 1), 'number_of_reviews': num_of_reviews})

        stats.reviews_all_time_year = reviews_percentages
        stats.save()

def reviews_all_time_year(id):

    game = Game.objects.get(app_id=id)

    year = timezone.now().year
    reviews = Review.objects.filter(app_id=game, time_created__year=year).order_by("time_created")
    stats = GameStat.objects.get(app_id=game)

    pos_counter = 0
    neg_counter = 0

    for review in reviews:
        if(review.time_created.year == year):
            if(review.voted_up):
                pos_counter += 1
            else:
                neg_counter += 1

    num_of_reviews = pos_counter + neg_counter

    found = False

    for stat in stats.reviews_all_time_year:
        if stat["label"] == year:
            stat["percentage"] = round(pos_counter / num_of_reviews * 100, 1)
            stat["number_of_reviews"] = num_of_reviews
            found = True

    if not found:
        stats.reviews_all_time_year.append({'label': year, 'percentage': round(pos_counter / num_of_reviews * 100, 1), 'number_of_reviews': num_of_reviews})

    stats.save()

def reviews_all_time_year_all():

    games = Game.objects.all()

    for game in games:
        
        reviews = Review.objects.filter(app_id=game).order_by("time_created")
        stats = GameStat.objects.get(app_id=game)

        print(reviews)

        year = timezone.now().year

        pos_counter = 0
        neg_counter = 0

        for review in reviews:
            if(review.time_created.year == year):
                if(review.voted_up):
                    pos_counter += 1
                else:
                    neg_counter += 1

        num_of_reviews = pos_counter + neg_counter

        for stat in stats.reviews_all_time_year:
            if stat["label"] == year:
                if num_of_reviews > 0:
                    percentage = round(pos_counter / num_of_reviews * 100, 1)
                else:
                    percentage = 0.0
                stat["percentage"] = percentage
                stat["number_of_reviews"] = num_of_reviews

        stats.save()

def reviews_all_time_month_legacy(id):

    stats = GameStat.objects.get(app_id__app_id__contains=id)
    years = [y.year for y in Review.objects.filter(app_id__app_id__contains=id).dates('time_created', 'year')]

    reviews_percentages = []
    
    for index, year in enumerate(years):

        for i in range(1 ,13):

            reviews = Review.objects.filter(app_id__app_id__contains=id, time_created__year=year, time_created__month=i).order_by("time_created")

            num_of_reviews = len(reviews)

            pos_counter = 0
            neg_counter = 0

            for review in reviews:
                if(review.voted_up):
                    pos_counter += 1
                else:
                    neg_counter += 1

            if not num_of_reviews:
                percentage = 0.0
            else:
                percentage = round(pos_counter / num_of_reviews * 100, 1)

            label = str(year) + " " + str(calendar.month_name[i])

            reviews_percentages.append({'label': label, 'year': year, 'month': calendar.month_name[i], 'percentage': percentage, 'number_of_reviews': num_of_reviews})

    stats.reviews_all_time_month = reviews_percentages
    stats.save()

def reviews_all_time_month_legacy_all():

    games = Game.objects.all()

    for game in games:

        stats = GameStat.objects.get(app_id=game)
        years = [y.year for y in Review.objects.filter(app_id=game).dates('time_created', 'year')]

        reviews_percentages = []
        
        for index, year in enumerate(years):

            for i in range(1 ,13):

                reviews = Review.objects.filter(app_id=game, time_created__year=year, time_created__month=i).order_by("time_created")

                num_of_reviews = len(reviews)

                pos_counter = 0
                neg_counter = 0

                for review in reviews:
                    if(review.voted_up):
                        pos_counter += 1
                    else:
                        neg_counter += 1

                if not num_of_reviews:
                    percentage = 0.0
                else:
                    percentage = round(pos_counter / num_of_reviews * 100, 1)

                label = str(year) + " " + str(calendar.month_name[i])

                reviews_percentages.append({'label': label, 'year': year, 'month': calendar.month_name[i], 'percentage': percentage, 'number_of_reviews': num_of_reviews})

        stats.reviews_all_time_month = reviews_percentages
        stats.save()

def reviews_all_time_month(id):

    stats = GameStat.objects.get(app_id__app_id__contains=id)

    year = timezone.now().year
    month = timezone.now().month

    reviews = Review.objects.filter(app_id__app_id__contains=id, time_created__year=year, time_created__month=month).order_by("time_created")
    
    pos_counter = 0
    neg_counter = 0

    for review in reviews:
        if(review.time_created.year == year):
            if(review.voted_up):
                pos_counter += 1
            else:
                neg_counter += 1

    num_of_reviews = len(reviews)
    found = False

    for stat in stats.reviews_all_time_month:
        if stat["year"] == year and stat["month"] == calendar.month_name[month]:
            if num_of_reviews:
                stat["percentage"] = round(pos_counter / num_of_reviews * 100, 1)
            else:
                stat["percentage"] = 0.0
            stat["number_of_reviews"] = num_of_reviews
            found = True

    label = str(year) + " " + str(calendar.month_name[month])

    if not found:
        if num_of_reviews:
            stats.reviews_all_time_month.append({'label': label, 'year': year, 'month': calendar.month_name[month], 'percentage': round(pos_counter / num_of_reviews * 100, 1), 'number_of_reviews': num_of_reviews})
        else:
            stats.reviews_all_time_month.append({'label': label, 'year': year, 'month': calendar.month_name[month], 'percentage': 0.0, 'number_of_reviews': num_of_reviews})

    stats.save()

def reviews_all_time_month_all():

    games = Game.objects.all()

    year = timezone.now().year
    month = timezone.now().month

    for game in games:

        stats = GameStat.objects.get(app_id=game)

        reviews = Review.objects.filter(app_id=game, time_created__year=year, time_created__month=month).order_by("time_created")
        
        pos_counter = 0
        neg_counter = 0

        for review in reviews:
            if(review.time_created.year == year):
                if(review.voted_up):
                    pos_counter += 1
                else:
                    neg_counter += 1

        num_of_reviews = len(reviews)
        found = False

        for stat in stats.reviews_all_time_month:
            if stat["year"] == year and stat["month"] == calendar.month_name[month]:
                if num_of_reviews:
                    stat["percentage"] = round(pos_counter / num_of_reviews * 100, 1)
                else:
                    stat["percentage"] = 0.0
                stat["number_of_reviews"] = num_of_reviews
                found = True

        label = str(year) + " " + str(calendar.month_name[month])

        if not found:
            if num_of_reviews:
                stats.reviews_all_time_month.append({'label': label, 'year': year, 'month': calendar.month_name[month], 'percentage': round(pos_counter / num_of_reviews * 100, 1), 'number_of_reviews': num_of_reviews})
            else:
                stats.reviews_all_time_month.append({'label': label, 'year': year, 'month': calendar.month_name[month], 'percentage': 0.0, 'number_of_reviews': num_of_reviews})

        stats.save()

def reviews_past_month(id):
    stat = GameStat.objects.get(app_id__app_id__contains=id)
    reviews = Review.objects.filter(app_id__app_id__contains=id).order_by('time_created')

    dates = []
    reviews_percentages = []

    # Get all dates from the last 30 days
    for i in range(1, 31):
        dates.append(datetime.datetime.now() - datetime.timedelta(days=i))

    for date in dates:

        pos_counter = 0
        neg_counter = 0
        num_of_reviews = 0

        for review in reviews:
            if review.time_created.year == date.year and review.time_created.month == date.month and review.time_created.day == date.day:
                num_of_reviews += 1
                if review.voted_up:
                    pos_counter += 1
                else:
                    neg_counter += 1

        if num_of_reviews:
            percentage = round(pos_counter / num_of_reviews * 100, 1)
        else:
            percentage = 0.0

        label = str(date.year) + " " + str(calendar.month_name[date.month] + " " + str(date.day))

        reviews_percentages.append({'label': label, 'year': date.year, 'month': date.month, 'day': date.day, 'percentage': percentage, 'number_of_reviews': num_of_reviews})

    stat.reviews_past_one_month = reviews_percentages
    stat.save()

def reviews_past_month_all():
    games = Game.objects.all()

    for game in games:
        stat = GameStat.objects.get(app_id=game)
        reviews = Review.objects.filter(app_id=game).order_by('time_created')

        dates = []
        reviews_percentages = []

        # Get all dates from the last 30 days
        for i in range(1, 31):
            dates.append(datetime.datetime.now() - datetime.timedelta(days=i))

        for date in dates:

            pos_counter = 0
            neg_counter = 0
            num_of_reviews = 0

            for review in reviews:
                if review.time_created.year == date.year and review.time_created.month == date.month and review.time_created.day == date.day:
                    num_of_reviews += 1
                    if review.voted_up:
                        pos_counter += 1
                    else:
                        neg_counter += 1

            if num_of_reviews:
                percentage = round(pos_counter / num_of_reviews * 100, 1)
            else:
                percentage = 0.0

            label = str(date.year) + " " + str(calendar.month_name[date.month] + " " + str(date.day))

            reviews_percentages.append({'label': label, 'year': date.year, 'month': date.month, 'day': date.day, 'percentage': percentage, 'number_of_reviews': num_of_reviews})

        stat.reviews_past_one_month = reviews_percentages
        stat.save()
