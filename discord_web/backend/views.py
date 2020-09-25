from django.shortcuts import render, redirect
from backend.backend_services import call_bot_command
from backend.forms import BotInteractionForm


def main_page(request):
    if request.method == 'POST':
        form = BotInteractionForm(request.POST)
        if form.is_valid():
            form.save()
            call_bot_command(command=form.data["command"], data=form.data)
            return redirect('main_page')
    else:
        form = BotInteractionForm()
    context = {
        'form': form
    }

    return render(request, 'index.html', context)
