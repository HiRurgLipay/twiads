from __future__ import annotations

import logging

from typing import TYPE_CHECKING
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from core.models import User
from core.business_logic.services import subscribe_and_unsubscribe
from core.business_logic.dto import SubscriberDTO

from django.shortcuts import redirect

if TYPE_CHECKING:
    from django.http import HttpRequest


@require_http_methods(request_method_list=["GET","POST"])
def subscriber_controller(request: HttpRequest, username: str) -> HttpResponse:
    user = get_object_or_404(User, username=username)
    subscriber_user = request.user
    print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", user)
    print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", subscriber_user)
    if request.method == "POST":
        data = SubscriberDTO(username=user.username, subscriber_username=subscriber_user.username)
        print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", data)
        subscribe_and_unsubscribe(data=data)
    current_page = request.META.get('HTTP_REFERER')
    return redirect(current_page)
