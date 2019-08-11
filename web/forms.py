from django import forms
from .models import Request

class MainForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('photo', 'ip', )