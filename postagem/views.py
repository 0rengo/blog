from django.shortcuts import render

# Create your views here.
def primeira_pagina(request):
	nome = 'Gilberto Orengo'
	metodo = request.method
	alunos = []
	# alunos = [
	# 	'Ana',
	# 	'Pedro',
	# 	'Maria'
	# 	]
	return render(request, 'postagem/primeira_pagina.html',{'nome': nome, 'metodo': metodo, 'alunos': alunos})

def segunda_pagina(request):
	return render(request, 'postagem/segunda_pagina.html')