from django.db import models

BOT_COMMANDS = (
    ('Тестовое сообщение', 'Тестовое сообщение'),
    ('Test case 1', 'Test case 1'),
    ('Test case 2', 'Test case 2'),
)


class BotInteraction(models.Model):
    discord_tag = models.CharField(max_length=20)
    command = models.CharField(max_length=100, choices=BOT_COMMANDS)

    class Meta:
        verbose_name = "Bot Interaction"
        verbose_name_plural = "Bot Interactions"

    def __str__(self):
        return self.discord_tag

