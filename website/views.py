from django.shortcuts import render, redirect
from .models import Contato


def home(request):
    return render(request, 'website/index.html')


def contato(request):
    mensagem = ''

    if request.method == 'POST':
        try:
            contato = {}
            contato['email'] = request.POST.get('email')
            contato['nome'] = request.POST.get('nome')
            contato['sobrenome'] = request.POST.get('sobrenome')
            contato['cidade'] = request.POST.get('cidade')
            contato['endereco'] = request.POST.get('endereco')
            contato['telefone'] = request.POST.get('telefone')
            contato['cep'] = request.POST.get('cep')
            contato['mensagem'] = request.POST.get('mensagem')

            Contato.objects.create(**contato)

        except Exception as e:
            mensagem = str(e)
        else:
            mensagem = 'Contato realizado com sucesso'

    return render(request, 'website/contato.html', {'mensagem': mensagem})



def servicos(request):
    return render(request, 'website/servicos.html')


def localizacao(request):
    return render(request, 'website/localizacao.html')
