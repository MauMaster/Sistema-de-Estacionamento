# Generated by Django 2.1 on 2018-11-23 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movrotativo',
            name='checkout',
            field=models.DateTimeField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movrotativo',
            name='veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Veiculo'),
        ),
    ]