from __future__ import annotations

from typing import TYPE_CHECKING

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from core.models import Tweet

if TYPE_CHECKING:
    from django.http import HttpRequest


def get_tweet_controller(request: HttpRequest, tweet_id: int) -> HttpResponse: # Получение выбранного твита
    tweet = get_object_or_404(Tweet, id=tweet_id)
    context = {"tweet": tweet}
    return render(request=request, template_name="get_tweet.html",context=context)
