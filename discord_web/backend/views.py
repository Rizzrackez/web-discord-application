from django.shortcuts import render, redirect
from backend.forms import BotInteractionForm

from discord_bot.webhook import send_user_id


def main_page(request):
    form = BotInteractionForm(data=request.POST)
    if form.is_valid():
        discord_tag = form.data["discord_tag"]
        send_user_id(discord_tag)
        form.save()
        return redirect('main_page')

    else:
        form = BotInteractionForm()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)
