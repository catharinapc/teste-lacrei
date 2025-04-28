from django.db import models
from django.utils import timezone

class Profissional(models.Model):
    nome_social = models.CharField(max_length=255)
    profissao = models.CharField(max_length=255)
    endereco = models.TextField()
    contato = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_social

class Consulta(models.Model):
    paciente_nome = models.CharField(max_length=255)  
    data = models.DateField()      
    horario = models.TimeField(default=timezone.now)  
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, related_name="consultas")

    def __str__(self):
        return f"Consulta com {self.profissional.nome_social} em {self.data}"
    


    def __str__(self):
        return self.nome
