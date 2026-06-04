import string

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