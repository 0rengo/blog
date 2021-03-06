# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descri\xe7\xe3o')),
                ('ativo', models.BooleanField(default=True, help_text='Se ativo, mostre na tela', verbose_name='Ativo')),
            ],
            options={
                'ordering': ['descricao'],
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
