from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.urls import reverse

from core.business_logic.services import create_tweet
from core.presentation.converters import convert_data_from_form_to_dto
from core.business_logic.dto import AddTweetDTO
from core.models import Tweet
from core.presentation.forms import AddTweetForm
import logging



if TYPE_CHECKING:
    from django.http import HttpRequest
    
    
logger = logging.getLogger(__name__)

User = get_user_model()


@login_required
@require_http_methods(request_method_list=["GET", "POST"])
def add_tweet_controller(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = AddTweetForm()
        context = {"form": form}
        logger.info("Rendered form")
        return render(request=request, template_name="add_tweet.html", context=context)
    
    elif request.method == "POST":
        form = AddTweetForm(data=request.POST)
        if form.is_valid():
            logger.info("Form is valid")
            data = convert_data_from_form_to_dto(AddTweetDTO, data_from_form=form.cleaned_data)
            data.author = request.user
            create_tweet(data=data)
            return HttpResponseRedirect(redirect_to=reverse("home"))
        else:
            logger.info("Invalid form", extra={"post_data": request.POST})
    return HttpResponseBadRequest("Incorrect http method")

@require_http_methods(request_method_list=["GET"])
def get_tweet_controller(request: HttpRequest, tweet_id: int) -> HttpResponse:
    tweet = get_object_or_404(Tweet, id=tweet_id)
    context = {"tweet": tweet}
    return render(request=request, template_name="get_tweet.html",context=context)
