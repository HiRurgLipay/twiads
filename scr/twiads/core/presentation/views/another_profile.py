from __future__ import annotations

import logging

from typing import TYPE_CHECKING
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404
from core.models import User, Tweet, Retweet
from core.presentation.forms import SortForm
from django.core.paginator import Paginator

if TYPE_CHECKING:
    from django.http import HttpRequest

logger = logging.getLogger(__name__)


@require_http_methods(request_method_list=["GET"])
def another_profile_controller(request: HttpRequest, username: str) -> HttpResponse:
    user = get_object_or_404(User, username=username)
    tweets = Tweet.objects.filter(author=user)
    retweets = Retweet.objects.filter(user=user)
    form  = SortForm(request.GET)
    if form.is_valid():
        sort_by = form.cleaned_data['sort_by']
        if sort_by == 'Newest':
            tweets = tweets.order_by('-created_at')
        elif sort_by == 'Likes':
            tweets = tweets.order_by('-likes_count')
    else:
        tweets = tweets.order_by('-created_at')
    
    paginator = Paginator(tweets, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    
    context = {
        "user": user,
        "tweets":tweets,
        "retweets":retweets,
        "form": form,
        "tweets": page,
    }
    return render(request=request, template_name='another_profile.html', context=context)

# @require_http_methods(request_method_list=["GET"])
# def another_profile_controller(request: HttpRequest, username: str) -> HttpResponse:
    
#     user = get_object_or_404(User, username=username)
#     tweets = Tweet.objects.filter(author=user)
#     retweets = Tweet.objects.prefetch_related('retweets').filter(author=user)
    
#     tweets_and_retweets = tweets.union(retweets)
    
#     form  = SortForm(request.GET)
#     tweets_and_retweets = tweets_and_retweets.order_by('-created_at')
    
#     paginator = Paginator(tweets_and_retweets, 2)
#     page_number = request.GET.get('page', 1)
#     page = paginator.get_page(page_number)
  
#     context = {
#         "user": user,
#         "tweets":tweets,
#         "retweets":retweets,
#         "form": form,
#         'tweets_and_retweets': page,
#     }
#     return render(request=request, template_name='another_profile.html', context=context)
