from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Receitas

# Register your models here.
class ListandoReceitas(admin.ModelAdmin):#habilitando edição do admin 
    list_display = ('id', 'nome_receita', 'categoria','tempo_preparo')  
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_per_page = 5

admin.site.register(Receitas, ListandoReceitas)