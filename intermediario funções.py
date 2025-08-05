print("-------------------EMPACOTAMENTO DE FUNÇÕES--------------------\n")
def Somatoria (*dados): #para receber um número variável de argumentos, ou seja vários argumentos para dados
    r=0
    for i in dados:
        r += i
    return r

a = Somatoria(3, 5, 1, 4)
print(a)

print('\n-------------------FUNÇÕES COM ARGUMENTO--------------------\n')
def MontaSaida(*valores, separador = ', '): #separador é um argumento padrão, se não for passado, será usado a vírgula
    saida = separador.join(valores) #join --> junta os valores de uma lista ou tupla, join só funciona com strings
    print(f'Valores: {saida}')
    return saida

MontaSaida('Maçã', 'Laranja', 'Banana', 'Melão', separador=' - ') #passando o separador como argumento
MontaSaida('Maçã', 'Laranja', 'Banana', 'Melão') #usando o separador padrão, que é a vírgula

print('\n-------------------DESEMPACOTAMENTO DE FUNÇÕES--------------------\n')
def Calcula(a, b, c):
    saida = (a + b) / c
    print(f'O resultado é: {saida}')
    return saida

L1 = [12, 20, 5] #a lista deve ter o mesmo número de elementos que os parâmetros da função
Calcula(*L1) #desempacotando a lista L1, ou seja, passando os valores da lista como argumentos separados

print('\n-------------------ESCOPO DE OBJETOS--------------------\n')
def função1():
    print('dentro da fução 1 temos >>', a, b) #recebe os valores de a e b do escopo global

def função2():
    a = 100
    b = 200
    print('dentro da fução 2 temos >>', a, b) #recebe os valores de a e b do escopo local, do qual será sempre a preferencia de uso

a = 10 #objetos de escopo global
b = 20

função1()
função2()
print('fora das funções temos >>', a, b) #os valores exibidos são os do escopo global

#dica: evitar conflito de nomes de variáveis entre escopos, para não gerar confusão

print('\n-------------------FUNÇÕES RECURSIVAS--------------------\n')
def Fatorial(N):
    if N <= 1:
        return 1
    else:
        return N * Fatorial(N - 1) #a recursiva vai retornar seu valor até chegar ao caso base, que é N <= 1
        #Exemplo: Fatorial(4)
        # 4 * Fatorial(3) = 4 * 6 = 24
        # 3 * Fatorial(2) = 3 * 2 = 6
        # 2 * Fatorial(1) = 2 * 1 = 2

Entrada = 4
F = Fatorial(Entrada)
print(f'O fatorial de {Entrada} é {F}')

print('\n-------------------FUNÇÕES LAMBDA--------------------\n')
def mais2(a):
    return a + 2

print(mais2(10))

print(lambda x: x + 2) #função lambda, que é uma função anônima, ou seja, não tem nome
#pode ser usada para criar funções simples, de uma linha

print((lambda x: x + 2)(10)) #função lambda com parâmetro, que recebe o valor 10 e retorna 12
print((lambda x, y, z: (x + y) / z)(350, 50, 20)) #função lambda com três parâmetros, que retorna o maior valor

print('\n-------------------FUNÇÕES LAMBDA COMBINADA COM map()--------------------\n')
#map() aplica uma função a todos os itens de um iterável (lista, tupla, etc.)

L = [8, 5, 3, 9, 7, 2]
def quadrado(a):
    return a ** 2

L2 = list(map(quadrado, L)) #aplica a função quadrado a todos os itens da lista L
print(L2) #converte o resultado de map() em uma lista
        #o list converte o resultado de map() em uma lista, pois map() retorna um iterável

L3 = list(map(lambda x: x ** 3, L)) #aplica a função lambda a todos os itens da lista L
print(L3) #converte o resultado de map() em uma lista, que nesse caso é o cubo dos números da lista L

print('\n-------------------FUNÇÕES - APLICAÇÃO--------------------\n')
prods = {'121': 23.90, '189': 14.33, '152': 36.95, '175': 19.35}
sorted(prods) #retorna os itens do dicionário ordenados apenas pelas chaves
print(prods)
print(sorted(prods.items())) #retorna os itens do dicionário ordenados pelas chaves, mas como tuplas

print(prods.items()) #retorna uma lista com os itens do dicionário como tuplas

print(sorted(prods.items(), key=lambda x: x[1])) #ordena os itens do dicionário pelas chaves quem tem indice 1, ou seja, pelos valores
