from django.db import models


class DiscordServerConfigModel(models.Model):
    server_id = models.BigIntegerField(primary_key=True)
    default_voice_model_key = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'discord_server_config_model'
