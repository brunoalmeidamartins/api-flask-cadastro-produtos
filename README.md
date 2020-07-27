# API Flask para Cadastro de Produtos com Login via JWT

## Para rodar a API na própria máquina
- Tenha o mysql instalado e rodando
- Modifique os parâmetros relacionados ao mysql  no arquivo 'config.py'
- Crie um database com o nome 'flask_api' no mysql
- Instale as bibliotecas requeridas no arquivo 'requirements.txt'
- Use o comando 'python run.py'

## Para rodar a API com docker utilizando o docker-compose
- Rode o comando 'docker-compose up --build -d'
- Aguarde todo o processo de criação
- Para debug retire a flag '-d' do comando acima
- A API estará acessível em: http://IP-MAQUINA:5000 ou http://localhost:5000

## Documentação da API
- Executando na máquina: http://localhost:5000/apidocs
- Executando no docker:   http://IP-MAQUINA:5000/apidocs ou http://localhost:5000/apidocs 

## Banco de Dados
- Caso escolha executar a api utilizando o docker e docker-compose a porta do MYSQL é a 3307
- As credências do banco estão no arquivo config.py

## Rotas públicas da API
- /usuarios METHOD = POST => Utilizada para criar um usuário de acesso a API.
- /login METHOD = POST => Utilizada para efetuar login do usuário criado anteriormente. 

## Rotas privadas da API
- /produtos METHOD = GET => Utilizada para obter a lista de produtos já página.
- /produtos METHOD = POST => Utilizada para criar um produto novo.
- /produtos/<id> METHOD = GET => Utilizada para obter um produto com o id do parâmetro.
- /produtos/<id> METHOD = PUT => Utilizada para editar um produto com o id do parâmetro.
- /produtos/<id> METHOD = DELETE => Utilizada deletar um produto com o id do parâmetro.

## Autenticação das Rotas Privadas
Ao utilizar a rota /login usando um usuário cadastrado no banco de dados, a API lhe responderá com um 'access_token' válido por 5 minutos. Sendo assim, todas as rotas privadas deverá possuir em seu headers o parâmetro 'Authorization' com o valor 'Bearer access_token'
