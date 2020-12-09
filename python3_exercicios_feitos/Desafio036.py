'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa
vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.'''

casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você vai pagar as prestações? '))
mes = anos*12
valMensal = casa/mes
if valMensal>sal*0.30:
    print(f'\033[1;31mEmpréstimo NEGADO\033[m, a prestação mensal de R${valMensal:.2f}, excede os 30% do seu salário.')
else:
    print(f'\033[1;35;40mParabéns! Empréstimo APROVADO com sucesso!\033[m Sendo 30% do seu salário, a prestação mensal será de R${valMensal:.2f}')


