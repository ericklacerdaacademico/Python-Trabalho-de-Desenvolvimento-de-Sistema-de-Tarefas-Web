from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tarefa/<int:tarefa_id>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefa/<int:tarefa_id>/excluir/', views.excluir_tarefa, name='excluir_tarefa'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('cadastro/', views.register, name='register'),
    path('grafico/', views.grafico_tarefas, name='grafico_tarefas')
]