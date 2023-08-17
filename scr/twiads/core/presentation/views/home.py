from __future__ import annotations

from typing import TYPE_CHECKING

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from core.models import Tweet

if TYPE_CHECKING:
    from django.http import HttpRequest


def home_controller(request: HttpRequest) -> HttpResponse:
    tweets = Tweet.objects.all
    context = {"tweets": tweets} # dictionary with data that is passed to the template
    return render(request=request, template_name="home.html", context=context)
