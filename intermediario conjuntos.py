#Conjuntos aprofundamento - capítulo 9
print('\n------------------CRIAÇÃO DE CONJUNTOS DA CLASSE SET------------------\n')
#não pode ter elementos repetidos, eles serão ignorados, a ordem do conjunto depende do interpretado python
c1 = {21, 8, 16, 30, 21, 41, 28} #cria um conjunto
print(type(c1)) #retorna a classe
print(len(c1)) #retorna o tamanho do conjunto
print(c1) #retorna o conjunto
c2 = set() #cria um conjunto vazio da classe set
           #o construtor set só aceita um argumento, ou seja
           #c3 = set(4, 9, 24, 21) dará erro
c3 = set( [4, 9, 24, 21] ) #funciona, pois recebe os dados como uma lista
print(c3) #dentro do construtor cria uma tupla ou uma lista

print('\n----exemplo 09 02----')
texto = 'Qualquer texto'
print(type(texto))
c4 = set (texto)
print(c4) #só vai aparecer uma ocorrência de cada letra

tupla = (26, 73, 41, 41)
c5 = set(tupla)
print(c5)

lista = [32, 34]
c6 = set(lista)
print(c6)

c7 = set(c4) #aqui se clona um conjunto que estará em outro local na mémoria do pc
print(id(c7))
print(id(c4))

print('\n----exemplo 09 03 | HASH----')
#HASH --> forma de criar uma identificação baseado no conteudo do objeto
s1 = 'abcd'
print(hash(s1))
s2 = 'abcd'
print(hash(s2)) #os dois textos estão em obejtos difentes, mas são iguais, pois o conteúdo é igual
                #não é possível calcular o HASH de objetos mutáveis

c1 = {207, 37.3, (9, 10, 11), 'abcd'} #cada ítem aí dentro tem um hash
print(hash(207))
print(hash(37.3))
print(hash((9, 10, 11)))
print(hash('abcd'))

print('\n----exemplo 09 04 | HASH----')
c = {26, 26.0}
print(hash(26))
print(hash(26.0)) #Os HASHS são iguais, pois ambos remetem ao mesmo número
                  #apesar de ser um int e um float

print('\n----exemplo 09 05 | Métodos existentes dentro da classe SET----')
c = set()
print(f'{type(c)}\n{len(c)}')
c.add(85) #inclui elementos dentro do conjunto
c.add(190)
c.add(32)
c.add(76)
c.add(32.4)
c.add('abcd')
print(c) #a ordem não é relevante no SET
c.clear() #limpa o conjunto
print(c)

c = {36, 77, 81, 43, 18}
print(c)

d = c.copy() #cria uma copia de C, com IDs diferentes, serão coisas diferentes

c1 = {26, 32, 45, 58, 63}
c2 = {19, 34, 58, 67, 82}
print(c1.difference(c2)) #retorna os números diferentes de c1 que não estão em c2

d = c1.difference_update(c2) #o próprio c1 é atualizado, não há retorno guardado em outro conjunto
print(f'c1:{c1}\nc2:{c2}')

c2.discard(58) #remove um elemento do conjunto
print(f'c2:{c2}') #se o elemento solicitado não existir, não acontece nada

c1.add(82)
c1.add(34)
print(f'interseção de c1 e c2:{c1.intersection(c2)}')#retorna os elementos existentes nos dois conjuntos
c1.intersection_update(c2) #a alteração ocorre no próprio c1
print(f'c1:{c1}')

c1.add(50)
c1.add(88)
c1.add(17)

print(c1.isdisjoint(c2))#conjuntos são disjuntos, quando não há nenhum elemento igual
c1.discard(34)
c1.discard(82)
print(c1.isdisjoint(c2))#TRUE, pois nenhum elemento é igual
print(c1.intersection(c2))

print(c1.issubset(c2))#verifica se todos os elementos de c1 estão em c2
c2.add(17)
c2.add(50)
c2.add(88) #inclui todos os elementos de c1 em c2, agora retorna TRUE
print(f'Issubset de c1 e c2: {c1.issubset(c2)}')

print(c1.issuperset(c2))#TRUE quando c1 contém todos os elementos de c2
print(c2.issuperset(c2))

print(f'c1: {c1}')
a = c1.pop() #remover algum elemento do conjunto de forma arbitraria
print(f'item removido: {a}') #não funciona com conjuntos vazios
print(f'c1: {c1}')
c1.pop()
c1.pop()

print(f'c2: {c2}')
c2.remove(17) #remove um elemento indicado no conjunto
print(f'c2: {c2}')

print(50 in c2)#pergunta de o 50 está no c2

c1 = {50, 16, 39, 88, 67}
print(f'c1: {c1}\nc2: {c2}')
d = c1.union(c2) #união do c1 e c2 apenas uma copias dos repetidos
print(f'união de c1 e c2: {d}')

print(c1.symmetric_difference(c2)) #todos os presentes nos conjuntos menos as copias dos dois
c3 = c1.copy()                     #pode ser atribuido a um objeto
print(f'c3: {c3}\nc2: {c2}')
c3.symmetric_difference_update(c2) #atualiza o c3 para q ele seja a diferença simetrica
print(f'c3: {c3}') 

c1.update(c2) #union_update -> atualiza o c1 para q seja a união de c1 e c2

print('\n----exemplo 09 07----')
print('primeira execução')
conjunto = {3.3, 18.6, 34.0, 43.1, 58.7}
for c in conjunto:
    print(c)

print('segunda execução')
conjunto = {18.6, 3.3, 58.7, 34.0, 43.1}
for c in conjunto:
    print(c)
    #não importa qual ordem seja usada na criação do conjunto, uma vez inseridos
    #no conjunto o interpretador Python decidirá em que posição cada um estará
    
print('\n\nFim do Programa')