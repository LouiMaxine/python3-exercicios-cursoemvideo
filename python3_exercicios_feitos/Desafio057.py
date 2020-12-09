'''FUPQ leia o sexo de uma pessoa, mas só aceite os valores m ou f. Caso esteja errado, peça a
digitação novamente até ter o valor correto'''


sexo = str(input('Sexo: [M/F] ')).upper()[0].strip()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
