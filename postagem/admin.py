from django.contrib import admin

from .models import Categoria, Postagem

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ['descricao', 'ativo']
	search_fields = ['descricao']

admin.site.register(Categoria, CategoriaAdmin)


class PostagemAdmin(admin.ModelAdmin):
	list_display = ['titulo', 'data_postagem', 'ativo']
	search_fields = ['titulo']

admin.site.register(Postagem, PostagemAdmin)