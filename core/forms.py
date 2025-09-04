# Em core/forms.py

from django import forms
from .models import Tarefa, User 

class TarefaForm(forms.ModelForm):
    atribuido_a = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        required=False, 
        label="Atribuir a"
    )

    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'status', 'atribuido_a'] 
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }