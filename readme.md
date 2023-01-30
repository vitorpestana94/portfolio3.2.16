# PROJETO EVENTEX

Esta pasta refere-se ao código de aula de Vitor Luiz Pestana Pereira Menezes do curso 'Welcome to The Django' do professor Henrique Bastos. Em suma, este é um código de estudos pois é resultado da investigação acerca da framework "django" realizada pelo aluno com a orientação do mentor e da comunidade "HBnetwork". Desta maneira, faz-se mister notar que esta pasta está em constante construção e é apenas é usada como portfólio temporário, uma vez que o site final ainda está em desenvolvimento.

O intuíto deste "README.MD" é exemplificar como criar uma documentação adequada e prática para meus futuros projetos. Não basta ao código ser funcional. Além de disto, deve ser de fácil manutenção por qualquer profissional que vier a trabalhar neste. Destarte, uma documentação adequada faz-se necessária para este fim.

Vale ressaltar que uma boa documentação não é aquela que explica cada linha do código, mas a que com poucos passos entregue ao seu leitor o resultado mais célere possível.Fazendo-o, desta forma, começar a trabalhar naquele projeto imediatamente.

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