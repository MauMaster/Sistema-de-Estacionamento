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
        modelo = cleaned_data.get('modelo')
        marca = cleaned_data.get('marca')
        if not modelo and not marca:
            raise forms.ValidationError('Campos obriatorios')


class MovRotativoForm(forms.ModelForm):
    class Meta:
        model = MovRotativo
        fields = '__all__'
       
    def clean(self):
        cleaned_data = super(MovRotativoForm, self).clean()
        checkin = cleaned_data.get('checkin')
        valor_hora = cleaned_data.get('valor_hora')
        if not checkin and not valor_hora:
            raise forms.ValidationError('Campos obriatorios')


class MensalistaForm(forms.ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'
        
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
