from django import forms
from backend.models import BotInteraction


class BotInteractionForm(forms.ModelForm):
    class Meta:
        model = BotInteraction
        fields = ['discord_tag', 'command']
