# Generated by Django 2.1.1 on 2018-10-01 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='telefone',
            name='clientes',
            field=models.ForeignKey(default=1, on_delete=0, to='clientes.Cliente'),
            preserve_default=False,
        ),
    ]
