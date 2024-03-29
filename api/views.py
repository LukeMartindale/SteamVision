from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import (
    GameSerializer, 
    GameReviewSerializer, 
    GameStatSerializer, 
    DescriptorSerializer, 
    PlayerCountSerializer,
    )
from home.models import (
    Game, 
    GameStat, 
    Review, 
    Descriptor, 
    PlayerCount,
    )
from users.models import (
    Profile
)
from data_processors.processor_helpers import sentiment_past_time_calc
from django.utils import timezone
import datetime
import calendar

from django.db.models import Max, Avg

# Base route for eash of use
@api_view(['GET'])
def base(request):
    return Response({"message": "Base Route"})

# Get a single game by its app_id / pk
@api_view(['GET'])
def getGame(request, id):

    try:
        game = Game.objects.filter(pk=id)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = GameSerializer(game, many=True)

    return Response(serializer.data)

# get all games in the database
@api_view(['GET'])
def getAllGames(request):
    game = Game.objects.all()
    serializer = GameSerializer(game, many=True)
    return Response(serializer.data)

# Get a single game stat object by its app_id / pk of the game
@api_view(['GET'])
def getGameStats(request, id):
    game_stats = GameStat.objects.filter(app_id__app_id=id)
    serializer = GameStatSerializer(game_stats, many=True)

    return Response(serializer.data)

# Get a list of games which match the search arguments
@api_view(['GET'])
def getGameSearch(request, search):

    print(search)
    games = Game.objects.filter(name__icontains=search)
    print(games)
    serializer = GameSerializer(games, many=True)

    return Response({"games": serializer.data})

# Get the all time year reviews data form game stat object by its app_id / pk of the game
@api_view(['GET'])
def getReviewsAllTimeYear(request, id):
    stat = GameStat.objects.get(app_id__app_id=id)
    
    return Response(stat.reviews_all_time_year)

@api_view(['GET'])
def getReviewsAllTimeMonth(request, id):
    stat = GameStat.objects.get(app_id__app_id=id)

    return Response(stat.reviews_all_time_month)

@api_view(['GET'])
def getReviewsPastTwelveMonths(request, id):
    stats = GameStat.objects.get(app_id__app_id=id)

    time = timezone.now()
    end_index = 0

    for index, stat in enumerate(stats.reviews_all_time_month):
        if(stat["year"] == time.year and stat["month"] == calendar.month_name[time.month]):
            end_index = index+1
            break

    start_index = end_index - 12
    past_twelve_months = []

    for stat in reversed(stats.reviews_all_time_month[start_index:end_index]):
        past_twelve_months.append(stat)

    return Response(reversed(past_twelve_months))

@api_view(['GET'])
def getReviewsPastSixMonths(request, id):
    stats = GameStat.objects.get(app_id__app_id=id)

    time = timezone.now()
    end_index = 0

    for index, stat in enumerate(stats.reviews_all_time_month):
        if(stat["year"] == time.year and stat["month"] == calendar.month_name[time.month]):
            end_index = index+1
            break

    start_index = end_index - 6
    past_twelve_months = []

    for stat in reversed(stats.reviews_all_time_month[start_index:end_index]):
        past_twelve_months.append(stat)

    return Response(reversed(past_twelve_months))

@api_view(['GET'])
def getReviewsPastOneMonth(request, id):
    stat = GameStat.objects.get(app_id__app_id=id)
    
    return Response(reversed(stat.reviews_past_one_month))

@api_view(['GET'])
def getReviewsPastTwoWeeks(request, id):
    stat = GameStat.objects.get(app_id__app_id=id)
    reviews_percentages = []

    # Get all dates from the last 30 days
    for i in range(0, 14):
        reviews_percentages.append(stat.reviews_past_one_month[i])

    return Response(reversed(reviews_percentages))

@api_view(['GET'])
def getReviewsPastOneWeek(request, id):
    stat = GameStat.objects.get(app_id__app_id=id)
    reviews_percentages = []

    # Get all dates from the last 30 days
    for i in range(0, 7):
        reviews_percentages.append(stat.reviews_past_one_month[i])

    return Response(reversed(reviews_percentages))

@api_view(['GET'])
def getSentimentAllTime(request, id):
    stat = GameStat.objects.get(app_id__app_id=id)

    return Response(stat.sentiment_all_time)

