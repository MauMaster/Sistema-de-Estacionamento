from django.forms import ModelForm
from django import forms
from .models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'

    def clean(self):
        cleaned_data = super(ContatoForm, self).clean()
        nome = cleaned_data.get('nome')
        email = cleaned_data.get('email')
        if not nome and not email:
            raise forms.ValidationError('Campos obriatorios')