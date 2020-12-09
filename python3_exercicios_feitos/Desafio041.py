'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de
um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
-Até 20 anos: SêNIOR
-Acima: MASTER'''

from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
if idade>20:
    print(f'Idade: {idade} ; Categoria: MASTER')
elif idade==20:
    print(f'Idade: {idade}; Categoria: SÊNIOR')
elif 14<idade<=19:
    print(f'Idade: {idade}; Catgoria: JUNIOR')
elif 9<idade<=14:
    print(f'Idade: {idade}; Categoria: INFANTIL')
else:
    print(f'Idade: {idade}; Categoria: MIRIM')


