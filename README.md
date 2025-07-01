# Atividade Prática de Estrutura de Dados 🎲  

Esse repositório foi criado para armazenar os exercícios desenvolvidos durante os meus estudos sobre estrutura de dados e algoritmos.

## Objetivo da Questão 01 ✅  

O objetivo da primeira questão é desenvolver um sistema de triagem de pacientes em uma clínica utilizando uma **lista encadeada simples**, onde os pacientes são classificados por prioridade de atendimento com base na cor de seu cartão (amarelo ou verde).  

### 🏥 Regras da Triagem:
- Pacientes com cartão **amarelo (A)** têm prioridade sobre os com cartão **verde (V)**.
- Entre pacientes com a **mesma cor**, o atendimento é feito em ordem **numérica crescente** dos cartões.
- A numeração dos cartões **amarelos** inicia em **201**.
- A numeração dos cartões **verdes** inicia em **1**.

### 🔧 Funcionalidades implementadas:
- Inserção de pacientes com e sem prioridade.
- Impressão da lista de espera.
- Chamada do próximo paciente para atendimento.
- Menu interativo com opções:
  1. Adicionar paciente à fila  
  2. Mostrar pacientes na fila  
  3. Chamar paciente  
  4. Sair do programa

A estrutura de dados utilizada foi uma **lista encadeada simples**, onde cada nó representa um paciente contendo:
- Número do cartão
- Cor do cartão (A ou V)
- Ponteiro para o próximo paciente


---

## Objetivo da Questão 02 ✅  

A segunda questão consiste na criação de uma **Tabela Hash com endereçamento em cadeia** para representar um sistema de emplacamento de veículos, onde o **último número da placa** indica o **estado de registro** do veículo.

### 🧮 Regras da função hash:
- A entrada é uma sigla de estado (ex: `"RS"`, `"SP"`, `"DF"`).
- Se a sigla for `"DF"`, a posição retornada é sempre **7**.
- Para os demais estados:  
  `Índice = (ord(primeira_letra) + ord(segunda_letra)) % 10`

### 🗂 Estrutura da Tabela Hash:
- 10 posições (de 0 a 9), cada uma com uma **lista encadeada**.
- Cada nó representa um estado e contém:
  - Sigla do estado
  - Nome completo do estado
  - Ponteiro para o próximo

### 🔧 Funcionalidades implementadas:
- Inserção no início da lista encadeada de cada posição da tabela.
- Impressão da tabela hash com os estados organizados por posição.
- Inserção:
  - Dos **26 estados brasileiros**
  - Do **Distrito Federal**
