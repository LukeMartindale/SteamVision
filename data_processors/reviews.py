from home.models import Game, Review, GameStat
from django.utils import timezone

def reviews_all_time_year_legacy(id):

    reviews = Review.objects.filter(app_id__app_id__contains=id).order_by("time_created")
    stats = GameStat.objects.get(app_id__app_id__contains=id)

    years = [y.year for y in Review.objects.filter(app_id__app_id__contains=id).dates('time_created', 'year')]
    # months = [m.month for m in Review.objects.filter(app_id__app_id__contains=id).dates('time_created', 'month')]

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

    print(reviews[0])

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
    print("all")
    games = Game.objects.all()

    for game in games:

        print(game)
        
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
