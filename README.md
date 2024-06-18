# Challenge - Tech Mahindra - Python

Este repositório faz parte das entregas do Challenge da Tech Mahindra do curso de engenharia de software na FIAP ( 2024 ).

A entrega é correspondente à matéria de Computational Thinking with Python.

## Alunos Participantes

- Douglas dos Santos Melo - RM: 556439
- Gabriel Danius Fachetti Barbosa - RM: 555747
- Henrique Borges de Castro Sanches - RM: 557959
- Matheus Marcelino Dantas da Silva - RM: 556332
- Vitor Chaves de Lima Coelho - RM: 557067

## Detalhes do projeto

O projeto consiste em uma API que possuí um fluxo de autenticação baseado em e-mail e senha, um processo de autorização baseado em roles e também um sistema de definição de pontos. Esta API possui cinco endpoints, que serão detalhados na seção de [instruções de uso](#instruções-de-uso).

## Instruções de Uso

A API possuí 5 endpoints:

### **/api/auth/sign-up**
- Método: **POST** 
- Descrição: Cadastra um novo usuário

O body desta requisição possuí o seguinte modelo, é necessário que o tipo da requisição seja **application/json**.

```json
{
    "email": "email@gmail.com",
    "password": "test123",
    "passwordConfirm": "test123"
}
```

- **OBS:** A senha deve ter no mínimo 8 characteres
- **OBS2:** Todos os usuários cadastrados possuem a role **user**

### **/api/auth/sign-in**
- Método: **POST** 
- Descrição: Cria uma sessão para um usuário (Login)

O body desta requisição possuí o seguinte modelo, é necessário que o tipo da requisição seja **application/json**.

```json
{
    "email": "email@gmail.com",
    "password": "test123",
}
```

A resposta deste endpoint possuí o seguinte modelo:

```json
{
  "access_token": "string", // Token de acesso.
  "refresh_token": "string", // Refresh token.
  "access_token_expires_at": 0 // Duração do token de acesso ( Segundos ).
}
```

### **/api/auth/refresh**
- Método: **POST** 
- Descrição: Gera um novo token de acesso

O body desta requisição possuí o seguinte modelo, é necessário que o tipo da requisição seja **application/json**.

```json
{
  "refreshToken": "string" // Refresh token válido
}
```

A resposta deste endpoint possuí o seguinte modelo:

```json
{
  "access_token": "string", // Token de acesso.
  "access_token_expires_at": 0 // Duração do token de acesso ( Segundos ).
}
```

### **/api/points**
- Método: **GET** 
- Descrição: Lista os pontos obtidos por um usuário

A resposta deste endpoint possuí o seguinte modelo:

```json
{
  "data": [
    {
      "id": "7714f8b2-c4f6-44c8-bebd-a65803a55ace",
      "amount": 1000,
      "created_at": "2024-06-18T00:33:14"
    },
  ]
}
```

**OBS:** É necessário estar autenticado como um usuário comum para acessar este endpoint

### **/api/points**
- Método: **POST** 
- Descrição: Adiciona pontos para um usuário

O body desta requisição possuí o seguinte modelo, é necessário que o tipo da requisição seja **application/json**.

```json
{
  "userEmail": "string",
  "amount": 0
}
```

**OBS:** É necessário estar autenticado como um administrador para acessar este endpoint

## Instalação de dependências e execução

O projeto possuí algumas dependências e para a sua execução precisamos instalá-las. A melhor forma de fazer isto é criar um virtual env do python.

```cmd
python -m venv venv
```

Após a criação do virtual env devemos ativá-lo e instalar as dependências utilizando os dois comandos abaixo.


```cmd
./venv/Scripts/activate # Ativa o virtual env
pip install -r requirements.txt # Instala as dependências
``` 

Após a instalação das dependências o projeto pode ser executado utilizando o comando abaixo:
```
fastapi dev
```

## Como utilizar a API?

É possível acessar o swagger da api utilizando a seguinte URL:

```
http://localhost:8000/docs
```