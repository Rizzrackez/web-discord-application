from discord_bot.webhook import send_user_id
from django.shortcuts import render, redirect
from backend.commands.bot_command import create_context_for_test_message, create_context_for_convert_youtube

BOT_COMMAND = {
    'Тестовое сообщение': create_context_for_test_message,
    'Конвертация видео с ютуб в m4a файл.': create_context_for_convert_youtube
}


def call_bot_command(command, data):
    BOT_COMMAND[command](data)

