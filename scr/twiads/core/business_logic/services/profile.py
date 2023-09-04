from __future__ import annotations
from typing import TYPE_CHECKING
from django.contrib.auth import get_user_model
from django.db import transaction
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpRequest
from core.models import ConfirmationCode, User, Country, Tweet, Retweet
from core.business_logic.services.common import replace_file_name_to_uuid, change_file_size


import uuid
import time

if TYPE_CHECKING:
    from core.business_logic.dto import EditProfileDto



def edit_profile(data: EditProfileDto, user: User) -> None:
    with transaction.atomic():
        if data.avatar:
            data.avatar = replace_file_name_to_uuid(file=data.avatar)
            data.avatar = change_file_size(file=data.avatar)
            user.avatar.delete()  # Удалите текущий аватар пользователя
            user.avatar.save(data.avatar.name, data.avatar)
        else:
            user.avatar = data.avatar
            
        country = Country.objects.get(name=data.country)
        User.objects.filter(id=user.id).update(
            username = data.username,
            first_name = data.first_name,
            last_name = data.last_name,
            bio = data.bio,
            email = data.email,
            birth_date = data.birth_date,
            country = country
        )
        
        user.save()
        
        if data.email != user.email:
            user.email = data.email
            user.is_active = False
            user.save()

            confirmation_code = str(uuid.uuid4())
            code_expiration_time = int(time.time()) + settings.CONFIRMATION_CODE_LIFETIME
            ConfirmationCode.objects.create(code=confirmation_code, user=user, expiration_time=code_expiration_time)

            confirmation_url = settings.SERVER_HOST + reverse("confirm-email") + f"?code={confirmation_code}"
            send_mail(
                subject="Confirm your new email",
                message=f"Please confirm your new email by clicking the link below:\n\n{confirmation_url}",
                from_email=settings.EMAIL_FROM,
                recipient_list=[data.email],
            )


# def initialize_profile(user):
#     initial_data = {
#         "avatar": user.avatar,
#         "username": user.username,
#         "first_name": user.first_name,
#         "last_name": user.last_name,
#         "email": user.email,
#         "birth_date": user.birth_date,
#         "country": user.country.name
#     }
#     return initial_data
# def get_another_profile(username: str) -> None:
#     with transaction.atomic():
#         user = get_object_or_404(User, username=username)
#         tweets = Tweet.objects.filter(author=user)
#         retweets = Retweet.objects.filter(user=user)



# @require_http_methods(request_method_list=["GET"])
# def another_profile_controller(request: HttpRequest, username: str) -> HttpResponse:
#     user = get_object_or_404(User, username=username)
#     retweets = Retweet.objects.filter(user=user)
#     form = SortForm(request.GET)
#     if form.is_valid():
#         sort_by = form.cleaned_data['sort_by']
#     else:
#         sort_by = None

#     tweets = sort_tweets(get_user_tweets(user), sort_by)
    
#     paginator = Paginator(tweets, 2)
#     page_number = request.GET.get('page', 1)
#     page = paginator.get_page(page_number)
    
#     context = {
#         "user": user,
#         "tweets": page,
#         "retweets": retweets,
#         "form": form,
#     }
#     return render(request=request, template_name='another_profile.html', context=context)