@api_view(['GET'])
def getSentimentAllTimeMonth(request, id):
    stat = GameStat.objects.get(app_id__app_id=id)

    return Response(stat.sentiment_all_time_month)

@api_view(['GET'])
def getSentimentPastTwelveMonths(request, id):
    stats = GameStat.objects.get(app_id__app_id=id)

    time = timezone.now()
    end_index = 0

    for index, stat in enumerate(stats.sentiment_all_time_month):
        if(stat["year"] == time.year and stat["month"] == calendar.month_name[time.month]):
            end_index = index+1
            break

    start_index = end_index - 12
    past_twelve_months = []

    for stat in reversed(stats.sentiment_all_time_month[start_index:end_index]):
        past_twelve_months.append(stat)

    past_twelve_months_calced = sentiment_past_time_calc(past_twelve_months)

    return Response(past_twelve_months_calced)

@api_view(['GET'])
def getSentimentPastSixMonths(request, id):
    stats = GameStat.objects.get(app_id__app_id=id)

    time = timezone.now()
    end_index = 0

    for index, stat in enumerate(stats.sentiment_all_time_month):
        if(stat["year"] == time.year and stat["month"] == calendar.month_name[time.month]):
            end_index = index+1
            break

    start_index = end_index - 6
    past_six_months = []

    for stat in reversed(stats.sentiment_all_time_month[start_index:end_index]):
        past_six_months.append(stat)

    past_six_months_calced = sentiment_past_time_calc(past_six_months)

    return Response(past_six_months_calced)

@api_view(['GET'])
def getSentimentPastOneMonth(request, id):
    stats = GameStat.objects.get(app_id__app_id=id)

    return Response(stats.sentiment_past_one_month)

@api_view(['GET'])
def getSentimentPastTwoWeeks(request, id):
    stats = GameStat.objects.get(app_id__app_id=id)

    return Response(stats.sentiment_past_two_weeks)

@api_view(['GET'])
def getSentimentPastOneWeek(request, id):
    stats = GameStat.objects.get(app_id__app_id=id)

    return Response(stats.sentiment_past_one_week)

@api_view(['GET'])
def getEmotionAllTime(request, id):
    stat = GameStat.objects.get(app_id__app_id=id)

    return Response(stat.emotion_all_time)

@api_view(['GET'])
def getEmotionAllTimeMonth(request, id):
    stat = GameStat.objects.get(app_id__app_id=id)

    return Response(stat.emotion_all_time_month)

@api_view(['GET'])
def getEmotionPastTwelveMonths(request, id):
    stats = GameStat.objects.get(app_id__app_id=id)

    time = timezone.now()
    end_index = 0

    for index, stat in enumerate(stats.emotion_all_time_month):
        if(stat["year"] == time.year and stat["month"] == calendar.month_name[time.month]):
            end_index = index+1
            break

    start_index = end_index - 12
    past_twelve_months = []

    for stat in reversed(stats.emotion_all_time_month[start_index:end_index]):
        past_twelve_months.append(stat)

    emotions = {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}
    for past in past_twelve_months:
        for emotion, score in emotions.items():
            emotions[emotion] += past["emotion"][emotion]
        
    return Response(emotions)

@api_view(['GET'])
def getEmotionPastSixMonths(request, id):
    stats = GameStat.objects.get(app_id__app_id=id)

    time = timezone.now()
    end_index = 0

    for index, stat in enumerate(stats.emotion_all_time_month):
        if(stat["year"] == time.year and stat["month"] == calendar.month_name[time.month]):
            end_index = index+1
            break

    start_index = end_index - 6
    past_twelve_months = []

    for stat in reversed(stats.emotion_all_time_month[start_index:end_index]):
        past_twelve_months.append(stat)

    emotions = {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}
    for past in past_twelve_months:
        for emotion, score in emotions.items():
            emotions[emotion] += past["emotion"][emotion]
        
    return Response(emotions)

@api_view(['GET'])
def getEmotionPastOneMonth(request, id):
    stats = GameStat.objects.get(app_id__app_id=id)

    return Response(stats.emotion_past_one_month)

@api_view(['GET'])
def getEmotionPastTwoWeeks(request, id):
    stats = GameStat.objects.get(app_id__app_id=id)

    return Response(stats.emotion_past_two_weeks)

@api_view(['GET'])
def getEmotionPastOneWeek(request, id):
    stats = GameStat.objects.get(app_id__app_id=id)

    return Response(stats.emotion_past_one_week)

