from __future__ import annotations

from typing import TYPE_CHECKING
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from core.presentation.forms import ProfileForm

if TYPE_CHECKING:
    from django.http import HttpRequest


@require_http_methods(request_method_list=["GET", "POST"])
def profile_controller(request: HttpRequest) -> HttpResponse:
    # if  request.method == "GET":
    form = ProfileForm()
    context = {"form": form}
    return render(request=request, template_name="profile.html", context=context)
    