# Projeto Cadastro de Clientes - Python Tkinter & SQLite

## Descrição

Este projeto é uma aplicação desktop simples para gerenciamento de clientes, desenvolvida em Python utilizando a biblioteca **Tkinter** para interface gráfica e **SQLite** para persistência dos dados. 

A aplicação permite inserir, visualizar, buscar, atualizar e deletar registros de clientes, com campos para nome, sobrenome, email e CPF.

---

## Funcionalidades

- **Cadastrar clientes:** Insira nome, sobrenome, email e CPF de novos clientes.
- **Visualizar clientes:** Liste todos os clientes cadastrados no banco.
- **Buscar clientes:** Pesquise clientes por qualquer um dos campos.
- **Atualizar clientes:** Modifique informações de clientes existentes.
- **Excluir clientes:** Apague clientes selecionados da base de dados.

---

## Estrutura do Projeto

### backend.py:
- Responsável por toda a comunicação com o banco de dados SQLite.
- Contém a classe `TransactionObject` para gerenciar conexões e executar comandos SQL, além das funções para CRUD (Create, Read, Update, Delete).
  
### Aplicacao.py:
- Define a interface gráfica usando Tkinter.
- Campos para entrada de dados, lista para mostrar os clientes.
- Botões conectados aos comandos do backend para realizar as operações no banco.
- Evento de seleção na lista para carregar dados nos campos para edição ou exclusão.

### clientes.db:
- Arquivo SQLite onde os dados são armazenados localmente.

