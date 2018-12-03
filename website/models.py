from django.db import models
from django.core.mail import send_mail


class Contato(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    sobrenome = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    telefone = models.CharField(max_length=20, blank=False)
    endereco = models.CharField(max_length=100, blank=False)
    cidade = models.CharField(max_length=100, blank=False)
    cep = models.CharField(max_length=100, blank=False)
    mensagem = models.TextField(max_length=500, blank=False)
    
    def __str__(self):
        return self.nome

   