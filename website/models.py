from django.db import models


class Contato(models.Model):
    email = models.EmailField(blank=False)
    nome = models.CharField(max_length=100, blank=False)
    sobrenome = models.CharField(max_length=100, blank=False)
    endereco = models.CharField(max_length=100, blank=False)
    cidade = models.CharField(max_length=100, blank=False)
    cep = models.CharField(max_length=100, blank=False)
    mensagem = models.TextField(max_length=500, blank=False)
    receber_noticias = models.BooleanField()

    def __str__(self):
        return self.nome


