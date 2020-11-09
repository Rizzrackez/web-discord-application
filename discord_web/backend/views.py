from django.shortcuts import render, redirect
from backend.backend_services import call_bot_command
from backend.forms import BotInteractionForm, UserProfileForm, UserRegisterForm
from backend.models import *


def main_page(request):
    return render(request, 'backend/mainPage.html')


def view_bot_commands(request):
    try:
        userProfile = UserProfile.objects.get(user=request.user).discord_tag
    except:
        userProfile = ""
    if request.method == 'POST':
        form = BotInteractionForm(request.POST)
        if form.is_valid():
            form.save()
            call_bot_command(command=form.data["command"], data=form.data)
            return redirect('viewBotCommands')
    else:

        form = BotInteractionForm()
    context = {
        'form': form,
        'userProfileTag': userProfile
    }

    return render(request, 'backend/viewBotCommands.html', context)


def view_guide(request):
    context = {}
    return render(request, 'backend/guide.html', context)


def command_list(request):
    context = {}
    return render(request, 'backend/commandList.html', context)


def registration(request):

    if request.method == 'POST':
        user_profile_form = UserProfileForm(request.POST)

        if user_profile_form.is_valid():
            user_profile = user_profile_form.save()

        user_creation_form = UserRegisterForm(request.POST)

        if user_creation_form.is_valid():
            user = user_creation_form.save()
            user_profile.user = user
            user_profile.save()

            return redirect('mainPage')

    else:
        user_profile_form = UserProfileForm()
        user_creation_form = UserRegisterForm()

    context = {
        'user_profile_form': user_profile_form,
        'user_creation_form': user_creation_form,
    }

    return render(request, 'backend/registration.html', context)
