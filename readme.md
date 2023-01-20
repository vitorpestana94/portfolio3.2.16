# PROJETO EVENTEX

Esta pasta refere-se ao código de aula de Vitor Luiz Pestana Pereira Menezes
do curso 'Welcome to The Django' do professor Henrique Bastos.
Em suma, este código é para estudos pois é resultado dos estudos do aluno.

O intuíto deste README.MD é exemplificar uma maneira prática de criar uma 
documentação adequada para meus futuros projetos. Além de ser bom, o código
deve ser facilmente usável por qualquer profissional que vier a trabalhar neste. 
Desta forma, uma documentação adequada faz-se mister para este fim.

Vale ressaltar que uma boa documentação não é aquela que explica cada linha do
código, mas a que com poucos passos entregue ao seu leitor o resultado mais célere
possível e o faça, desta forma, começar a trabalhar naquele código, projeto.

# Como desenvolver?

1. Clone o repositório;
2. Crie um virtualenv com python;
3. Ative o virtual env;
4. Instale as dependências;
5. Configure a instância com o .env;
6. Execute os testes.

```console
git clone git@github:vitorpestana94/portifolio3.2.16 wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

# Como fazer o deploy?

1. Crie uma instância no heroku;
2. Envie as configurações para o heroku;
3. Defina uma SECRET_KEY segura para a instância;
4. Defina DEBUG=False;
5. Configure o serviço de email;
6. Envie o código para o heroku.

```console
heroku create minha_instancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py
#configure o email
git push heroku master --force
```