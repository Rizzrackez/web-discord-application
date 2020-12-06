from discord.ext import commands
import discord
import os
import random
from datetime import timedelta

from convert_video import convert_youtube
from parsing_movie_site import get_random_film
from get_currency import get_currency


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

        elif content[1] == "Случайный фильм":
            film = get_random_film() # [title, category, rating, description, image]
            description = "\n- ".join(film[1])
            embed = discord.Embed(
                colour=discord.Color.from_rgb(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)),
                title='',
                description=f''
            )

            embed.add_field(name=':movie_camera: **Название**',
                            value=film[0],
                            inline=False)

            embed.add_field(name=':film_frames: **Жанр**',
                            value=f'- {description}',
                            inline=False)

            embed.add_field(name=':star: **Рейтинг на кинопоиске**',
                            value=film[2],
                            inline=False)

            embed.add_field(name=':scroll: **Краткое описание**',
                            value=film[3],
                            inline=False)

            embed.set_image(url=film[4])
            await user.send(embed=embed)

        elif content[1] == "Конвертер валют":
            currency_from = content[2]
            currency_to = content[3]
            currency = get_currency(currency_from, currency_to)


            try:
                time_now = timedelta(hours=int(currency['time'][11:13]) + 3, minutes=int(currency['time'][14:16]),
                                     seconds=int(currency['time'][17:19]))

                await user.send(
                    f'Последнее обновление: **{time_now}**\n1.00 `{content[2]}` ⟶ {currency["amount"]} `{content[3]}`')

            except Exception:
                await user.send(
                    f'Последнее обновление: **undefined**\n1.00 `undefined` ⟶ `undefined`')

    except ValueError:
        pass


if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