@api_view(['GET'])
def getDescriptors(request):
    descriptors = Descriptor.objects.all()
    serializer = DescriptorSerializer(descriptors, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getGenres(request):
    genres = Descriptor.objects.filter(type="Genres")
    serializer = DescriptorSerializer(genres, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getTags(request):
    tags = Descriptor.objects.filter(type="Tags")
    serializer = DescriptorSerializer(tags, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getCategories(request):
    categories = Descriptor.objects.filter(type="Categories")
    serializer = DescriptorSerializer(categories, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getPlayerAllTime(request, id):
    player_count = PlayerCount.objects.filter(app_id__app_id=id).order_by("timestamp")
    serialiser = PlayerCountSerializer(player_count, many=True)

    return Response(serialiser.data)

@api_view(['GET'])
def getPlayerCountPastOneMonth(request, id):
    start_date = timezone.now() + timezone.timedelta(days=-30)
    end_date = timezone.now()

    player_count = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[start_date, end_date])
    serializer = PlayerCountSerializer(player_count, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getPlayerCountPastTwoWeeks(request, id):
    start_date = timezone.now() + timezone.timedelta(days=-14)
    end_date = timezone.now()

    player_count = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[start_date, end_date])
    serializer = PlayerCountSerializer(player_count, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getPlayerCountPastOneWeek(request, id):
    start_date = timezone.now() + timezone.timedelta(days=-7)
    end_date = timezone.now()

    player_count = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[start_date, end_date])
    serializer = PlayerCountSerializer(player_count, many=True)

    return Response(serializer.data)  

@api_view(['GET'])
def getPlayerCountPast72Hours(request, id):
    start_time = timezone.now() - timezone.timedelta(hours=73)
    end_time = timezone.now()

    player_count = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[start_time, end_time])
    serializer = PlayerCountSerializer(player_count, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getPlayerCountPast48Hours(request, id):
    start_time = timezone.now() - timezone.timedelta(hours=49)
    end_time = timezone.now()

    player_count = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[start_time, end_time])
    serializer = PlayerCountSerializer(player_count, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getPlayerCountPast24Hours(request, id):
    start_time = timezone.now() - timezone.timedelta(hours=25)
    end_time = timezone.now()

    player_count = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[start_time, end_time])
    serializer = PlayerCountSerializer(player_count, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getPlayerCountCurrent(request):
    games = Game.objects.all()

    # Get List of current most played games
    players_current = []
    for game in games:

        current = {}
        player_count = PlayerCount.objects.filter(app_id=game).last()
        serializer = GameSerializer(game)

        current["app"] = serializer.data
        current["player_count"] = player_count.player_count
        players_current.append(current)

    players_current = sorted(players_current, key=lambda x:x['player_count'], reverse=True)

    return Response(players_current)

@api_view(['GET'])
def getReviewPercentageCurrent(request):
    games = Game.objects.all()

    reviews_current = []
    for game in games:

        current = {}
        review_percentage = GameStat.objects.get(app_id=game).current_review_score
        serializer = GameSerializer(game)

        current["app"] = serializer.data
        current["reviews_percentage"] = review_percentage
        reviews_current.append(current)

    reviews_current = sorted(reviews_current, key=lambda x:x['reviews_percentage'], reverse=True)

    return Response(reviews_current)

@api_view(['GET'])
def userFollowGame(request, id):

    # check if user is logged in
    if(request.user.is_anonymous):
        # User is not logged in
        return Response({"follow_status": "not applicable", "code": "0"})
    else:
        # Check that game exists
        if Game.objects.filter(app_id=id).exists():
            # Get user profile
            profile = Profile.objects.get(user=request.user)

            # Create dictionary object
            followed_entry = dict()
            # check if followed game is empty or not
            if profile.followed_games == {}:
                followed_list = []
            else:
                followed_list = profile.followed_games
            # Check if game already being followed
            if not any (d.get('app_id', 'default') == id for d in followed_list):
                # Set app_id in followed_entry
                followed_entry["app_id"] = id
                # Get current date/time and set in followed_entry
                followed_entry["date_and_time"] = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
                # Figure out followed rank should be
                followed_entry["rank"] = len(followed_list) + 1
                # add game to followed games list
                followed_list.append(followed_entry)
                # set profile followed game to file_list
                profile.followed_games = followed_list
                # Save profile
                profile.save()
                return Response({"message": "Game successfully followed"})
            else:
                return Response({"message": "User is already following this game"})
        else:
            return Response({"message": "This game does not exist"})

@api_view(['GET'])
def userUnfollowGame(request, id):

    # check if user is logged in
    if(request.user.is_anonymous):
        # User is not logged in
        return Response({"message": "Not Logged In"})
    else:
        # Get user profile
        profile = Profile.objects.get(user=request.user)
        # Check that game is being followed
        if any (d.get('app_id', 'default') == id for d in profile.followed_games):
            # get rank of removed game
            removed_rank = next((x for x in profile.followed_games if (x["app_id"]) == id), None)
            if removed_rank: removed_rank = removed_rank["rank"]
            # remove game from followed list
            new_list = [i for i in profile.followed_games if not (i["app_id"] == id)]
            # update game ranks
            for item in new_list:
                if item["rank"] > removed_rank: item["rank"]-=1
            # set profile followed games to new list
            profile.followed_games = new_list
            # save profile
            profile.save()
            return Response({"message": "Game successfully unfollowed"})
        else:
            return Response({"message": "This game is not being followed"})

@api_view(['GET'])
def userGetFollowedGames(request):
    # check if user is logged in
    if(request.user.is_anonymous):
        # User is not logged in
        return Response({"message": "user is not logged in", "games": []})
    else:
        # Get user profile
        profile = Profile.objects.get(user__username=request.user)
        game_ids = [i["app_id"] for i in profile.followed_games]
        # Get game objects
        followed_games = Game.objects.filter(app_id__in=game_ids)
        # serialize followed games
        serializer = GameSerializer(followed_games, many=True)
        # Return followed games list
        return Response({"message": "Followed games list retrieved", "games": serializer.data})

@api_view(['GET'])
def userCheckFollowingGame(request, id):

    # check if user is logged in
    if(request.user.is_anonymous):
        # User is not logged in
        return Response({"follow_status": "not applicable", "code": "0"})
    else:
        profile = Profile.objects.get(user=request.user)
        # check if user is following game
        if any (d.get('app_id', 'default') == id for d in profile.followed_games):
            # user is following game
            return Response({"follow_status": "following", "code": "1"})
        else:
            # user is not following game
            return Response({"follow_status": "not following", "code": "2"})
    
@api_view(['GET'])
def gameDetailReviewsStats(request, id):

    game = Game.objects.get(app_id=id)

    game_stats = GameStat.objects.get(app_id=game)

    total_reviews = len(Review.objects.filter(app_id=game))
    positive_reviews = len(Review.objects.filter(app_id=game, voted_up=True))
    negative_reviews = len(Review.objects.filter(app_id=game, voted_up=False))

    return Response({"current_review_score": game_stats.current_review_score, "total_reviews": total_reviews, "positive_reviews": positive_reviews, "negative_reviews": negative_reviews})

@api_view(['GET'])
def getVisualisationWidgetReviewData(request, id):

    game = Game.objects.get(app_id=id)
    game_stats = GameStat.objects.get(app_id=game)

    # All time
    all_time = round(game_stats.current_review_score * 100, 1)
    if game_stats.number_of_reviews > 0:
        all_time_neg = round(100 - all_time, 1)
    else:
        all_time_neg = 0.0
    # 12 months
    twelve_months_total = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(weeks=52), timezone.now()]).count()
    twelve_months_pos = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(weeks=52), timezone.now()], voted_up=True).count()
    if twelve_months_total:
        twelve_months = round(twelve_months_pos / twelve_months_total * 100, 1)
        twelve_months_neg = round(100 - twelve_months, 1)
    else:
        twelve_months = 0.0
        twelve_months_neg = 0.0
    # 6 months
    six_months_total = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(weeks=26), timezone.now()]).count()
    six_months_pos = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(weeks=26), timezone.now()], voted_up=True).count()
    if six_months_total:
        six_months = round(six_months_pos / six_months_total * 100, 1)
        six_months_neg = round(100 - six_months, 1)
    else:
        six_months = 0.0
        six_months_neg = 0.0
    # 30 days
    thirty_days_total = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(days=30), timezone.now()]).count()
    thirty_days_pos = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(days=30), timezone.now()], voted_up=True).count()
    if thirty_days_total:
        thirty_days = round(thirty_days_pos / thirty_days_total * 100, 1)
        thirty_days_neg = round(100 - thirty_days, 1)
    else:
        thirty_days = 0.0
        thirty_days_neg = 0.0
    # 2 weeks
    two_weeks_total = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(days=14), timezone.now()]).count()
    two_weeks_pos = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(days=14), timezone.now()], voted_up=True).count()
    if two_weeks_total:
        two_weeks = round(two_weeks_pos / two_weeks_total * 100, 1)
        two_weeks_neg = round(100 - two_weeks, 1)
    else:
        two_weeks = 0.0
        two_weeks_neg = 0.0
    # 1 week
    one_week_total = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(days=7), timezone.now()]).count()
    one_week_pos = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(days=7), timezone.now()], voted_up=True).count()
    if one_week_total:
        one_week = round(one_week_pos / one_week_total * 100, 1)
        one_week_neg = round(100 - one_week, 1)
    else:
        one_week = 0.0
        one_week_neg = 0.0

    return Response({"all_time": all_time, "all_time_neg": all_time_neg, "twelve_months": twelve_months, "twelve_months_neg": twelve_months_neg, "six_months": six_months, "six_months_neg": six_months_neg, "thirty_days": thirty_days, "thirty_days_neg": thirty_days_neg, "two_weeks": two_weeks, "two_weeks_neg": two_weeks_neg, "one_week": one_week, "one_week_neg": one_week_neg})

