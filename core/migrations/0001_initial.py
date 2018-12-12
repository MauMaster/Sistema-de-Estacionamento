# Generated by Django 2.1.4 on 2018-12-12 00:01

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mensalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField(default=datetime.date.today, verbose_name='Início')),
                ('validade', models.DateField(verbose_name='Validade')),
                ('valor_mes', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pago', models.CharField(choices=[('Não', 'Não Pago'), ('Sim', 'Pago')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='MovMensalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_pgto', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('mensalista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Mensalista')),
            ],
        ),
        migrations.CreateModel(
            name='MovRotativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateTimeField(default=datetime.datetime(2018, 12, 12, 0, 1, 26, 348705, tzinfo=utc))),
                ('checkout', models.DateTimeField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('placa', models.CharField(max_length=7)),
                ('modelo', models.CharField(max_length=15)),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pago', models.CharField(choices=[('Não', 'Não Pago'), ('Sim', 'Pago')], max_length=15)),
                ('chk', models.CharField(choices=[('Não', 'CheckIn'), ('Sim', 'CheckOut')], default='Não', max_length=15, verbose_name='Situação')),
            ],
        ),
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_mes', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('[0-9]', 'Use somente número', 'Precisa contar 11')])),
                ('endereco', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=20)),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=20)),
                ('ano', models.CharField(default='2018', max_length=7)),
                ('placa', models.CharField(max_length=7)),
                ('cor', models.CharField(max_length=15)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Marca')),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='mensalista',
            name='veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Veiculo'),
        ),
    ]
