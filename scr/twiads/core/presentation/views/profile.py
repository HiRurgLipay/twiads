from __future__ import annotations

import logging

from typing import TYPE_CHECKING
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.core.paginator import Paginator


from core.models import Tweet
from core.presentation.converters import convert_data_from_form_to_dto
from core.business_logic.services import edit_profile
from core.business_logic.dto import EditProfileDto
from core.presentation.forms import EditProfileForm, SortForm


if TYPE_CHECKING:
    from django.http import HttpRequest

logger = logging.getLogger(__name__)



@require_http_methods(request_method_list=["GET"])
def profile_controller(request: HttpRequest) -> HttpResponse:
    tweets = Tweet.objects.filter(author=request.user)
    form = SortForm(request.GET)
    
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
    
    context = {"tweets": tweets,
               'form': form,
               'tweets': page,}
    
    return render(request=request, template_name="profile.html", context=context)   
  

@require_http_methods(request_method_list=["GET", "POST"])
def edit_profile_controller(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        user = request.user
        form = EditProfileForm(initial={
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "birth_date": user.birth_date,
            "country": user.country.name
        })
        context = {"form": form}
        return render(request=request, template_name="edit_profile.html", context=context)
    
    elif request.method == "POST":
        form = EditProfileForm(data=request.POST)
        if form.is_valid():
            data = convert_data_from_form_to_dto(EditProfileDto, data_from_form=form.cleaned_data)
            user = request.user
            edit_profile(data=data, user=user)
            return HttpResponseRedirect(redirect_to=reverse("profile"))
