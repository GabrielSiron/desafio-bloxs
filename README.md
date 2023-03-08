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
$ cd flask-api/
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
$ cd flask-api/
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

# Documentação

Nessa seção, descreverei cada endpoint presente na aplicação, os dados que ele espera e o que ele retorna para o usuário.

## Endpoints de Autenticação

    /signup

#
Endpoint utilizado para realizar cadastro de novos usuários. Um exemplo de BODY possível é o seguinte:

```json
{
	"email": "teste@teste.com",
	"password": "senha",
	"name": "Teste",
	"cpf": "12345678910",
	"birth": "2001-06-19T00:00:00"
}
```

### Validações
- Email e CPF não podem ser duplicados em banco e, caso exista um elemento já cadastrado com alguma das duas informações, a API retorna um texto indicando QUAL CAMPO já foi cadastrado no banco de dados;
- Na ausência de alguma dessas informações, a API retornará um texto indicando QUAL CAMPO não foi preenchido;

#

    /signin

