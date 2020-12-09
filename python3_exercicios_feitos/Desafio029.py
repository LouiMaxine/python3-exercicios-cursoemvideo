'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7 por cada Km acima do limite'''

car = float(input('Digite a velocidade do carro: '))
if car>80:
    multa = (car - 80)*7
    print(f'Você foi multado em R${multa:.2f}')

