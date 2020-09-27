from django import forms
from backend.models import BotInteraction


class BotInteractionForm(forms.ModelForm):
    class Meta:
        model = BotInteraction
        fields = ['discord_tag', 'command', 'youtube']

    def __init__(self, *args, **kwargs):
        super(BotInteractionForm, self).__init__(*args, **kwargs)
        self.fields['youtube'].label = ''
