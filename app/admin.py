from django.contrib import admin
from .models import *

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class UFAdmin(admin.ModelAdmin):
    list_display = ('sigla',)
    search_fields = ('sigla',)
    inlines = [CidadeInline]

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome', 'cidade__nome')

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome', 'cidade__nome')

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome', 'cidade__nome')

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data_emprestimo', 'data_devolucao')
    search_fields = ('usuario__nome',)

admin.site.register(UF, UFAdmin)
admin.site.register(Cidade)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Livros)
admin.site.register(Emprestimo, EmprestimoAdmin)