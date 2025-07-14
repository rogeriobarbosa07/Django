from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("djangoapp/", views.detail, name="detail"),
    path("djangoapp/results/", views.results, name="results"),
    path("djangoapp/vote/", views.vote, name="vote"),
]