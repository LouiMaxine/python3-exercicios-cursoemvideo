#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
# carro custa R$60 por dia e R$0.15 por Km rodado.
car = float(input('Qnt de Km rodados: '))
days=float(input('Qnt de dias: '))
pagar = car*0.15 + days*60
print(f'O total a pagar é de R${pagar:.2f}')