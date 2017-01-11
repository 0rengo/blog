# coding: utf-8
from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify

class Categoria(models.Model):
	descricao = models.CharField(u'Descrição', max_length=100)
	ativo = models.BooleanField('Ativo', default = True, help_text =u'Se ativo, mostre a categoria na tela')

	def __unicode__(self):
		return self.descricao

	class Meta:
		ordering = ['descricao']
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'


class Postagem(models.Model):
	titulo = models.CharField(u'Titulo', max_length=100)
	data_postagem = models.DateTimeField(u'Data da postagem', auto_now_add=True)
	texto = models.TextField(u'Texto')
	categorias = models.ManyToManyField(Categoria)
	slug = models.SlugField(u'slug', max_length=180, blank=True, editable=False, unique=True, help_text=u'URL amigável')
	ativo = models.BooleanField('Ativo', default=True, help_text=u'Se ativo, publica a postagem no site.')

	def __unicode__(self):
		return self.titulo

	class Meta:
		ordering = ['-data_postagem']
		verbose_name = 'Postagem'
		verbose_name_plural = 'Postagens'

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo)
		super(Postagem, self).save(*args, **kwargs)

