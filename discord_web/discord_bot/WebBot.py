from discord.ext import commands
import discord
import os
import random
from datetime import timedelta


from convert_video import convert_youtube
from parsing_movie_site import get_random_film
from get_currency import get_currency
from get_weather import get_weather_by_id, get_len_weather


DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='=')

@bot.event
async def on_ready():
    print('\n----------------------')
    print(f'Logged in as {bot.user.name}')
    print(f'ID: {bot.user.id}')


@bot.event
async def on_message(ctx):

    """ctx: "discord_tag"+"discord_command"+"something"""

    if ctx.content == "weatcher":
        embed = discord.Embed(
            colour=discord.Color.from_rgb(0, 204, 255),
            title='Погода на 19:00 - СПБ',
            description=f''
        )
        embed.set_image(
            url="https://lh3.googleusercontent.com/proxy/mezk6K1-Oo4V4AOsxczBfSkx0sW-EQAtheHJgmsvTlQGGpffZ6kJ3XWyrVR-BhnTnjrklzTJ3Md3GVbXZdN5Xwh9itoUWRfPzxtw0jFO6bMb")
        embed.add_field(name='Состояние погоды',
                        value="Пасмурно, дождь",
                        inline=False)
        embed.add_field(name='Температура',
                        value="-1°",
                        inline=False)
        embed.add_field(name='Вероятность осадков',
                        value="60%°",
                        inline=False)

        await ctx.channel.send(embed=embed)

    if ctx.channel.id == 780133612258721804 and ctx.content == "!sub-weather":
        member = ctx.author
        roles = ctx.guild.roles[2]
        await member.add_roles(roles)
        await ctx.channel.send(f'{ctx.author.mention} оформил подписку на рассылку **прогноза погоды**!')

    if ctx.channel.id == 780133612258721804 and ctx.content == "!sub-movie":
        member = ctx.author
        roles = ctx.guild.roles[1]
        await member.add_roles(roles)
        await ctx.channel.send(f'{ctx.author.mention} оформил подписку на рассылку **кино**!')

    if ctx.content == "movie":

        for ch in ctx.guild.channels:
            if ch.name == "кино":
                movie_channel = ch

        film = get_random_film()
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

        await movie_channel.send(embed=embed)

    try:

        content = ctx.content.split('+')
        user = bot.get_user(int(content[0]))

        if content[1] == "Тестовое сообщение":
            await user.send(f"Тестовое сообщение пользователю под id {user}.")

        elif content[1] == "Конвертация видео с ютуб в m4a файл":
            youtube_link = content[2]
            result_str = convert_youtube(youtube_link)
            await user.send(file=discord.File(f"music/{result_str}.m4a"))

        elif content[1] == "Погода":

            city = get_weather_by_id(content[2])
            await user.send(f"\n\nПогода - {content[2]}\n\n" + city)

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
            print(currency)
            time_now = timedelta(hours=int(currency['time'][11:13]) + 3, minutes=int(currency['time'][14:16]), seconds=int(currency['time'][17:19]))

            await user.send(f'Последнее обновление: **{time_now}**\n1.00 `{content[2]}` ⟶ {currency["amount"]} `{content[3]}`')


    except ValueError:
        pass


if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
