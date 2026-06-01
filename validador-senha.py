import string

print("""========== CADASTRO DE SENHA ==========
\033[1;37mSua senha deve ter:\033[m
  >> Entre 8 e 30 caracteres
  >> Pelo menos 1 letra maíuscula
  >> Pelo menos 1 número
  >> Pelo menos 1 caractere especial (Ex. @!,#)
\033[1;37mSua senha não pode ter:\033[m
  >> Espaços em branco
=======================================""")

def validar_senha(senha):
  erros = []
  if not senha:
    erros.append('O campo de senha não pode estar vazio.')
  if len(senha) < 8 or len(senha) > 30:
    erros.append('A senha deve ter entre 8 e 30 caracteres.')
  if not any(c.isupper() for c in senha):
    erros.append('A senha deve ter pelo menos 1 letra maiúscula.')
  if not any(c.isnumeric() for c in senha):
    erros.append('A senha deve ter pelo menos 1 número.')
  if not any(c in string.punctuation for c in senha):
    erros.append('A senha deve ter pelo menos 1 caractere especial.')
  if ' ' in senha:
    erros.append('A senha não pode conter espaços em branco.')

  return erros

while True:
    senha = input('Digite sua nova senha: ')
    erros = validar_senha(senha)
    if not erros:
        break
    for e in erros:
        print(f'\033[31m>> {e}\033[m')

confirma_senha = str(input('Confirme a senha: '))
while confirma_senha != senha:
  print('\033[31mAs senhas precisam ser iguais. Tente novamente.\033[m')
  confirma_senha = str(input('Confirme a senha: '))
print('\033[32mSenha registrada com sucesso!\033[m')



