from django.urls import path
from django.shortcuts import redirect
from core.presentation.views import (
    home_controller, 
    get_tweet_controller, 
    add_tweet_controller,  
    login_controller,
    logout_controller,
    registration_confirmation_controller,
    registration_controller,
    confirm_email_stub_controller,
    profile_controller,
    edit_profile_controller,
    tags_views_controller,
    top_tags_controller,
    like_controller,
    subscriber_controller,
    another_profile_controller,
    add_comment_controller,
    retweet_view,
)


urlpatterns = [
    path("", lambda request: redirect('login')),
    path("home/", home_controller, name="home"),
    path("profile/", profile_controller, name="profile"),
    path('profile/<str:username>/', another_profile_controller, name='another-profile'),
    path("profile/edit", edit_profile_controller, name="edit-profile"),
    path("tweet/add/", add_tweet_controller, name="add-tweet"),
    path("tweet//<int:tweet_id>/", get_tweet_controller, name="get-tweet"),
    path("signup/", registration_controller, name="registration"),
    path("confirmation/", registration_confirmation_controller, name="confirm-signup"),
    path("confirm/note/", confirm_email_stub_controller, name="confirm-stub"),
    path("singnin/", login_controller, name="login"),
    path("logout/", logout_controller, name="logout"),
    path("tags/", tags_views_controller, name="tags"),
    path("populated/tags/", top_tags_controller, name="top_tags"),
    path('<int:tweet_id>/like', like_controller, name='like_tweet'),
    path("profile/<str:username>/sub/", subscriber_controller, name="subscribe-from-profile"),
    path('comment/<int:tweet_id>/', add_comment_controller, name='comment'),
    path('retweet/<int:tweet_id>/', retweet_view, name='retweet'),
]
