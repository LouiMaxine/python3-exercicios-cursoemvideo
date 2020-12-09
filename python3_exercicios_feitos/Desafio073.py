'''Crie uma tupla preenchida com os 20 primeiros colocados na Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela;
c)Uma lista com os times em ordem alfabética
d) Em que posição da tabela está o time da Chapecoense'''

brasileirao = ('Palmeiras', 'Santos','Flamengo','Internacional','Atlético-MG','Goiás','Botafogo','Bahia','São Paulo','Corinthians','Grêmio','Athletico-PR','Ceará','Fortaleza','Vasco','Fluminense','Chapecoense','Cruzeiro','CSA','Avaí')
print('*'*30)
print('TABELA DO BRASILEIRÃO 2019')
print(f'{brasileirao}')
print('*'*30)

print(f'Os 5 primeiros colocados: {brasileirao[0:5]}')
print('*'*30)
print(f'Os 4 últimos colocados são: {brasileirao[-4:]}')
print('*'*30)
print('Em ordem alfabética:')
print(f'{sorted(brasileirao)}')
print('*'*30)
#print(f'O Chapecoense está {brasileirao.index()}')
print('*'*30)

