# Explicação do Código — Mini Compilador

Este documento explica como funciona o mini compilador implementado em Python, relacionando cada parte aos conceitos de linguagens formais.

---

## 1. Análise Léxica

O analisador léxico identifica *tokens* usando expressões regulares.  
Cada token corresponde a um elemento da linguagem: números, identificadores, operadores etc.

Isso está diretamente relacionado a:

- Linguagens Regulares  
- Expressões Regulares  
- Autômatos Finitos  

---

## 2. Tabela de Tokens

| Tipo | Exemplo | Teoria |
|------|---------|--------|
| NUM | `10` | ER + AF |
| ID | `x`, `variavel` | ER |
| OP | `+ - * / =` | AF |
| DELIM | `; ,` | AF |

---

## 3. Análise Sintática

A análise sintática é feita usando uma **pilha**, simulando o funcionamento básico de um **Autômato com Pilha (AP)**.

Ele valida expressões como:

