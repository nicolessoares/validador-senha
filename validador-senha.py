import string
from rich import print
from rich.panel import Panel
from rich import box

print(Panel.fit((""":locked: [white]CADASTRO DE SENHA
                 
Sua senha deve ter:[/]
  >> Entre 8 e 30 caracteres
  >> Pelo menos 1 letra maíuscula
  >> Pelo menos 1 número
  >> Pelo menos 1 caractere especial (Ex. @!,#)
[white]Sua senha não pode ter:[/]
  >> Espaços em branco"""), box=box.DOUBLE))

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
        print(f'[red]:heavy_exclamation_mark: {e}[/]')

confirma_senha = str(input('Confirme a senha: '))
while confirma_senha != senha:
  print('[red]:cross_mark: As senhas precisam ser iguais. Tente novamente.[/]')
  confirma_senha = str(input('Confirme a senha: '))
print(':white_check_mark: [green]Senha registrada com sucesso![/]')



