#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input("Digite o número que você quer saber a tabuada: "))
for i in range(1,11):
    print('{} x {:2} = {}'.format(num,i,num*i))