from rest_framework import generics
from api.models import DiscordServerConfigModel
from .serializers import DiscordServerConfigModelSerializer


class DiscordServerConfig(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiscordServerConfigModel.objects.all()
    serializer_class = DiscordServerConfigModelSerializer
