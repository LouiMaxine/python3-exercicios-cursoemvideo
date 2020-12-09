'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
-a vista dinheiro/ cheque: 10% de desconto (Código: D/CH)
- a vista no cartão: 5% de desconto        (Código: VC)
- em até 2x no cartão: preço normal        (Código: 2C)
-3x ou mais no cartão: 20% de juros        (Código: C) '''

produto = float(input('Valor do Produto: '))
pagamento = str(input('Forma de Pagamento[D/CH/VC/2C/C]: ')).upper()
if pagamento == 'D' or pagamento == 'CH':
    desconto = produto - produto*0.10
    print(f'Com 10% de desconto o valor é R${desconto}')
elif pagamento == 'VC':
    desconto = produto - produto*0.5
    print(f'Com 5% de desconto, o valor é R${desconto}')
elif pagamento == '2C':
    print(f'Preço normal, valor de R${produto}')
elif pagamento == 'C':
    juros = produto + produto*0.20
    print(f'Juros de 20%, valor de R${juros}')
else:
    print(f'Código inválido, tente novamente')


