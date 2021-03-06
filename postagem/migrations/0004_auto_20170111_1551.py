# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postagem', '0003_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('data_postagem', models.DateTimeField(auto_now_add=True, verbose_name='Data da postagem')),
                ('texto', models.TextField(verbose_name='Texto')),
                ('slug', models.SlugField(blank=True, editable=False, help_text='URL amig\xe1vel', max_length=180, unique=True, verbose_name='slug')),
                ('ativo', models.BooleanField(default=True, help_text='Se ativo, publica a postagem no site.', verbose_name='Ativo')),
            ],
            options={
                'ordering': ['-data_postagem'],
                'verbose_name': 'Postagem',
                'verbose_name_plural': 'Postagens',
            },
        ),
        migrations.AlterField(
            model_name='categoria',
            name='ativo',
            field=models.BooleanField(default=True, help_text='Se ativo, mostre a categoria na tela', verbose_name='Ativo'),
        ),
        migrations.AddField(
            model_name='postagem',
            name='categorias',
            field=models.ManyToManyField(to='postagem.Categoria'),
        ),
    ]
