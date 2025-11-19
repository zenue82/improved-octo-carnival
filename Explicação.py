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

x = 10 + 20
y = x * 2

Isso se relaciona a:

- Gramáticas Livres de Contexto (GLC)  
- Autômatos com Pilha (AP)  

---

## 4. Fluxo Geral do Compilador

1. **Entrada:** código simples (ex.: `x = 10 + 20;`)
2. **Léxico:** tokens são gerados.
3. **Sintático:** tokens são validados pela pilha.
4. **Resultado:** o programa retorna se a expressão é válida.

---

## 5. Conclusão

Esse mini compilador demonstra na prática como:

- ER e AF reconhecem tokens  
- GLC e AP validam a estrutura  
- Compiladores reais usam exatamente esses modelos teóricos  
