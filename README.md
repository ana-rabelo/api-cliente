## Sobre o Projeto
Este projeto foi desenvolvido com o [curso API com Django 3](https://cursos.alura.com.br/course/api-django-3-validacoes-buscas-filtros-deploy/) e aborda validações, buscas, filtros e deploy. Foram utilizadas técnicas de inclusão de validações nos modelos e serializers, além de como lidar com mensagens de erro. Também foi incluído o uso de paginação, ordenação, buscas e filtros nos endpoints da API.

O projeto desenvolvido consiste em uma lista de clientes, com campos como nome, email, CPF, RG, celular e uma flag para indicar se o cliente está ativo ou não na API. Será necessário realizar autenticação para acessar os dados da API, garantindo assim a segurança das informações.

## Executando o Projeto
Este projeto é uma API desenvolvida utilizando o Django Rest Framework. Para executá-lo, siga os passos abaixo:

### Configuração do Ambiente
Certifique-se de ter o Python e o pip instalado em sua máquina. Caso não tenha, você pode baixá-lo em <https://www.python.org/>. O pip pode ser instalado com o seguinte comando:

```python get-pip.py```

Crie um ambiente virtual para o projeto. Você pode fazer isso utilizando o comando:

```python -m venv nome_do_ambiente```

Ative o ambiente virtual. No Windows, utilize o comando:

```nome_do_ambiente\Scripts\activate```

No MacOS e Linux, utilize o comando:

```source nome_do_ambiente/bin/activate```

Instale as dependências do projeto utilizando o comando:

```pip install -r requirements.txt```

### Executando a Aplicação
Após instalar as dependências, migre as alterações para o banco de dados utilizando os comandos:

```python manage.py makemigrations```

```python manage.py migrate```

Inicie o servidor de desenvolvimento com o comando:

```python manage.py runserver```

Acesse a aplicação em seu navegador utilizando o endereço:

```
http://localhost:8000
```

Agora o projeto está em execução e pronto para ser utilizado!