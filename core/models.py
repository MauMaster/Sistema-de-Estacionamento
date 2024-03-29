from django.db import models
from django.core.mail import send_mail
import math
import datetime
from django.core.validators import RegexValidator
from django.utils import timezone

STATE_CHOICES = (
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
    ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
    ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
)

PAGO_CHOICES = (
    ('Não', 'Não Pago'),
    ('Sim', 'Pago')
)

SAIDA_CHOICES = (
    ('Não', 'CheckIn'),
    ('Sim', 'CheckOut')
)


class Pessoa(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True,blank=False)
    cpf = models.CharField(unique=True, max_length=11, validators=[
            RegexValidator(
                r'[0-9]',
                'Use somente número',
                'Precisa contar 11'
            ),
        
        ],
        
    )
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    telefone = models.CharField(max_length=20, blank=False)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(default='RS', max_length=2, choices=STATE_CHOICES)

    def __str__(self):
        return str(self.nome) + ' - ' + str(self.email)


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, blank=False)
    modelo = models.CharField(max_length=20, blank=False)
    ano = models.CharField(max_length=7, default="2018")
    placa = models.CharField(max_length=8)
    proprietario = models.ForeignKey(
        Pessoa, on_delete=models.CASCADE, blank=False, )
    cor = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return str(self.modelo) + ' - ' + str(self.placa)+ ' - ' + str(self.proprietario)


class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return 'Parametros Gerais'


class MovRotativo(models.Model):
    checkin = models.DateTimeField(default=timezone.now())
    checkout = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(blank=False)
    placa = models.CharField(max_length=8, blank=False)
    modelo = models.CharField(max_length=15, blank=False)
    valor_hora = models.DecimalField(
        max_digits=5, decimal_places=2, null=False, blank=False)
    pago = models.CharField(max_length=15, choices=PAGO_CHOICES)
    chk = models.CharField(("Situação"), max_length=15,
                           choices=SAIDA_CHOICES, default='Não')

                           

    def horas_total(self):
        if self.checkout is None:
            return self.checkout == 0
        else:
            return math.ceil((self.checkout - self.checkin).total_seconds() / 3600)

    def total(self):
        return self.valor_hora * self.horas_total()

    def save(self, *args, **kwargs):
        if not self.chk == 'Não':
            self.checkout = timezone.now()
        return super(MovRotativo, self).save(*args, **kwargs)

    def send_email(self):
        if self.pago == 'Sim':
            assunto = 'Comprovante pagamento Estacione Aqui 24 Horas'
            mensagem = 'Obrigado por utilizar o Estacione Aqui 24 horas. Seu horário de Chekin foi:  ' + str(self.checkin) + 'Seu horário de Chekou foi:   ' + str(
                self.checkout) + '  Confirmamos o pagamento do valor de: R$' + str(self.total()) + '   E aguardamos seu retorno '
            recipient_list = [self.email]

            send_mail(
                assunto,
                mensagem,
                'estacioneaqui24@gmail.com',
                [recipient_list],
                fail_silently=False,
            )


class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, blank=False)
    inicio = models.DateField(("Início"), default=datetime.date.today)
    validade = models.DateField(("Validade"), blank=False, )
    valor_mes = models.DecimalField(
        max_digits=6, decimal_places=2, blank=False)
    pago = models.CharField(max_length=15, choices=PAGO_CHOICES)
   

    @property
    def email(self):
        return self.veiculo.proprietario.email

    def mensal(self):
        return math.ceil((self.validade - self.inicio).total_seconds() / 86400)

    def total_mes(self):
        return math.ceil(self.mensal() // 30)

    def total_mes_pagar(self):
        return self.valor_mes * self.total_mes()

    def __str__(self):
        return str(self.veiculo) + ' - ' + str(self.inicio)

    def send_email(self):
        if self.pago == 'Sim':
            assunto = 'Comprovante pagamento Estacione Aqui 24 Horas'
            mensagem = 'Obrigado por utilizar o Estacione Aqui 24 horas. Ativação do estacionamento dia :  ' + str(self.inicio) + 'Com validade até o dia   ' + str(
                self.validade) + '  Confirmamos o pagamento do valor de: R$ ' + str(self.total_mes_pagar()) + '   E aguardamos seu retorno '
            recipient_list = [self.email]

            send_mail(
                assunto,
                mensagem,
                'estacioneaqui24@gmail.com',
                [recipient_list],
                fail_silently=False,
            )


class MovMensalista(models.Model):
    mensalista = models.ForeignKey(
        Mensalista, blank=False, on_delete=models.CASCADE)
    dt_pgto = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.mensalista) + ' - ' + str(self.total)
