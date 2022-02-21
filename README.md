# Trio-Tech.github.io

## O que é a Trio-Tech?

A Trio-Tech é uma empresa fictícia de desenvolvimento de software criada como projeto final da disciplina de Gerência e Configuração de Mudanças do IFPB - Campus Cajazeiras no curso de Análise e Desenvolvimento de Sistemas, segundo período.

## Qual o objetivo da empresa?

Em nosso website, usuários podem se cadastrar e criar pedidos de software, que serão analisados pela nossa equipe, podendo ser aceitos ou não, além de comentados.

## Como usar o projeto?

### Acessando nosso site

> Usuários interessados podem acessar ao nosso website seguindo seguinte link: https://trio-tech.herokuapp.com/

### Rodando o projeto localmente

#### Ambientes Linux (Ubuntu)

- Faça um clone do repositório: ```$ git clone https://github.com/Trio-Tech/Trio-Tech.github.io.git```
- Entre na pasta **backend**
- Instale o python: ```$ sudo apt install python3 python3-venv python3-pip```
- Crie um ambiente virtual Python e o ative: ```$ python3 -m venv env``` seguido por ```$ source env/bin/activate```

#### Ambientes Windows

- Faça um clone do repositório: ```$ git clone https://github.com/Trio-Tech/Trio-Tech.github.io.git```
- Entre na pasta **backend**
- Instale o python: https://www.python.org/ (Lembre de marcar pra adicionar o Python ao path)
- Crie um ambiente virtual Python e o ative: ```$ python -m venv env``` seguido por ```$ env\Scripts\activate```

#### Os proximos passos são comuns para ambos os ambientes

- Instale as dependencias do projeto: ```$ pip install -r requirements.txt```
- Faça as migrações e envie para o BD: ```$ python manage.py makemigrations``` e ```$ python manage.py migrate```
- Rode o projeto: ```$ python manage.py runserver``` que ficará localmente hosteado no endereço: http://localhost:8000

## Contribuindo

- Faça um fork do projeto
- Crie uma nova branch para a sua feature ```$ git checkout -b feature/sua-feature```
- Faça as alterações e dê push ```$ git push origin feature/sua-feature```
- Abra um pull-request para adicionar suas mudanças na branch master/main

## Quem mantém e contribui com o projeto

&nbsp;&nbsp;<span><img src="https://avatars.githubusercontent.com/u/62016873?v=4" width="200" height="200" /></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<span><img src="https://avatars.githubusercontent.com/u/87048683?v=4" width="200" height="200" /></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<span><img src="https://avatars.githubusercontent.com/u/91159124?v=4" width="200" height="200" /></span>

[Ives](https://github.com/ivesfg1) (Back-End Developer) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Samira](https://github.com/DevSamira) (Front-End Developer) &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp; [Jonathas](https://github.com/jwnathas) (Front-End Developer)
