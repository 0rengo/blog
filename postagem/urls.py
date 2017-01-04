from django.conf.urls import url
from .views import primeira_pagina, segunda_pagina

urlpatterns = [
	url(r'^$', primeira_pagina, name='primeira_pagina'),
	url(r'^segunda-pagina$', segunda_pagina, name='segunda_pagina')
]