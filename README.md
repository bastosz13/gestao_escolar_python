# gestao_escolar_python
Sistema de Gestão Escolar
Introdução

Este projeto consiste em um sistema simples de gestão escolar desenvolvido em Python. O objetivo do sistema é realizar o cadastro de alunos, armazenar suas notas bimestrais, calcular a média de cada estudante e verificar sua situação acadêmica (Aprovado ou Reprovado).

O sistema utiliza listas, dicionários e funções para organizar os dados e executar as operações necessárias, servindo como prática dos conceitos fundamentais da linguagem Python.

Funcionalidades
Cadastro de alunos.
Armazenamento de quatro notas por aluno.
Cálculo automático da média.
Verificação da situação do aluno.
Geração de relatório contendo:
Nome do aluno;
Notas cadastradas;
Média final;
Situação (Aprovado ou Reprovado).
Requisitos

Para executar o projeto é necessário possuir:

Python 3 instalado no computador;
Editor de código (recomendado: Visual Studio Code).
Como executar o sistema
Abra o arquivo principal do projeto em seu editor de código.
Certifique-se de que o Python está instalado corretamente.
Execute o arquivo principal.

Exemplo pelo terminal:

python nome_do_arquivo.py

ou

python3 nome_do_arquivo.py
O sistema executará os cadastros previamente definidos no código.
Após a execução, será exibido um relatório contendo os dados dos alunos cadastrados.
Estrutura do Projeto

O sistema é composto pelas seguintes funções:

cadastrar_aluno()

Responsável por cadastrar um aluno e armazenar suas informações na lista de alunos.

calcular_media()

Responsável por calcular a média das notas de um aluno.

verificar_aprovacao()

Responsável por verificar se o aluno foi aprovado ou reprovado com base na média calculada.

gerar_relatorio()

Responsável por exibir o relatório final contendo nome, notas, média e situação de todos os alunos cadastrados.

Critério de Aprovação

O sistema considera:

Média maior ou igual a 7,0: Aprovado.
Média menor que 7,0: Reprovado.
Exemplo de Saída

Aluno: Luiz

Notas: [10, 7, 5, 3]

Média: 6.25

Situação: Reprovado

Aluno: João

Notas: [5, 9, 4, 2]

Média: 5.00

Situação: Reprovado

Luiz

Projeto desenvolvido como atividade acadêmica para prática de programação em Python, utilizando funções, listas, dicionários e manipulação de dados.
