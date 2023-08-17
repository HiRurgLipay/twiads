# from core.presentation.views import about, contact, index
from django.urls import path
from core.presentation.views import home_controller, get_tweet_controller
#  urlpatterns: list[type] = []


urlpatterns = [
    path("", home_controller, name="home"),
    path("tweet//<int:tweet_id>/", get_tweet_controller, name="get-tweet")
]
