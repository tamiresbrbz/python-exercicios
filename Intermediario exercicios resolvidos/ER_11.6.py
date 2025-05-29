#Escreva um programa que leia um arquivo de entrada carregando seus
#dados em um dicionário e ao final exibindo-os na tela. A figura 
#11.1 mostra o do lado esquerdo a natureza dos dados que serão 
#lidos e do lado direito mostra o formato do arquivo.
#Esse formato é conhecido como CSV. Arquivos CSV são muito usados 
#em diversas áreas da computação, em especial em Análise de Dados. 
#O que caracteriza um arquivo CSV é que cada linha tem um conjunto 
#de dados de alguma forma relacionados e separados por um caractere
#delimitador. No arquivo deste exercício o delimitador é um 
#ponto-e-vírgula ";"
#Neste caso, cada linha tem: código de produto (int), a quantidade 
#em estoque (int), preço (float). Use o código como chave para o 
#dicionário e valor deve ser em formato de tupla.
Estoque = {}

for linha in open('entrada_er_11.6.txt', 'r'):
    lst = linha.rstrip().split(';') #remove o '\n' oculto no txt || cria uma lista com, cada linha
    cod = int(lst[0])
    qtde = int(lst[1])
    pcunit = float(lst[2])
    Estoque[cod] = (qtde, pcunit)

print('Exibição dos dados na forma de tabela')
tot = 0

print('{:9} {:6} {:8} {:10}'.format('Código', 'Qtde', 'Valor', 'Total'))
for cod, dados in Estoque.items():
    tot += dados[0] * dados[1]
    print(f' {cod}: {dados[0]:5d} x {dados[1]:6.2f} = {dados[0] * dados[1]:8.2f}')
print(' ' * 10, f'Total Geral = {tot:8.2f}')

print('\nFim do Programa')