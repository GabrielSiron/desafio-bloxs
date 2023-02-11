# Desafio | Bloxs

## Instalação

Parte da tarefa está executando corretamente via docker-compose, e começaremos por essa parte.

```
$ docker-compose build

```

Isso fará a instalação de todas as ferramentas necessárias para rodar o frontend da aplicação (em React) e o banco de dados MySQL.

Para rodar a API, será necessário instalar alguns módulos via pip no computador. O projeto tem um requirements.txt, então o processo é simplificado:

```
$ cd flask-api/
$ pip install -r requirements.txt
```

## Rodando o Projeto

Para rodar o frontend e o banco de dados, basta executar o seguinte comando:

```
$ docker-compose up
```

Para rodar o backend, três comandos serão necessários.

### Criando o banco de dados

Para rodar esse comando, o container do Banco de Dados precisa estar no ar. Então, após o comando anterior, execute o seguinte comando:

```
$ python start_db.py
```

Esse comando apaga um banco (caso exista) e cria o banco para a aplicação. Não deve ser executado toda vez, apenas na primeira execução ou toda vez que zerar o banco for útil.

### Criando o usuário com FlaskMigrate

```
$ cd flask-api/
$ python main.py
```

Isso fará as tabelas serem criadas no banco.

Em outra aba do terminal, execute:

```
$ flask db upgrade heads
```

Isso criará um usuário com as seguintes credenciais:

- email: gabriel@gmail.com
- senha: password
  
Os outros dados não são necessários para login. Por definição, toda conta é inicialmente ativa e também automaticamente relacionada ao tipo de conta "Conta Fácil", com limite de saque diário estimado em R$ 1000,00.

## Testando a Aplicação

Agora, todas os serviços necessários já estão no ar. O frontend é acessado a partir da url http://localhost:3000.

### Decisões de projeto

- O bloqueio da conta somente impossibilita SAQUE e não depósito. Essa foi uma decisão baseada no comportamento real de alguns sistemas bancários. Depósito ou transferências recebidas não são bloqueados, apenas saques ou envio de dinheiro.
- Na home, a lista de transações é reduzida (mostra somente as últimas 10). Para ver todas as transações, vá para a Aba "Transações" no menu superior.