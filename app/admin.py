from django.contrib import admin
from app.models import *

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
    
class LivrosInline(admin.TabularInline):
    model = Livros
    extra = 1

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [LivrosInline]
    
class LivrosInline(admin.TabularInline):
    model = Livros
    extra = 1

class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome', 'cidade__nome')
    inlines = [LivrosInline]
    
class LivrosInline(admin.TabularInline):
    model = Livros
    extra = 1

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome', 'cidade__nome')
    inlines = [LivrosInline]
    
class LivrosInline(admin.TabularInline):
    model = Livros
    extra = 1

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data_emprestimo', 'data_devolucao')
    search_fields = ('usuario__nome',)
    inlines = [LivrosInline]
    

admin.site.register(UF, UFAdmin)
admin.site.register(Cidade)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Livros)
admin.site.register(Emprestimo, EmprestimoAdmin)