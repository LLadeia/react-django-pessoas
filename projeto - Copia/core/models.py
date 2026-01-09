from django.db import models

def upload_to(instance, filename):
    return 'file_pessoa/{filename}'.format(filename=filename)

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    curso = models.CharField(max_length=100)
    periodo = models.IntegerField()
    opiniao = models.TextField()
    foto = models.ImageField(upload_to='pessoas/', null=True, blank=True)


    def __str__(self):
        return self.nome
    
# Create your models here.
