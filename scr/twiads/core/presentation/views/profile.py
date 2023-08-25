from __future__ import annotations

from typing import TYPE_CHECKING
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from core.presentation.forms import EditProfileForm
import logging
from core.models import Tweet

if TYPE_CHECKING:
    from django.http import HttpRequest

logger = logging.getLogger(__name__)


@require_http_methods(request_method_list=["GET", "POST"])
def profile_controller(request: HttpRequest) -> HttpResponse:
    # if request.method == "GET":
    form =EditProfileForm()
    tweets = Tweet.objects.filter(author=request.user)
    context = {"form": form, "tweets": tweets}
    return render(request=request, template_name="profile.html", context=context)
    # elif request.method == "POST":
        # form = EditProfileForm(data=request.POST)
        # if form.is_valid:
            



        
  