from discord_bot.webhook import send_user_id


def create_context_for_test_message(data):
    context = f"{data['discord_tag']}+{data['command']}"
    send_user_id(context)


def create_context_for_convert_youtube(data):
    context = f"{data['discord_tag']}+{data['command']}+{data['youtube']}"
    send_user_id(context)


def get_random_film(data):
    context = f"{data['discord_tag']}+{data['command']}"
    send_user_id(context)


def create_context_for_currency(data):
    context = f"{data['discord_tag']}+{data['command']}+{data['currency_from']}+{data['currency_to']}"
    send_user_id(context)


def create_context_for_weather(data):
    context = f"{data['discord_tag']}+{data['command']}+{data['weather']}"
    send_user_id(context)
