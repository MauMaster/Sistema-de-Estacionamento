from django.forms import ModelForm
from django import forms
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
)


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

    def clean(self):
        cleaned_data = super(PessoaForm, self).clean()
        nome = cleaned_data.get('nome')
        email = cleaned_data.get('email')
        if not nome and not email:
            raise forms.ValidationError('Campos obriatorios')


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'

    def clean(self):
        cleaned_data = super(VeiculoForm, self).clean()
        marca = cleaned_data.get('marca')
        modelo = cleaned_data.get('modelo')
        if not marca and not modelo:
            raise forms.ValidationError('Campos obriatorios')


class MovRotativoForm(ModelForm):
    class Meta:
        model = MovRotativo
        fields = '__all__'


class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'
        widgets = {
            'inicio': forms.DateInput(attrs={'class':'datepicker'}),
        }
       

    def clean(self):
        cleaned_data = super(MensalistaForm, self).clean()
        veiculo = cleaned_data.get('veiculo')
        proprietario = cleaned_data.get('proprietario')
        if not veiculo and not proprietario:
            raise forms.ValidationError('Campos obriatorios')


class MovMensalistaForm(ModelForm):
    class Meta:
        model = MovMensalista
        fields = '__all__'