@api_view(['GET'])
def getVisualisationWidgetSentiementData(request, id):
    game = Game.objects.get(app_id=id)
    game_stats = GameStat.objects.get(app_id=game)

    # All time
    all_time = game_stats.current_sentiment_score
    # # 12 months
    twelve_months_neu = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(weeks=52), timezone.now()], sentiment_polarity__gte=-0.05000000000000000, sentiment_polarity__lte=0.04999999999999999).count()
    twelve_months_pos = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(weeks=52), timezone.now()], sentiment_polarity__gte=0.05000000000000001, sentiment_polarity__lte=1).count()
    twelve_months_neg = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(weeks=52), timezone.now()], sentiment_polarity__gte=-1, sentiment_polarity__lte=-0.05000000000000001).count()
    twelve_months_sub = twelve_months_pos + twelve_months_neg + twelve_months_neu
    if twelve_months_sub > 0:
        twelve_months = round((twelve_months_pos - twelve_months_neg) / twelve_months_sub, 3)
    else:
        twelve_months = 0
    # 6 months
    six_months_neu = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(weeks=26), timezone.now()], sentiment_polarity__gte=-0.05000000000000000, sentiment_polarity__lte=0.04999999999999999).count()
    six_months_pos = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(weeks=26), timezone.now()], sentiment_polarity__gte=0.05000000000000001, sentiment_polarity__lte=1).count()
    six_months_neg = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(weeks=26), timezone.now()], sentiment_polarity__gte=-1, sentiment_polarity__lte=-0.05000000000000001).count()
    six_months_sub = six_months_pos + six_months_neg + six_months_neu
    if six_months_sub > 0:
        six_months = round((six_months_pos - six_months_neg) / six_months_sub, 3)
    else:
        six_months = 0
    # 30 days
    thirty_days_neu = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(days=30), timezone.now()], sentiment_polarity__gte=-0.05000000000000000, sentiment_polarity__lte=0.04999999999999999).count()
    thirty_days_pos = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(days=30), timezone.now()], sentiment_polarity__gte=0.05000000000000001, sentiment_polarity__lte=1).count()
    thirty_days_neg = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(days=30), timezone.now()], sentiment_polarity__gte=-1, sentiment_polarity__lte=-0.05000000000000001).count()
    thirty_days_sub = thirty_days_pos + thirty_days_neg + thirty_days_neu
    if thirty_days_sub > 0:
        thirty_days = round((thirty_days_pos - thirty_days_neg) / thirty_days_sub, 3)
    else:
        thirty_days = 0
    # 2 weeks
    two_weeks_neu = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(days=14), timezone.now()], sentiment_polarity__gte=-0.05000000000000000, sentiment_polarity__lte=0.04999999999999999).count()
    two_weeks_pos = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(days=14), timezone.now()], sentiment_polarity__gte=0.05000000000000001, sentiment_polarity__lte=1).count()
    two_weeks_neg = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(days=14), timezone.now()], sentiment_polarity__gte=-1, sentiment_polarity__lte=-0.05000000000000001).count()
    two_weeks_sub = two_weeks_pos + two_weeks_neg + two_weeks_neu
    if two_weeks_sub > 0:
        two_weeks = round((two_weeks_pos - two_weeks_neg) / two_weeks_sub, 3)
    else:
        two_weeks = 0
    # 1 week
    one_week_neu = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(days=7), timezone.now()], sentiment_polarity__gte=-0.05000000000000000, sentiment_polarity__lte=0.04999999999999999).count()
    one_week_pos = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(days=7), timezone.now()], sentiment_polarity__gte=0.05000000000000001, sentiment_polarity__lte=1).count()
    one_week_neg = Review.objects.filter(app_id__app_id=id, time_created__range=[timezone.now() - timezone.timedelta(days=7), timezone.now()], sentiment_polarity__gte=-1, sentiment_polarity__lte=-0.05000000000000001).count()
    one_week_sub = one_week_pos + one_week_neg + one_week_neu
    if one_week_sub > 0:
        one_week = round((one_week_pos - one_week_neg) / one_week_sub, 3)
    else:
        one_week = 0

    return Response({"all_time": all_time, "twelve_months": twelve_months, "six_months": six_months, "thirty_days": thirty_days, "two_weeks": two_weeks, "one_week": one_week})

