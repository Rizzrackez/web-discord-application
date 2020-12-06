from django import forms
from backend.models import BotInteraction, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BotInteractionForm(forms.ModelForm):
    class Meta:
        model = BotInteraction
        fields = ['discord_tag', 'command', 'youtube', 'currency_from', 'currency_to']

    def __init__(self, *args, **kwargs):
        super(BotInteractionForm, self).__init__(*args, **kwargs)
        self.fields['youtube'].label = ''


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['discord_tag']
