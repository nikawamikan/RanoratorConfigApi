from rest_framework import generics
from api.models import DiscordServerConfigModel
from .serializers import DiscordServerConfigModelSerializer


class DiscordServerConfigListCreate(generics.ListCreateAPIView):
    queryset = DiscordServerConfigModel.objects.all()
    serializer_class = DiscordServerConfigModelSerializer


class DiscordServerConfigDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiscordServerConfigModel.objects.all()
    serializer_class = DiscordServerConfigModelSerializer
