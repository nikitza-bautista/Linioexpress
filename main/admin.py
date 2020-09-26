from django.contrib import admin

from .models import Localizacion, Producto, Categoria, Proveedor
#tambien se puede importar todas las clases con *

# Register your models here.
admin.site.register(Localizacion)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)

#username: admin
#email adress: linio_exp@yopmail.com
#se puede entrar despues ahi y ver la bandeja de entrada
#contra es: ru