import requests


discord_webhook_url = 'https://discordapp.com/api/webhooks/754976056313643028/L1zVe-xJ4712mG30q_hHJoApbmTWxVjP5g69oK7zHQmrliuTBx3QJYAouaLxVR7hDP4O'


def send_user_id(discord_user_id):
    data = {
        "content": discord_user_id
    }
    requests.post(discord_webhook_url, data=data)






