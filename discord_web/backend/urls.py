from django.urls import path
from backend.views import view_bot_commands, view_guide, main_page, command_list, registration
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('bot-commands', view_bot_commands, name='viewBotCommands'),
    path('guide', view_guide, name='guide'),
    path('', main_page, name='mainPage'),
    path('command-list', command_list, name="command-list"),

    path('registration', registration, name='user-profile'),
    path('login', auth_views.LoginView.as_view(template_name="backend/login.html"), name="login"),
    path('logout', auth_views.LogoutView.as_view(template_name="backend/logout.html"), name="login"),

]
