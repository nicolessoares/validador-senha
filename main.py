from rich import print
from rich.panel import Panel
from rich import box
import functions

print(Panel.fit((""":locked: [white]CADASTRO DE SENHA
                 
Sua senha deve ter:[/]
  >> Entre 8 e 30 caracteres
  >> Pelo menos 1 letra maíuscula
  >> Pelo menos 1 número
  >> Pelo menos 1 caractere especial (Ex. @!,#)
[white]Sua senha não pode ter:[/]
  >> Espaços em branco"""), box=box.DOUBLE))

while True:
    senha = input('Digite sua nova senha: ')
    erros = functions.validar_senha(senha)
    if not erros:
        break
    for e in erros:
        print(f'[red]:heavy_exclamation_mark: {e}[/]')

confirma_senha = str(input('Confirme a senha: '))
while confirma_senha != senha:
  print('[red]:cross_mark: As senhas precisam ser iguais. Tente novamente.[/]')
  confirma_senha = str(input('Confirme a senha: '))
print(':white_check_mark: [green]Senha registrada com sucesso![/]')



