from discord.ext import commands

DISCORD_TOKEN = 'NzU1MDQyNTUwNjAzMzE3Mjg4.X19iLA.lrpT3_Y0yqs2DbcB8vgZDxWh6Qk'

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('\n----------------------')
    print(f'Logged in as {bot.user.name}')
    print(f'ID: {bot.user.id}')


@bot.event
async def on_message(ctx):
    user = bot.get_user(int(ctx.content))
    print(user)
    await user.send("Good luck, have fun!")


if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)