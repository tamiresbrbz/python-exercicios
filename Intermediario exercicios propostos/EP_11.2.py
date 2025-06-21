#Escreva um programa que leia um arquivo CSV de entrada que tenha dois 
#inteiros em cada linha. O primeiro é um código de produto e o segundo é 
#a quantidade vendida. O programa deve totalizar quantos itens foram 
#vendidos para cada produto.
#Dica: use um dicionário tendo o código como chave e a quantidade como 
#valor. Para cada código lido do arquivo verifique se ele já existe no 
#dicionário usando o operador in. Se não existir, inclua; se existir some
#a quantidade existente com a nova quantidade lida do arquivo.
vendas = {}

for linha in open('dados_11.2.txt', 'r'):
    x = linha.rstrip().split(';')
    cod = int(x[0])
    qtde = int(x[1])
    if cod in vendas:
        vendas[cod] = (vendas[cod] + qtde)
    else:
        vendas[cod] = (qtde)