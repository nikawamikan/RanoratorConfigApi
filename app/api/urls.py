from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("discord_server_configs/<int:pk>",
         views.DiscordServerConfigDetail.as_view()),
    path("discord_server_configs",
         views.DiscordServerConfigListCreate.as_view()),
]
