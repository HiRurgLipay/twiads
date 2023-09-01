from __future__ import annotations
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from core.models import Tweet, Retweet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.http import HttpRequest
    
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods
from django.urls import reverse

from core.models import Tweet
from core.presentation.forms import AddCommentForm
import logging

def add_retweet_controller(request, tweet_id):
    user = request.user
    tweet = get_object_or_404(Tweet, pk=tweet_id, )
    retweet_count = tweet.retweets_count
    
    retweet = Retweet(user=user, tweet=tweet)
    retweet.save()
    tweet.retweets_count = retweet_count + 1
    tweet.save()
    
    current_page = request.META.get('HTTP_REFERER')
    return redirect(current_page)


@login_required
@require_http_methods(request_method_list=["POST"])
def delete_retweet_controller(request, tweet_id):
    user = request.user
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    
    # Проверяем, есть ли ретвит от данного пользователя
    retweet = Retweet.objects.filter(user=user, tweet=tweet).first()
    if retweet:
        # Удаляем ретвит
        retweet.delete()
        tweet.retweets_count -= 1
        tweet.save()
    
    current_page = request.META.get('HTTP_REFERER')
    return redirect(current_page)
