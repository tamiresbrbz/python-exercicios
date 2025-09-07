#Reescreva o programa principal do exercício resolvido 12.10 de modo que no início seja feita a leitura 
#de um inteiro Qtde e a lista de valores seja gerada com Qtde números aleatórios não repetidos. Exiba 
#a lista na tela. Em seguida inicie o processo de busca semelhante ao implementado no exercício 
#12.10 para testar a função recursiva BuscaBin(). Lembre-se: a lista precisa estar ordenada. 
import random
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

#-----------Programa principal-----------
Qtd = int(input('Digíte a quantidade de números: '))
L = []
i = 0
while i < Qtd:
    a = random.randint(0, 99)
    if a not in L:
        L.append(a)
        i = i + 1
L.sort()
print(L)

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