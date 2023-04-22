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
    return Response({"message": "Review Visualisation Widgets Data"})

@api_view(['GET'])
def getVisualisationWidgetSentiementData(request, id):
    return Response({"message": "Sentiment Visualisation Widgets Data"})

@api_view(['GET'])
def getVisualisationWidgetEmotionData(request, id):
    return Response({"message": "Emotion Visualisation Widgets Data"})

@api_view(['GET'])
def getVisualisationWidgetPlayerData(request, id):
    return Response({"message": "Player Visualisation Widgets Data"})

@api_view(['GET'])
def test(request):

    print(request.session)
    print(request.user)
    print(request)

    return Response({"test": "text"})
