from rest_framework import serializers
from api.models import DiscordServerConfigModel


class DiscordServerConfigModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscordServerConfigModel
        fields = '__all__'
