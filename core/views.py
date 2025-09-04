# Em core/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout 
from django.db.models import Q
from .models import Tarefa 
from .forms import TarefaForm 
from django.shortcuts import render, redirect, get_object_or_404
import matplotlib.pyplot as plt
from django.contrib.auth.models import User

# Imports do Matplotlib na ordem correta
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



@login_required
def home(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()
            return redirect('home')
    else:
        form = TarefaForm()

    tarefas_base = Tarefa.objects.filter(
        Q(usuario=request.user) | Q(atribuido_a=request.user)
    ).distinct()

    status_filtro = request.GET.get('status')

    if status_filtro in ['pendente', 'em_andamento', 'concluida']:
        tarefas = tarefas_base.filter(status=status_filtro)
    else:
        tarefas = tarefas_base

    context = {'tarefas': tarefas, 'form': form}
    return render(request, 'home.html', context)

@login_required
def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, Q(usuario=request.user) | Q(atribuido_a=request.user), id=tarefa_id)
    
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'editar_tarefa.html', {'form': form, 'tarefa': tarefa})


@login_required
def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, Q(usuario=request.user) | Q(atribuido_a=request.user), id=tarefa_id)
    
    if request.method == 'POST':
        tarefa.delete()
        return redirect('home')
    
    return redirect('home') 

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def grafico_tarefas(request):
    users = User.objects.all()
    selected_user_id = request.POST.get('user_id')

    if selected_user_id:
        user_selecionado = get_object_or_404(User, id=selected_user_id)
    else:
        user_selecionado = request.user

    tarefas = Tarefa.objects.filter(
        Q(usuario=user_selecionado) | Q(atribuido_a=user_selecionado)
    ).distinct()

    status_counts = {
        'pendente': tarefas.filter(status='pendente').count(),
        'em_andamento': tarefas.filter(status='em_andamento').count(),
        'concluida': tarefas.filter(status='concluida').count(),
    }

    labels_originais = ['Pendentes', 'Em Andamento', 'Concluídas']
    sizes_originais = [status_counts['pendente'], status_counts['em_andamento'], status_counts['concluida']]
    colors_originais = ['#ffc107', '#0dcaf0', '#198754']

    labels, sizes, colors = [], [], []
    for i, size in enumerate(sizes_originais):
        if size > 0:
            labels.append(labels_originais[i])
            sizes.append(size)
            colors.append(colors_originais[i])

    fig1, ax1 = plt.subplots()

    if not sizes:
        ax1.text(0.5, 0.5, 'Nenhuma tarefa encontrada.', horizontalalignment='center', verticalalignment='center')
        ax1.axis('off')
    else:
        ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')

    plt.title(f'Gráfico de Tarefas para: {user_selecionado.username}')
    plt.savefig('core/static/grafico_tarefas.png')
    plt.close()

    context = {
        'users': users,
        'selected_user': user_selecionado,
        'chart_url': 'grafico_tarefas.png'
    }
    return render(request, 'grafico_tarefas.html', context)

