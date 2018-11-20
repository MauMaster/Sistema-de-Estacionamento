from django.db import models


class Contato(models.Model):
    email = models.EmailField()
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    mensagem = models.TextField()
    receber_noticias = models.BooleanField()

    def __str__(self):
        return self.nome


