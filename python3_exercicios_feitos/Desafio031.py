'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
passagem, cobrando R$0.50 por Km pra viagens de até 200Km e R$0.45 para viagens mais longas '''

viag = float(input('Digite a distância da viagem: '))
if viag>200:
    print(f'O valor da passagem é R${viag*0.45}')
else:
    print(f'O valor da passagem é R${viag*0.50}')


