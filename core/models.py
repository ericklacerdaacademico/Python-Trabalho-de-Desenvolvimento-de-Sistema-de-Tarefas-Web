from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('pendente', 'Pendente'),
    ('em_andamento', 'Em Andamento'),
    ('concluida', 'Concluída'),
)

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas_criadas')

    atribuido_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tarefas_atribuidas')

    def __str__(self):
        return self.titulo