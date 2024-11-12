from django.db import models

# Create your models here.

class UF(models.Model):
    sigla=models.CharField(max_length=2)
    
    class Meta: 
        verbose_name = 'Unidade Federativa'
        verbose_name_plural = 'Unidades Federais'
        
    def __str__(self):
        return self.sigla
    
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.uf}"


class Genero(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

#Super classe de 'Pessoa', que será uma classe pai para PessoaFisica e PessoaJuridica

class Pessoa(models.Model):
    nome = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, default='')
    telefone = models.IntegerField(default=0)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.nome
    
class PessoaFisica(Pessoa):
    cpf = models.IntegerField(default=0)
    data_nasc = models.DateField(default='2000-01-01')
    
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.nome
    
    
class PessoaJuridica(Pessoa):
    cnpj = models.IntegerField(default=0)
    razao_social = models.CharField(max_length=200, default='')
    data_fundacao = models.DateField(default='2000-01-01')
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.nome
    
class Autor(PessoaFisica):
    pass

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        
class Editora(PessoaJuridica):
    site = models.CharField()
    
    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
        
        
class Usuario(PessoaFisica):    
    pass

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
        
class Genero(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
    
    def __str__(self):
        return self.nome
        
class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(blank=True, null=True, default='2000-01-01')
    data_devolucao = models.DateField( blank=True, null=True, default='2000-01-01')
    
    class Meta:
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'
    
    def __str__(self):
        return f"Emprestimo de {self.usuario} em {self.data_emprestimo}"

        
class Livros(models.Model):
    nome = models.CharField(max_length=255, verbose_name = 'Nome do livro:')
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
    
    def __str__(self):
        return self.nome





