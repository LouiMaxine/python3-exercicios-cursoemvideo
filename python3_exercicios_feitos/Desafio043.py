'''Desenvolva uma lógica que leia o peso e a altra de uma pessoa, calcule seu IMC(índice de massa corpórea) e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

#from math import pow
peso = float(input('Peso: '))
alt = float(input('Altura: '))
#imc = peso/pow(alt,2)
imc = peso/(alt**2) #esqueci que poderia usar dois asteriscos, obgda Guanabara
if imc<18.5:
    print(f'Seu IMC é: {imc:.2f} e você está ABAIXO DO PESO')
elif 18.5<=imc<25:
    print(f'Seu IMC é: {imc:.2f} e você está no PESO IDEAL')
elif 25<=imc<30:
    print(f'Seu IMC é: {imc:.2f} e você está com SOBREPESO')
elif 30<=imc<=40:
    print(f'Seu IMC é: {imc:.2f} e você está com OBESIDADE')
else:
    print(f'Seu IMC é: {imc:.2f} e você está com OBESIDADE MÓRBIDA')




