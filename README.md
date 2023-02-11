# Desafio | Bloxs

O desafio consiste em criar um sistema que simule um banco digital e que permita ao usuário realizar operações básicas numa conta registrada naquele banco. As operações são:

- Sacar dinheiro da sua conta;
- Depositar dinheiro na sua conta;
- Ver o saldo atual;
- Ver o extrato de sua conta;

## API

A API usada para essa aplicação foi construída com Python Flask e possui alguns pontos a serem destacados. Vamos falar sobre eles!

### Autenticação

O sistema de autenticação dessa aplicação é reduzido, porque não era o objetivo do projeto desenvolver um login completo. Mas o sistema ainda é capaz de verificar se você está autenticado e tem permissão para acessar o que está pedindo.