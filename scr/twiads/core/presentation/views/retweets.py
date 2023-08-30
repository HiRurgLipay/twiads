from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from core.models import Tweet, Retweet

def retweet_view(request, tweet_id):
    user = request.user
    tweet = get_object_or_404(Tweet, pk=tweet_id, )
    retweet_count = tweet.retweets_count
    
    retweet = Retweet(user=user, tweet=tweet)
    retweet.save()
    tweet.retweets_count = retweet_count + 1
    tweet.save()
    
    current_page = request.META.get('HTTP_REFERER')
    return redirect(current_page)
