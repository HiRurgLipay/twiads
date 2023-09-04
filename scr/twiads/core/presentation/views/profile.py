# from __future__ import annotations

# import logging

# from typing import TYPE_CHECKING

# from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
# from django.shortcuts import render, redirect
# from django.views.decorators.http import require_http_methods
# from django.core.paginator import Paginator
# from django.contrib.auth.decorators import login_required
# from django.urls import reverse

# from core.business_logic.exceptions import ConfirmationCodeExpired, ConfirmationCodeNotExists
# from core.models import Tweet, Retweet
# from core.presentation.converters import convert_data_from_form_to_dto
# from core.business_logic.services import confirm_user_registration, edit_profile, initialize_profile
# from core.business_logic.dto import EditProfileDto
# from core.presentation.forms import EditProfileForm, SortForm


# if TYPE_CHECKING:
#     from django.http import HttpRequest

# logger = logging.getLogger(__name__)



# @require_http_methods(request_method_list=["GET"])
# def profile_controller(request: HttpRequest) -> HttpResponse:
#     tweets = Tweet.objects.filter(author=request.user)
#     retweets = Retweet.objects.filter(user=request.user)
#     form = SortForm(request.GET)
    
#     if form.is_valid():
#         sort_by = form.cleaned_data['sort_by']
#         if sort_by == 'Newest':
#             tweets = tweets.order_by('-created_at')
#         elif sort_by == 'Likes':
#             tweets = tweets.order_by('-likes_count')
#     else:
#         tweets = tweets.order_by('-created_at')
    
#     paginator = Paginator(tweets, 2)
#     page_number = request.GET.get('page', 1)
#     page = paginator.get_page(page_number)
    
#     context = {"tweets": tweets,
#                "retweets": retweets,
#                'form': form,
#                'tweets': page,}
    
#     return render(request=request, template_name="profile.html", context=context)   
  

# @login_required
# @require_http_methods(request_method_list=["GET", "POST"])
# def edit_profile_controller(request: HttpRequest) -> HttpResponse:
#     if request.method == "GET":
#         if request.user.is_authenticated:
#             user = request.user
#             initial_data = initialize_profile(user)
#             form = EditProfileForm(initial=initial_data)
#             context = {"form": form}
#             return render(request=request, template_name="edit_profile.html", context=context)
#         else:
#             return HttpResponse("You need to log in to edit your profile.")

#     elif request.method == "POST":
#         if request.user.is_authenticated:
#             form = EditProfileForm(data=request.POST, files=request.FILES)
#             if form.is_valid():
#                 data = convert_data_from_form_to_dto(EditProfileDto, data_from_form=form.cleaned_data)
#                 user = request.user
#                 if form.cleaned_data["change_email"]:
#                    edit_profile(data=data, user=user)
#                 else:
#                     edit_profile(data=data, user=user)
#                     return HttpResponseRedirect(redirect_to=reverse("profile"))
#             else:
#                 form = EditProfileForm(request.POST)
#                 context = {"form": form}
#                 return render(request=request, template_name="edit-profile", context=context)
            

# @require_http_methods(["GET"])
# def confirm_email_stub_controller(request: HttpRequest) -> HttpResponse:
#     return HttpResponse("Confirmation email sent. Please confirm it by the link.")


# @require_http_methods(["GET"])
# def registration_confirmation_controller(request: HttpRequest) -> HttpResponse:
#     confirmation_code = request.GET["code"]
#     try:
#         confirm_user_registration(confirmation_code=confirmation_code)
#     except ConfirmationCodeNotExists:
#         return HttpResponseBadRequest(content="Invalid confirmation code.")
#     except ConfirmationCodeExpired:
#         return HttpResponseBadRequest(content="Confirmation code expired.")

#     return redirect(to="login")
