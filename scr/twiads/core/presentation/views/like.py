from __future__ import annotations

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from core.models import Tweet, Like


@login_required
def like_controller(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    user = request.user
    
    like_count = tweet.likes_count

    existing_like = Like.objects.filter(tweet=tweet, user=user).first()
    if existing_like:
        existing_like.delete()
        tweet.likes_count = like_count - 1
    else:
        Like.objects.create(tweet=tweet, user=user)
        tweet.likes_count = like_count + 1

    tweet.save()

    current_page = request.META.get('HTTP_REFERER')
    return redirect(current_page)
