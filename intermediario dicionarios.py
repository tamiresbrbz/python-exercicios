#Dicionários e sua estrutura --> Bastante parecido com as listas, porem a
#identificação dos elementos não é feita por um índice, mas sim por um 
#valor chave que pode ser texto ou número que eu escolho
UF = {'SP': 'São Paulo', 'RJ': 'Rio de Janeiro', 'MG': 'Minas Gerais'}
print(f'{type(UF)}\n{UF}')
UF['PB'] = 'João Pessoa' #Adiciona conteúdo ao dicionário
print(UF)

D = {}
D['a'] = 120
D['a'] = 250 #Assim eu altero o elemento da chave 'a'
D['b'] = 90
x = D['a'] + D['b']
print(x)
D['a'] = D['a'] + 100
print(D['a'])
D['a'] += 100
print(D)
chave = 'a'
print(D[chave])
chave = 'b'
print(D[chave])
chave = 'c'
D[chave] = 0
print(D)

M={}
M[110] = 45.6
M[9.2] = 'xpto'
print(M)
M[(1, 0, 5)] = 281.9
print(M) #Todos os objetos de classe imutável, podem ser usados como chave
print('\n\n-------------------Métodos existentes no dicionário----------------\n')
D = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha'}
D[125] = 'Açúcar'
D[133] = 'Macarrão'
print(f'Dicionário D: {D}')
D.clear() #Limpa o dicionário
print(f'Dicionário limpo: {D}')
D = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açúcar', 133: 'Macarrão'}
A = D.copy #Produz uma cópia do dicionário, em locais diferente na memória
print(f'id(A): {id(A)}\nid(D): {id(D)}\n')
A = D #A ocupa o mesmo espaço na memória que D
print(f'Endereços de memória:\n{id(A)}\n{id(D)}\n\n')

print(A.get(134)) #a chave 134 retorna o valor dentro dela
X = A[125] #retorna o valor do qual 125 representa
print(X)

A = D.copy()
codigos = (111, 139, 143, 157)
print(A.fromkeys(codigos))
print(A.fromkeys(codigos, 'algo')) #cria um novo dicionário, onde a chave está no primeiro parametro
del(A)
A = {}.fromkeys(codigos, ' ')
print(A)
A[111] = 'Vinagrete'
D[111] = 'Vinagrete'
print(A)
print(D)

X = D.pop(111) #o valor indicado pela chave é removido do dicionário
print(f'\nValor Removido: {X}\nDicionário:{D}\n')
X = D.pop(117)
print(D)

X = D.popitem() #remove o último item que entrou no dicionário como tupla
print(X)
print(type(X))

D = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açúcar', 133: 'Macarrão', 111: 
'Vinagrete'}
R = D.setdefault(144, 'Feijão') #insere o item no dicionário, pq não existia 144
print(R)                        #Se o item já existe no dicionário, não acontece nada

D.update( ( (177, 'Cebola'), (271, 'Maçã'), (185, 'Abacate') ) ) #exige um parametro q tem q 
#ser lista ou tupla e dentro da tupla precisa de um par que vai ser uma tupla também, serão os pares
print(D)

Ch = D.keys() #retorna todas as chaves do dicionário
print(f'Classe de Ch: {type(Ch)}\nRetorno do Ch: {Ch}\n')

Vl = D.values() #retorna os itens do dicionário
print(f'Classe de Vl: {type(Vl)}\nRetorno do Vl: {Vl}\n')

It = D.items()
print(f'Classe de It: {type(It)}\nRetorno do It: {It}\n') #Retorna as tuplas com formato diferente
print('TUPLAS:\n')

for k in D.items():
    print(k)
for k in D.keys():
    print(k)
for k in D.values():
    print(k)

print('\n---------------------------Exemplo 10.5---------------------------\n\n')

cores = {1: 'azul', 2: 'verde', 3: 'amarelo', 4: 'vermelho'}
print('Exibição do dicionário - Caso 1')
for x in cores:
    print(f' {x} - {cores[x]}')
print('\nFim do programa')

print('\n---------------------------Exemplo 10.6---------------------------\n\n')

cores = {1: 'azul', 2: 'verde', 3: 'amarelo', 4: 'vermelho'}
print('Exibição do dicionário - Caso 2')
for cor in cores.values():
    print(f' {cor}')
print('\nFim do programa')

print('\n---------------------------Exemplo 10.7---------------------------\n\n')

cores = {1: 'azul', 2: 'verde', 3: 'amarelo', 4: 'vermelho'}
print('Exibição do dicionário - Caso 3')
for numero, cor in cores.items():
    print(f' nº da cor = {numero} - nome da cor = {cor}')
print('\nFim do programa')