#Escreva um programa que leia do teclado dois conjuntos de números inteiros 
#digitados pelo usuário. Exiba na tela a união e a interseção desses conjuntos.
msg = ('Digíte o valor: ')
c1 = set()
c2 = set()
print('Dados do primeiro conjunto\n')
x = int(input(msg))
while x != 0:
    c1.add(x)
    x = int(input(msg))
print('Dados do segundo conjunto\n')
x = int(input(msg))
while x != 0:
    c2.add(x)
    x = int(input(msg))

print(f'\nConjunto 1: {c1}\nConjunto 2: {c2}\n')
print(f'União dos conjuntos c1 e c2: \n{c1.union(c2)}\n')
print(f'Intersecção dos conjuntos c1 e c2: \n{c1.intersection(c2)}')