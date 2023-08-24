from __future__ import annotations

from typing import TYPE_CHECKING

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from core.models import Tweet
from core.presentation.forms import SortForm

if TYPE_CHECKING:
    from django.http import HttpRequest


@require_http_methods(["GET"])
def home_controller(request: HttpRequest) -> HttpResponse:
    form = SortForm(request.GET)
    if form.is_valid():
        sort_by = form.cleaned_data['sort_by']
        if sort_by == 'Newest':
            tweets = Tweet.objects.all().order_by('-created_at')
        elif sort_by == 'Likes':
            tweets = Tweet.objects.all().order_by('-likes_count')
    else:
        tweets = Tweet.objects.all().order_by('-created_at')

    context = {
        'form': form,
        'tweets': tweets,
    }
    return render(request, 'home.html', context)