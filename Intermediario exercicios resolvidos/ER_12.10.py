#Enunciado: Escreva um programa que implemente uma busca binária através 
# de uma função recursiva. O programa principal deve permanecer em laço 
# lendo valores inteiros que deve ser buscados na lista.
#Caso de Teste: Neste exercício será usada uma lista contendo valores
#  fixos e que foi apresentada na figura 12.5. O objetivo é que você 
# possa testar o programa com os valores como mostrado aqui.

def BuscaBin(valor, lista, ini, fim):
    '''Procura o valor na lista L entre os índices ini:fim'''
    print(f'ini = {ini}, fim = {fim}, meio = {(ini + fim) // 2}')
    if ini > fim:
        return False
    meio = (ini + fim) // 2
    if valor == lista[meio]:
        return True
    elif valor < lista[meio]:
        return BuscaBin(valor, lista, 0, meio - 1)
    else:
        return BuscaBin(valor, lista, meio + 1, fim)

L = [14, 17, 20, 22, 23, 25, 28, 29, 31, 35, 40, 45, 50, 53, 56, 59, 62, 65]
X = int(input('Digite um valor para pesquisa na lista: '))
while X != 0:
    Achou = BuscaBin(X, L, 0, len(L)-1)
    if Achou != 0:
        # chamada para verificar a metade esquerda da lista
        print(f'{X} está na lista')
    else:
        # chamada para verificar a metade direita da lista
        print(f'{X} não está na lista') 
    X = int(input('Digite um valor para pesquisa na lista: '))
print('Fim do Programa')