from django.db import models

BOT_COMMANDS = (
    ('Тестовое сообщение.', 'Тестовое сообщение'),
    ('Конвертация видео с ютуб в m4a файл.', 'Конвертация видео с ютуб в m4a файл.'),
)


class BotInteraction(models.Model):
    discord_tag = models.CharField(max_length=20)
    youtube = models.CharField(max_length=120)
    command = models.CharField(max_length=100, choices=BOT_COMMANDS, default=1)

    class Meta:
        verbose_name = "Bot Interaction"
        verbose_name_plural = "Bot Interactions"

    def __str__(self):
        return self.discord_tag

