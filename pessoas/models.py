
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(default=18)
    
    def __str__(self):
        return self.nome