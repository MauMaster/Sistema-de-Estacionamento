from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
import json
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib import messages

from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
)

from .forms import (
    PessoaForm,
    VeiculoForm,
    MovRotativoForm,
    MensalistaForm,
    MovMensalistaForm

)

User = get_user_model()


@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

@login_required
def index(request):
    return render(request, 'core/index.html')


@receiver(post_save, sender=MovRotativo)
def before_movrotativo_save(sender, **kwargs):
    print(kwargs)
    instance = kwargs['instance']
    if instance.pago == 'Sim':
        print('Send email')
        instance.send_email()


@receiver(post_save, sender=Mensalista)
def before_mensalista_save(sender, **kwargs):
    print(kwargs)
    instance = kwargs['instance']
    if instance.pago == 'Sim':
        print('Send email')
        instance.send_email()


class home(View):
    def get(sel, request, *args, **kwargs):
        return render(request, 'core/index.html', {"customers": 10})


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)


class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        checkin = MovRotativo.objects.all().count()
        clientes = Pessoa.objects.all().count()
        veiculos = Veiculo.objects.all().count()
        mensalistas = Mensalista.objects.all().count()
        labels = ["Usúario", "Checkin", "clientes", "veiculos", "mensalistas"]
        default_items = [qs_count, checkin, clientes, veiculos, mensalistas]
        data = {
            "labels": labels,
            "default": default_items,

        }
        return Response(data)


@login_required
def dashboard(request):
    mov_rot = MovRotativo.objects.all()
    data = {"mov_rot": mov_rot}
    return render(request, 'core/dashboard.html', data)


@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


@login_required
def pessoa_novo(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Pessoas adicionado com sucesso")
            return redirect('core_lista_pessoas')
    else:
        form = PessoaForm
    return render(request, 'core/lista_pessoas.html', {'form': form})


@login_required
def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro alterado com sucesso")
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


@login_required
def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        messages.success(request, "Cadastro deletado com sucesso")
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoa})


@login_required
def veiculo_novo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Veículo adicionado com sucesso")
            return redirect('core_lista_veiculos')
    else:
        form = VeiculoForm
    return render(request, 'core/lista_veiculos.html', {'form': form})


@login_required
def lista_veiculos(request):
    form = VeiculoForm()
    veiculos = Veiculo.objects.all()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


@login_required
def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Veículo alterado com sucesso")
            return redirect('core_lista_veiculos')

    else:
        return render(request, 'core/update_veiculo.html', data)


@login_required
def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        messages.success(request, "Veículo deletado com sucesso")
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': veiculo})


@login_required
def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'form': form, "mov_rot": mov_rot}
    return render(request, 'core/lista_movrotativos.html', data)


def movrotativos_grafico(request):
    queryset = MovRotativo.objects.all()
    placa = [obj.placa for obj in queryset]
    modelo = [obj.modelo for obj in queryset]

    context = {
        'placa': json.dumps(placa),
        'modelo': json.dumps(modelo),
    }
    return render(request, 'core/dashboard.html', context)


@login_required
def movrotativos_novo(request):
    if request.method == 'POST':
        form = MovRotativoForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Movimento Rotativo adicionado com sucesso")
            return redirect('core_lista_movrotativos')
    else:
        form = MensalistaForm
    return render(request, 'core/lista_movrotativos.html', {'form': form})


@login_required
def movrotativos_update(request, id):
    data = {}
    mov_rotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=mov_rotativo)
    data['mov_rotativo'] = mov_rotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro alterado com sucesso")
            return render(request, 'core/update_movrotativos.html', data)
    else:
        return render(request, 'core/update_movrotativos.html', data)


@login_required
def movrotativos_delete(request, id):
    mov_rotativo = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        mov_rotativo.delete()
        messages.success(request, "Cadastro deletado com sucesso")
        return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/delete_confirm.html',
                      {'obj': mov_rotativo})


@login_required
def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'form': form, 'mensalistas': mensalistas}
    return render(
        request, 'core/lista_mensalistas.html', data)


@login_required
def mensalista_novo(request):
    if request.method == 'POST':
        form = MensalistaForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensalista adicionado com sucesso")
            return redirect('core_lista_mensalista')
    else:
        form = MensalistaForm
    return render(request, 'core/lista_mensalistas.html', {'form': form})


@login_required
def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro alterado com sucesso")
            return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/update_mensalista.html', data)


@login_required
def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        messages.success(request, "Cadastro deletado com sucesso")
        return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mensalista})


@login_required
def lista_movmensalista(request):
    mov_mensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'form': form, 'mov_mensalistas': mov_mensalistas}
    return render(
        request, 'core/lista_movmensalistas.html', data)


@login_required
def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalista')


@login_required
def movmensalista_update(request, id):
    data = {}
    mov_mensalista = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=mov_mensalista)
    data['mov_mensalista'] = mov_mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalista')
    else:
        return render(request, 'core/update_movmensalista.html', data)


@login_required
def movmensalista_delete(request, id):
    mov_mensalista = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        mov_mensalista.delete()
        messages.success(request, "Cadastro deletado com sucesso")
        return redirect('core_lista_movmensalista')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mov_mensalista})
