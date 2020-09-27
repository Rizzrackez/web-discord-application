from discord.ext import commands
import discord
import os

from bot_services import convert_youtube


DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('\n----------------------')
    print(f'Logged in as {bot.user.name}')
    print(f'ID: {bot.user.id}')


@bot.event
async def on_message(ctx):

    """ctx: "discord_tag"+"discord_command"+"something"""

    try:
        content = ctx.content.split('+')
        user = bot.get_user(int(content[0]))

        if content[1] == "Тестовое сообщение":
            await user.send(f"Тестовое сообщение пользователю под id {user}.")

        elif content[1] == "Конвертация видео с ютуб в m4a файл":
            youtube_link = content[2]
            result_str = convert_youtube(youtube_link)
            await user.send(file=discord.File(f"music/{result_str}.m4a"))

    except ValueError:
        pass


if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
