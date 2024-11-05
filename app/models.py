from django.db import models

# Create your models here.

class UF(models.Model):
    sigla=models.CharField(max_length=2)
    
    class Meta: 
        verbose_name = 'Unidade Federativa'
        verbose_name_plural = 'Unidades Federais'
        
    def __str__(self):
        return self.sigla