@api_view(['GET'])
def getVisualisationWidgetEmotionData(request, id):
    game = Game.objects.get(app_id=id)
    game_stats = GameStat.objects.get(app_id=game)

    # All time
    past_all_time = game_stats.emotion_all_time

    emotion_total = 0
    for emotion, score in past_all_time.items():
        emotion_total += score

    all_time = []
    if emotion_total > 0:
        for emotion, score in past_all_time.items():
            if (past_all_time[emotion] / emotion_total >= 0.15):
                all_time.append(emotion)

    # Twelve Months
    time = timezone.now()
    end_index = 0

    for index, stat in enumerate(game_stats.emotion_all_time_month):
        if(stat["year"] == time.year and stat["month"] == calendar.month_name[time.month]):
            end_index = index+1
            break

    start_index = end_index - 12
    past_twelve_months = []

    for stat in reversed(game_stats.emotion_all_time_month[start_index:end_index]):
        past_twelve_months.append(stat)

    emotions = {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}
    for past in past_twelve_months:
        for emotion, score in emotions.items():
            emotions[emotion] += past["emotion"][emotion]

    emotion_total = 0
    for emotion, score in emotions.items():
        emotion_total += score

    twelve_months = []
    if emotion_total > 0:
        for emotion, score in emotions.items():
            if (emotions[emotion] / emotion_total >= 0.15):
                twelve_months.append(emotion)

    # Six Months
    time = timezone.now()
    end_index = 0

    for index, stat in enumerate(game_stats.emotion_all_time_month):
        if(stat["year"] == time.year and stat["month"] == calendar.month_name[time.month]):
            end_index = index+1
            break

    start_index = end_index - 6
    past_six_months = []

    for stat in reversed(game_stats.emotion_all_time_month[start_index:end_index]):
        past_six_months.append(stat)

    emotions = {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}
    for past in past_six_months:
        for emotion, score in emotions.items():
            emotions[emotion] += past["emotion"][emotion]

    emotion_total = 0
    for emotion, score in emotions.items():
        emotion_total += score

    six_months = []
    if emotion_total > 0:
        for emotion, score in emotions.items():
            if (emotions[emotion] / emotion_total >= 0.15):
                six_months.append(emotion)

    # One Month
    past_one_month = game_stats.emotion_past_one_month

    emotion_total = 0
    for emotion, score in past_one_month.items():
        emotion_total += score

    one_month = []
    for emotion, score in past_one_month.items():
        if (past_one_month[emotion] / emotion_total >= 0.15):
            one_month.append(emotion)
    # Two Weeks
    past_two_weeks = game_stats.emotion_past_two_weeks

    emotion_total = 0
    for emotion, score in past_two_weeks.items():
        emotion_total += score

    two_weeks = []
    for emotion, score in past_two_weeks.items():
        if (past_two_weeks[emotion] / emotion_total >= 0.15):
            two_weeks.append(emotion)
    # One Week
    past_one_week = game_stats.emotion_past_one_week

    emotion_total = 0
    for emotion, score in past_one_week.items():
        emotion_total += score

    one_week = []
    if emotion_total > 0:
        for emotion, score in past_one_week.items():
            if (past_one_week[emotion] / emotion_total >= 0.15):
                one_week.append(emotion)

    return Response({"all_time": all_time, "twelve_months": twelve_months, "six_months": six_months, "one_month": one_month, "two_weeks": two_weeks, "one_week": one_week})


