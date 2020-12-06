from backend.commands.bot_command import create_context_for_test_message, \
    create_context_for_convert_youtube, \
    get_random_film, \
    create_context_for_currency

BOT_COMMAND = {
    'Тестовое сообщение': create_context_for_test_message,
    'Конвертация видео с ютуб в m4a файл': create_context_for_convert_youtube,
    'Случайный фильм': get_random_film,
    'Конвертер валют': create_context_for_currency,
}


def call_bot_command(command, data):
    BOT_COMMAND[command](data)

