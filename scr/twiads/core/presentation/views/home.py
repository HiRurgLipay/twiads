from __future__ import annotations

from typing import TYPE_CHECKING

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from core.models import Tweet
from core.presentation.forms import SortForm

from core.presentation.pagination import CustomPagination, PageNotExists

if TYPE_CHECKING:
    from django.http import HttpRequest


@require_http_methods(["GET"])
def home_controller(request: HttpRequest) -> HttpResponse:
    tweets = Tweet.objects.all()
    form = SortForm(request.GET)
    tweets_paginated = None
    
    if form.is_valid():
        sort_by = form.cleaned_data['sort_by']
        if sort_by == 'Newest':
            tweets = Tweet.objects.all().order_by('-created_at')
        elif sort_by == 'Likes':
            tweets = Tweet.objects.all().order_by('-likes_count')
        
        try:
            page_number = request.GET["page"]
        except KeyError:
            page_number = 1
            
        paginator = CustomPagination(per_page=3)
        try:
            tweets_paginated = paginator.paginate(data=tweets, page_number=page_number)
        except PageNotExists:
            return HttpResponseBadRequest(content="Page with provided number doesn't exist.")
    
    else:
        tweets = Tweet.objects.all().order_by('-created_at')
        
        try:
            page_number = request.GET["page"]
        except KeyError:
            page_number = 1
            
        paginator = CustomPagination(per_page=20)
        try:
            tweets_paginated = paginator.paginate(data=tweets, page_number=page_number)
        except PageNotExists:
            return HttpResponseBadRequest(content="Page with provided number doesn't exist.")

    context = {
        'form': form,
        'tweets': tweets_paginated,
    }
    return render(request, 'home.html', context)
