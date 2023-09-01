from __future__ import annotations

from typing import TYPE_CHECKING

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required



from core.models import Tweet, Retweet
from core.presentation.forms import SortForm

from django.core.paginator import Paginator

if TYPE_CHECKING:
    from django.http import HttpRequest



@login_required
@require_http_methods(["GET"])
def home_controller(request: HttpRequest) -> HttpResponse:
    tweets = Tweet.objects.filter(parent_tweet=None)
    retweets = Retweet.objects.select_related('tweet')
    form = SortForm(request.GET)
    
    if form.is_valid():
        sort_by = form.cleaned_data['sort_by']
        if sort_by == 'Newest':
            tweets = tweets.order_by('-created_at')
        elif sort_by == 'Likes':
            tweets = tweets.order_by('-likes_count')
    else:
        tweets = tweets.order_by('-created_at')
    
    
    paginator = Paginator(tweets, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    context = {
        'form': form,
        'tweets': page,
        'retweets': retweets,
    }
    return render(request=request, template_name="home.html", context=context)
