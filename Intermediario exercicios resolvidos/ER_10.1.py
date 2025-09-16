produtos = {}
print('Leitura de dados')
cod = input('    Digíte o código: ')
while cod != '':
    preco = float(input('    Digíte o valor: '))
    produtos[cod] = preco
    cod = input('    Digíte o código: ')
print('Fim da leitura de dados')

for cod in produtos.keys():
    print(f'Código produto: {cod}     Valor: R${produtos[cod]:7.2f}')
print("\nFim do programa")