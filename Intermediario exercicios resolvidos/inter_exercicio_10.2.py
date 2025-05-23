#Escreva um programa que leia do teclado o código de um produto e seu 
#preço unitário. O código é um string e o preço é real. Acrescente o par
#código:preço em um dicionário. O programa deve verificar se o código já
#está no dicionário e neste caso deve emitir uma mensagem de erro. O laço
#termina quando for fornecido um string vazio para o código. Ao final, 
#exibir código e preço, um produto em cada linha.

produto = {}
print('Leitura de dados')
cod = input('   Digíte o código: ')
while cod != '':
    if cod in produto:
        print('ERRO: Código já existe')
        cod = input('   Digíte outro código: ')
    else:
        valor = float(input('   Digíte o valor: '))
        produto[cod] = valor
        cod = input('   Digíte o código: ')
for x, y in produto.items():
    print(f'Código produto: {x}  Valor: R${y:7.2f}')
print("\nFim do programa")