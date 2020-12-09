#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere USS 1,00= R$ 3,27

din = float(input('Digite o valor: '))
print(f'{din:.2f} reais equivalem a {din/3.85:.2f} dólares')