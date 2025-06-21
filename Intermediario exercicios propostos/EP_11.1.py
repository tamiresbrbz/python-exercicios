#Reescreva o programa exercício resolvido 11.6 usando um dicionário 
#aninhado no lugar da tupla como valor para o dicionário Estoque.
Estoque = {}

for linha in open('entrada_er_11.6.txt', 'r'):
    lst = linha.rstrip().split(';') #remove o '\n' oculto no txt || cria uma lista com, cada linha
    cod = int(lst[0])
    qtde = int(lst[1])
    pcunit = float(lst[2])
    Estoque[cod] = {'quantidade': qtde, 'valor': pcunit}

print('Exibição dos dados na forma de tabela')
tot = 0

print('{:9} {:6} {:8} {:10}'.format('Código', 'Qtde', 'Valor', 'Total'))
for cod, dados in Estoque.items():
    tot += dados['quantidade'] * dados['valor']
    print(f" {cod}: {dados['quantidade']:5d} x {dados['valor']:6.2f} = {dados['quantidade'] * dados['valor']:8.2f}")
print(' ' * 10, f'Total Geral = {tot:8.2f}')

print('\nFim do Programa')