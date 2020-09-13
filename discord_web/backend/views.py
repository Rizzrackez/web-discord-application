from django.shortcuts import render, redirect
from backend.forms import BotInteractionForm


def main_page(request):
    form = BotInteractionForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('main_page')

    else:
        form = BotInteractionForm()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)
