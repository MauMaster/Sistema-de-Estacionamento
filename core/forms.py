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
    nome = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Nome Completo'}))

    email = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'seuemail@seuservidor.com.br'}))

    endereco = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Rua ou Avenida'}))

    numero = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'número'}))

    bairro = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'seu bairro'}))

    cidade = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'sua cidade'}))
    cpf = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': '0000000000'}))

    telefone = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': '00 00000000'}))

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
    placa = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'AAA-9999'}))

    modelo = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Modelo do carro'}))

    cor = forms.CharField(
        widget=forms.TextInput(
                                attrs={
                                        'placeholder': 'Cor do carro'}))
 
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
    placa = forms.CharField(
            widget=forms.TextInput(
                                    attrs={'placeholder': 'AAA-9999'}))

   

    email = forms.CharField(
            widget=forms.TextInput(
                                    attrs={ 'placeholder': 'seuemail@seuservidor.com.br'}))

    modelo = forms.CharField(
            widget=forms.TextInput(
                                    attrs={ 'placeholder': 'Modelo do carro'}))

    valor_hora = forms.CharField(
            widget=forms.NumberInput(
                                    attrs={ 'placeholder': '0,00'}))
 
  
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
    validade = forms.DateField(
        widget=forms.DateInput( 
                               attrs={
                                      'placeholder': 'xx/xx/xxxx'}))
    valor_mes = forms.DecimalField(
        widget=forms.NumberInput(
                                attrs={
                                        'placeholder': '000,00'}))

    class Meta:
        model = Mensalista
        fields = '__all__'

    def clean(self):
        cleaned_data = super(MensalistaForm, self).clean()
        veiculo = cleaned_data.get('veiculo')
        validade = cleaned_data.get('validade')
        if not veiculo and not validade:
            raise forms.ValidationError('Campos obriatorios')


class MovMensalistaForm(ModelForm):
    class Meta:
        model = MovMensalista
        fields = '__all__'
