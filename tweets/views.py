from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import *
from .models import *

# Create your views here.


app_name = 'tweets'

def homePage(request):
    user = request.user

    if user.id == None:
        return redirect('/login')

    tweet = Tweet.objects.all().order_by('-created_at')
    user = request.user
    hashtags = Tag.objects.all()
    context = {
        'tweet': tweet,
        'user': user,
        'hashtags': hashtags
    }

    return render(request, 'home.html', context)

def viewUser(request):
    user = request.user

    if user.id == None:
        return redirect('/login')

    user = User.objects.filter(username = request.GET.get('user'))
    username = str(user.first().username)
    tweet = Tweet.objects.all().filter(author=user.first().id).order_by('-created_at')

    user2 = request.user

    context = {
        'tweet' : tweet,
        'user' : user2,
        'username' : username
    }

    return render(request, 'user.html', context)

def viewHashtag(request):
    user = request.user

    if user.id == None:
        return redirect('/login')

    hashtag = Tag.objects.filter(tag=request.GET.get('hashtag'))
    hashtag = hashtag.first()
    
    tweet = hashtag.tweets.all().order_by('-created_at')

    context = {
        'hashtag' : hashtag.tag,
        'tweet' : tweet,
        'user' : user
    }

    return render(request, 'hashtag.html', context)


def likeTweets(request):
    user = request.user

    if user.id == None:
        return redirect('/login')

    if request.method == 'POST':
        tweet_id = request.POST.get('tweet_id')
        tweet_obj = Tweet.objects.get(id=tweet_id)

        if user in tweet_obj.likes.all():
            tweet_obj.likes.remove(user)
        else:
            tweet_obj.likes.add(user)

        like, created = Like.objects.get_or_create(user=user, tweet_id = tweet_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
    return redirect('tweets:home_page')


def postTweet(request):
    user = request.user

    if user.id == None:
        return redirect('/login')

    if request.method == 'POST':
        body = request.POST.get('body')
        if (len(body) == 0):
            messages.error(request, 'Cannot post a blank tweet.')
        else:            
            tweet = Tweet.objects.create(body=body, author=user)
            tweet.save()
            getTweet = Tweet.objects.get(id=tweet.id)
            parseHashtags(body, getTweet)

    return redirect('tweets:home_page')

def parseHashtags(body, tweet):
    hashtagStrings = {tag.strip('#') for tag in body.split() if tag.startswith('#')}
    for string in hashtagStrings:
        tag = Tag.objects.all().filter(tag=string)
        if (tag.first() == None):
            tag = Tag.objects.create(tag=string)
            tag.save()
            first = Tag.objects.get(id=tag.id)
        else: 
            first = tag.first()
        first.tweets.add(tweet)


def deleteTweet(request):
    user = request.user

    if user.id == None:
        return redirect('/login')

    if request.method == 'POST':
        tweet_id = request.POST.get('tweet_id')
        instance = Tweet.objects.get(id=tweet_id)
        instance.delete()            

    return redirect('tweets:home_page')



