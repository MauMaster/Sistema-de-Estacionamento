from django.forms import ModelForm
from django import forms
from .models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'

   