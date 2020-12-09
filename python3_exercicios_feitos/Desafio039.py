'''FUPQ leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar:
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo'''

from datetime import date
nasc = int(input('Em que ano você nasceu? '))
atual = date.today().year
idade = atual - nasc
if idade<18:
    falta = 18 - idade
    print(f'Você tem {idade} anos. Ainda faltam {falta} anos para você se alistar.')
    ano = atual + falta #Adção de Guanabara, mas o resto consegui sozinha
    print(f'Seu alistamento será em {ano}')
elif idade == 18:
    print(f'Você já tem {idade} anos! Hora de se alistar!')
else:
    atraso = idade - 18
    print(f'Você já tem {idade}! Seu alistamento está {atraso} anos atrasado!!!')
    ano = atual - atraso
    print(f'Seu alistamento foi em {ano}')