@api_view(['GET'])
def getVisualisationWidgetPlayerData(request, id):
    game = Game.objects.get(app_id=id)
    game_stats = GameStat.objects.get(app_id=game)

    # all time peak
    all_time_peak = game_stats.highest_player_count
    all_time_average = PlayerCount.objects.filter(app_id__app_id=id).aggregate(Avg('player_count'))
    all_time = {"peak": all_time_peak, "average": all_time_average["player_count__avg"]}
    # 30 day peak & Average
    thirty_day_peak = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[timezone.now() + timezone.timedelta(days=-30) , timezone.now()]).aggregate(Max('player_count'))
    thirty_day_average = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[timezone.now() + timezone.timedelta(days=-30) , timezone.now()]).aggregate(Avg('player_count'))
    thirty_days = {"peak": thirty_day_peak["player_count__max"], "average": thirty_day_average["player_count__avg"]}
    # 14 day peak & Average
    fourteen_day_peak = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[timezone.now() + timezone.timedelta(days=-14), timezone.now()]).aggregate(Max('player_count'))
    fourteen_day_average = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[timezone.now() + timezone.timedelta(days=-14), timezone.now()]).aggregate(Avg('player_count'))
    fourteen_days = {"peak": fourteen_day_peak["player_count__max"], "average": fourteen_day_average["player_count__avg"]}
    # 7 day peak & Average
    seven_day_peak = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[timezone.now() + timezone.timedelta(days=-7), timezone.now()]).aggregate(Max('player_count'))
    seven_day_average = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[timezone.now() + timezone.timedelta(days=-7), timezone.now()]).aggregate(Avg('player_count'))
    seven_days = {"peak": seven_day_peak["player_count__max"], "average": seven_day_average["player_count__avg"]}
    # 72 hours peak & Average
    seventy_two_peak = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[timezone.now() - timezone.timedelta(hours=73), timezone.now()]).aggregate(Max('player_count'))
    seventy_two_average = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[timezone.now() - timezone.timedelta(hours=73), timezone.now()]).aggregate(Avg('player_count'))
    seventy_two_hours = {"peak": seventy_two_peak["player_count__max"], "average": seventy_two_average["player_count__avg"]}
    # 48 hours peak & Average
    forty_eight_peak = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[timezone.now() - timezone.timedelta(hours=49), timezone.now()]).aggregate(Max('player_count'))
    forty_eight_average = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[timezone.now() - timezone.timedelta(hours=49), timezone.now()]).aggregate(Avg('player_count'))
    forty_eight_hours = {"peak": forty_eight_peak["player_count__max"], "average": forty_eight_average["player_count__avg"]}
    # 24 hours peak
    twenty_four_peak = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[timezone.now() - timezone.timedelta(hours=25), timezone.now()]).aggregate(Max('player_count'))
    twenty_four_average = PlayerCount.objects.filter(app_id__app_id=id, timestamp__range=[timezone.now() - timezone.timedelta(hours=25), timezone.now()]).aggregate(Avg('player_count'))
    twenty_four_hours = {"peak": twenty_four_peak["player_count__max"], "average": twenty_four_average["player_count__avg"]}

    return Response({"all_time": all_time, "thirty_days": thirty_days, "fourteen_days": fourteen_days, "seven_days": seven_days, "seventy_two_hours": seventy_two_hours, "forty_eight_hours": forty_eight_hours, "twenty_four_hours": twenty_four_hours})
    
@api_view(['GET'])
def getOldestDateForGamePlayerData(request, id):
    oldest_date = PlayerCount.objects.filter(app_id__app_id=id).earliest('timestamp')
    serializer = PlayerCountSerializer(oldest_date)

    return Response({"app_id": serializer.data["app_id"], "oldest_date": serializer.data['timestamp']})

@api_view(['GET'])
def test(request):

    print(request.session)
    print(request.user)
    print(request)

    return Response({"test": "text"})
