# Generated by Django 2.1.1 on 2018-10-02 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_telefone_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=15)),
                ('data_exp', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='clientes',
            name='cpf',
            field=models.OneToOneField(blank=True, null=True, on_delete=0, to='clientes.CPF'),
        ),
    ]
