from django.urls import path
from core.presentation.views import index, about, contact


#  urlpatterns: list[type] = []


urlpatterns = [
    path('', index),
    path('about', about),
    path('contact', contact),
]
