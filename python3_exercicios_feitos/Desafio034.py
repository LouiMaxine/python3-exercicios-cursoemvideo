'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a 1.250.00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%'''

sal = float(input('Salário: '))
if sal>1250:
    print(f'Seu novo salário é de R${sal*0.10+sal:.2f} com um aumento de 10%')
else:
    print(f'Com um aumento de 15%, seu salário agora é R${sal*0.15+sal:.2f}')

