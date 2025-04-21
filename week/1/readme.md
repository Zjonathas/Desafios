# 🔐 Desafio 1: Sugeridor de Senhas Inteligente

## 🧠 Contexto

A empresa **SecureMind**, especializada em educação digital e cibersegurança acessível, está desenvolvendo uma série de **ferramentas educativas interativas** para conscientizar usuários comuns sobre práticas seguras na internet.

Um dos maiores problemas enfrentados por empresas e usuários é o uso de **senhas fracas e previsíveis**, como `123456`, `senha`, `admin`, ou `meunome123`. Esse hábito coloca **sistemas pessoais e corporativos em risco**, sendo uma das principais causas de vazamentos de dados.

---

## 💡 Desafio

A equipe da SecureMind deseja lançar um mini-aplicativo que ajude o usuário a **reforçar senhas fracas** a partir de frases simples — como nomes, datas ou senhas comuns — utilizando técnicas básicas de **obfuscação e substituição criativa**.

O objetivo é ajudar as pessoas a:

- Tornar suas senhas mais seguras, mantendo **fácil memorização**.
- Aprender boas práticas de segurança **de forma lúdica e prática**.
- Adquirir consciência sobre o risco de usar senhas previsíveis.

---

## 🛠️ Especificações da Tarefa

Você deve criar um algoritmo na linguagem de sua escolha que execute os seguintes passos no terminal:

1. Receba uma **frase simples ou senha fraca** digitada pelo usuário.
2. Gere **sugestões de versões mais seguras**, utilizando técnicas como:
   - 🔄 **Senha invertida** – Inverte os caracteres da frase.
   - 🔠 **Senha em caixa alta** – Transforma toda a frase para letras maiúsculas.
   - 🔇 **Modo "sem vogais"** – Remove todas as vogais (para dificultar ataques por dicionário).
   - 🔐 **Modo "cifrado"**
  
Entrada:
Insira a senha: minhasenha123
Saída:
Original: minhasenha123
Invertida: 321ahnesahnim
Caixa Alta: MINHASENHA123
Sem Vogais: mnhsnh123
Cifrada: m!nh@$3nh@123
