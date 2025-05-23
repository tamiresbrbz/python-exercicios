#Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa 
#quantidade de inteiros aleatórios. Exiba a lista na tela. Em seguida elimine valores
#que estiverem repetidos, deixando apenas uma ocorrência de cada. Exiba a nova lista 
#sem repetidos e o seu tamanho.
from random import randint
qtd = int(input('Digite a quantidade: '))
lista = []
while len(lista) < qtd:
    lista.append(randint(1, 100))
print(f'Lista gerada com {qtd} elementos:\n{lista}')
conjunto = set(lista)
lista = set(conjunto)
print(f'\nLista após os itens repetidos serem removidos: \n{lista}')
print(f'A lista tem {len(lista)} elementos')
print('Fim do programa')