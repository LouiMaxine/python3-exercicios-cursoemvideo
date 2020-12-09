#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos
# alunos. FUPQ leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle
n1 = input('Aluno1: ')
n2 = input('Aluno2: ')
n3 = input('Aluno3: ')
n4 = input('Aluno4: ')
lista = [n1,n2,n3,n4]
shuffle(lista)
print(lista)


