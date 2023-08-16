from core.presentation.views import about, contact, index
from django.urls import path

#  urlpatterns: list[type] = []


urlpatterns = [
    path("", index),
    path("about", about),
    path("contact", contact),
]
