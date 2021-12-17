from django.urls import path
from tweets.views import *

app_name = 'tweets'

urlpatterns = [
    path('', homePage, name = 'home_page'),
    path('tweet/', postTweet, name = 'post_tweet'),
    path('like/', likeTweets, name = 'tweet_likes'),
    path('user/', viewUser, name = 'view_user'),
    path('hashtag/', viewHashtag, name = 'view_hashtag'),
    path('deleteTweet/', deleteTweet, name = 'delete_tweet')
]