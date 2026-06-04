# Validador de Senha

Projeto desenvolvido em Python para validar uma senha com base em critérios de segurança, com feedback no terminal.

---

## Sobre o projeto

O **Validador de Senha** é um programa que guia o usuário na criação de uma senha segura, exibindo mensagens de erro no terminal até que todos os critérios sejam atendidos.

---

## Critérios de validação

A senha deve ter:

- Entre **8 e 30 caracteres**
- Pelo menos **1 letra maiúscula**
- Pelo menos **1 número**
- Pelo menos **1 caractere especial** (Ex: @, !, #)

A senha não pode ter:

- **Espaços em branco**

---

## Como executar

**Pré-requisito:** Python 3 instalado.

```bash
# Clonando o repositório
git clone https://github.com/nicolessoares/validador-senha.git

# Acessando a pasta
cd validador-senha

# Executando o projeto
python main.py
```

---

## O que foi utilizado

- `Python 3`
- Módulo `string` para verificar a existência de caracteres especiais na senha.
- Módulo `rich` para otimizar a estética do programa no terminal.

---

## Melhorias futuras

Desenvolver a interface visual do projeto, integrando HTML, CSS com SASS e JavaScript, trazendo intuitividade, responsividade, e possibilitando que ele seja executado diretamente pelo navegador.
