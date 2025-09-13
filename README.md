# Sistema de Gerenciamento de Tarefas Web

## Sobre o Projeto

Este projeto foi desenvolvido para a disciplina de "Tópicos Especiais em Software". Trata-se de uma aplicação web em Python com Django que simula um sistema de gerenciamento de tarefas, permitindo que usuários se cadastrem, criem, editem, visualizem e excluam suas próprias tarefas.

---

## Tecnologias Utilizadas
* Python
* Django
* HTML
* Bootstrap 5
* SQLite (banco de dados padrão)
* Matplotlib

---

## Como Executar o Projeto

Siga os passos abaixo para rodar o projeto em sua máquina local.

**1. Clone o repositório:**
```bash
git clone (https://github.com/ericklacerdaacademico/Python-Trabalho-de-Desenvolvimento-de-Sistema-de-Tarefas-Web.git)
cd (caminho aonde foi gerado o git clone)
```

**2. Crie e ative um ambiente virtual:**
```bash
# Windows
python -m venv venv
.\venv\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Aplique as migrações do banco de dados:**
```bash
python manage.py migrate
```

**5. Crie um superusuário para acessar o painel de admin:**
```bash
python manage.py createsuperuser
```
(Siga as instruções para criar um usuário e senha)

**6. Execute o servidor de desenvolvimento:**
```bash
python manage.py runserver
```
A aplicação estará disponível em `http://127.0.0.1:8000/`.

---

## Uso

- **Cadastro:** Acesse a aplicação e crie uma nova conta na página de **Cadastro**. Para testar as funcionalidades de colaboração, é recomendado criar pelo menos duas contas de usuário.

- **Login:** Faça **Login** com suas credenciais.

- **Dashboard Principal:**
    - **Adicionar Tarefas:** No formulário à esquerda, adicione novas tarefas. Use o campo "Atribuir a" para delegar a tarefa a outro usuário do sistema.
    - **Visualização:** A sua lista de tarefas mostrará tanto as tarefas que você criou quanto as que outros usuários atribuíram a você.
    - **Filtros:** Use os botões "Pendentes", "Em Andamento" e "Concluídas" para filtrar a lista de tarefas por status.
    - **Gerenciamento:** Você pode **Editar** ou **Excluir** qualquer tarefa que você criou ou que foi atribuída a você.

- **Relatório Visual:**
    - Acesse a página de **Relatório** através do link no menu de navegação.
    - Selecione um usuário na lista e clique em "Filtrar" para ver um gráfico de pizza com a distribuição de suas tarefas por status.
---

## Autores
* Erick Borges
