from __future__ import annotations

from typing import TYPE_CHECKING

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from django.db.models import Q

from core.models import Tweet, Retweet
from core.presentation.forms import SortForm

from django.core.paginator import Paginator

if TYPE_CHECKING:
    from django.http import HttpRequest


# @login_required
# @require_http_methods(["GET"])
# def home_controller(request: HttpRequest) -> HttpResponse:
#     current_user = request.user
#     followed_users = current_user.subscriptions.all()
    
#     tweets = Tweet.objects.filter(Q(author=current_user) | Q(author__in=followed_users), parent_tweet=None)
#     retweets = Retweet.objects.select_related('tweet').filter(Q(tweet__author__in=followed_users) | Q(user=current_user))
    
#     form = SortForm(request.GET)
    
#     if form.is_valid():
#         sort_by = form.cleaned_data['sort_by']
#         if sort_by == 'Newest':
#             tweets = tweets.order_by('-created_at')
#             retweets = retweets.order_by('-created_at')
#         elif sort_by == 'Likes':
#             tweets = tweets.order_by('-likes_count')
#     else:
#         tweets = tweets.order_by('-created_at')
    
#     paginator = Paginator(tweets, 10)
#     page_number = request.GET.get('page', 1)
#     page = paginator.get_page(page_number)
    
#     context = {
#         'form': form,
#         'tweets': page,
#         'retweets': retweets,
#     }
    
#     return render(request, 'home.html', context)

@login_required
@require_http_methods(["GET"])
def home_controller(request: HttpRequest) -> HttpResponse:
    current_user = request.user
    followed_users = current_user.subscriptions.all()
    
    tweets = Tweet.objects.filter(Q(author=current_user) | Q(author__in=followed_users), parent_tweet=None)
    retweets = Tweet.objects.prefetch_related('retweets').filter(retweets__user__in=followed_users)
    
    
    tweets_and_retweets = tweets.union(retweets)
    
    
    form = SortForm(request.GET)
    
    if form.is_valid():
        sort_by = form.cleaned_data['sort_by']
        if sort_by == 'Newest':
            tweets_and_retweets = tweets_and_retweets.order_by('-created_at')
        elif sort_by == 'Likes':
            tweets_and_retweets = tweets_and_retweets.order_by('-likes_count')
    else:
        tweets_and_retweets = tweets_and_retweets.order_by('-created_at')
    
    paginator = Paginator(tweets_and_retweets, 4)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    
    context = {
        'form': form,
        'tweets': tweets,
        'retweets': retweets,
        'tweets_and_retweets': page,
        # 'pages': page
    }
    return render(request, 'home.html', context)
