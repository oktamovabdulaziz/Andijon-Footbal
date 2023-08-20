from django.urls import path
from .views import *

urlpatterns = [
    path("news/", NewsView.as_view()),
    path("video/", VideoView.as_view()),
    path("table/", TableView.as_view()),
    path("player/", PlayerView.as_view()),
    path("product/", ProductView.as_view()),
    path("photo/", PhotoView.as_view()),
    path("arena/", ArenaView.as_view()),
    path("sponsors/", SponsorsView.as_view()),
    path("info/", InfoView.as_view()),
    path("newDetail/", NewDetailView.as_view()),
    path("press/", PressView.as_view()),
    path("club/", ClubView.as_view()),
    path("advice/", AdviceView.as_view()),
    path("training/", TrainingView.as_view()),
    path("arena-history/", ArenaHistoryView.as_view()),
]
