from django.db import models
import math


class Pessoa(models.Model):
    nome = models.CharField(max_length=25, blank=False)
    email = models.EmailField(blank=False)
    cpf = models.CharField(max_length=20, unique=True, blank=False)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    telefone = models.CharField(max_length=20, blank=False)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)

    
    def __str__(self):
        return self.nome


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, blank=False)
    modelo = models.CharField(max_length=20, blank=False)
    ano = models.CharField(max_length=7)
    placa = models.CharField(max_length=7)
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=False)
    cor = models.CharField(max_length=15, blank=False)
    observacoes = models.TextField(blank=False)
        
    def __str__(self):
        return self.modelo + ' - ' + self.placa


class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return 'Parametros Gerais'


class MovRotativo(models.Model):
    checkin = models.DateTimeField(auto_now=True)
    checkout = models.DateTimeField(auto_now=False, null=True, blank=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, blank=False)
    pago = models.BooleanField(default=False)

    def horas_total(self):
        return math.ceil((self.checkout - self.checkin).total_seconds() / 3600)

    def total(self):
        return self.valor_hora * self.horas_total()

    def __str__(self):
        return self.veiculo.placa


class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, blank=False)
    inicio = models.DateField(blank=False)
    validade = models.DateField(blank=False)
    proprietario = models.ForeignKey(Pessoa, blank=False, on_delete=models.CASCADE)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    pago = models.BooleanField(default=False)
    

    def mensal(self):
        return math.ceil((self.validade - self.inicio).total_seconds() / 86400)

    
    def total_mes(self):
        return math.ceil(self.mensal() // 30)

    def total_mes_pagar(self):
        return self.valor_mes * self.total_mes()
        
    def __str__(self):
        return str(self.veiculo) + ' - ' + str(self.inicio)


class MovMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista, blank=False, on_delete=models.CASCADE)
    dt_pgto = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.mensalista) + ' - ' + str(self.total)