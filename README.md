# 🛒 Meu E-commerce Simples com Django

Este é um projeto de e-commerce básico e funcional, desenvolvido com o objetivo de demonstrar habilidades em desenvolvimento web full-stack utilizando Python e o framework Django. É uma aplicação robusta, porém simples, ideal para entender os fundamentos de uma loja online.

## ✨ Funcionalidades

O projeto inclui as seguintes funcionalidades chave:

* **Autenticação e Gerenciamento de Usuários:**
    * Cadastro de novos usuários.
    * Login e logout de usuários.
    * Perfis de usuário para gerenciar informações pessoais.
* **Gestão de Produtos:**
    * Listagem de produtos com detalhes.
    * Visualização de variações de produtos (ex: tamanho, cor).
    * **Upload de Imagens:** Capacidade de carregar e exibir imagens para cada produto, proporcionando uma experiência visual rica.
* **Carrinho de Compras:**
    * Adição e remoção de produtos do carrinho.
    * Atualização de quantidades de itens no carrinho.
* **Painel Administrativo:**
    * Utilização do painel de administração nativo do Django para gerenciamento completo de usuários, produtos, pedidos e outras entidades do sistema.

## 🚀 Tecnologias Utilizadas

Este projeto foi construído com as seguintes tecnologias:

* **Backend:**
    * [**Python**](https://www.python.org/) - Linguagem de programação principal.
    * [**Django**](https://www.djangoproject.com/) - Framework web de alto nível para desenvolvimento rápido.
* **Banco de Dados:**
    * **SQLite** - Utilizado como banco de dados padrão para desenvolvimento.
* **Frontend:**
    * [**HTML5**](https://developer.mozilla.org/pt-BR/docs/Web/HTML/HTML5) & [**CSS3**](https://developer.mozilla.org/pt-BR/docs/Web/CSS) - Estrutura e estilização.
    * [**Bootstrap**](https://getbootstrap.com/) - Framework CSS para um design responsivo e moderno.
    * [**Django-Crispy-Forms**](https://django-crispy-forms.readthedocs.io/en/latest/) & [**Crispy-Bootstrap4**](https://pypi.org/project/crispy-bootstrap4/) - Para facilitar a estilização e renderização de formulários com Bootstrap.
* **Manipulação de Imagens:**
    * [**Pillow**](https://python-pillow.org/) - Biblioteca para processamento de imagens (redimensionamento, upload, etc.).
* **Controle de Versão:**
    * [**Git**](https://git-scm.com/) - Sistema de controle de versão distribuído.

## ⚙️ Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar e executar o projeto em sua máquina local:

### Pré-requisitos

Certifique-se de ter o Python (versão 3.9+) e o Git instalados em seu sistema.

### 1. Clonar o Repositório

```bash
git clone [https://github.com/ArnaldoFelipe/e-commerce-django.git](https://github.com/ArnaldoFelipe/e-commerce-django.git)
cd e-commerce-django
2. Criar e Ativar o Ambiente Virtual
É altamente recomendável usar um ambiente virtual para isolar as dependências do projeto.

Bash

# No Windows
python -m venv venv
.\venv\Scripts\activate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Instalar as Dependências
Com o ambiente virtual ativado, instale todas as bibliotecas necessárias:

Bash

pip install Django crispy-forms crispy-bootstrap4 Pillow
# Ou, se você criar um requirements.txt:
# pip install -r requirements.txt
4. Configurar o Banco de Dados
Aplique as migrações para criar as tabelas no banco de dados (SQLite por padrão):

Bash

python manage.py migrate
5. Criar um Superusuário (Opcional, para acessar o Admin)
Para acessar o painel administrativo do Django, crie um superusuário:

Bash

python manage.py createsuperuser
# Siga as instruções no terminal para definir nome de usuário, e-mail e senha.
6. Rodar o Servidor de Desenvolvimento
Inicie o servidor local do Django:

Bash

python manage.py runserver
Agora você pode acessar o projeto no seu navegador em http://127.0.0.1:8000/.
O painel administrativo estará disponível em http://127.0.0.1:8000/admin/.

🤝 Contribuição
Contribuições são bem-vindas! Se você tiver ideias, sugestões ou quiser reportar um bug, sinta-se à vontade para abrir uma issue ou enviar um pull request.

📞 Contato
Arnaldo Felipe - https://www.linkedin.com/in/arnaldo-felipe-da-silva-84b883233/
