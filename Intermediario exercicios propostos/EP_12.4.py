#Escreva um programa que leia dos inteiros A, B e carregue uma lista com
#todos os números primos situados no intervalo fechado [A, B]. Use a 
#função Primo() apresentada no exercício anterior. Ao final exiba a 
#lista na tela.
#Adicionalmente escreva uma função para exibir a lista de primos de uma 
#forma organizada na tela.
def Primo(V):
    '''Se V for primo, retorna True, se não, retorna False'''
    if V == 2:
        return True
    elif V % 2 == 0:
        return False
    else:
        raiz = pow(V, 0.5) # raiz quadrada de V
        i = 3
        while i <= raiz:
            if V % i == 0:
                return False
            i += 2
        return True
def ValidaAB(A, B):
    '''Valida se A é menor que B'''
    while A >= B:
        print('Valor inválido! A deve ser menor que B.')
        A = int(input("Digite o valor do início do intervalo (A): "))
        B= int(input("Digite o valor do fim do intervalo (B): "))
    return A, B
def ExibeLista(Lista, a, b):
    '''Exibe lista de primos de forma organizada'''
    print(f'Lista de números primos no intervalo fechado [{a}, {b}]:')
    for i in Lista:
        print(i, end='; ')


ListaPrimos = []
A = int(input("Digite o valor do início do intervalo (A): "))
B = int(input("Digite o valor do fim do intervalo (B): "))
A, B = ValidaAB(A, B)
C = A
while A < B:
    if Primo(A) == True:
        ListaPrimos.append(A)
    A += 1

ExibeLista(ListaPrimos, C, B)


