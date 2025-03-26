from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("discord_server_configs/<int:pk>",
         views.DiscordServerConfig.as_view()),
]
