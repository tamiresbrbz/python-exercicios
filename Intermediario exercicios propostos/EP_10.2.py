#Escreva um programa que permaneça em laço lendo do teclado números inteiros entre 1 e 9. 
#Outros valores devem ser ignorados. Esse laço termina quando for digitado zero ou qualquer 
#valor negativo. O objetivo deste programa é contar quantas vezes cada valor entre 1 e 9
#foi digitado. Ao término do laço de leitura o programa deve mostrar quais valores foram 
#digitados e quantas vezes cada um. Obrigatoriamente use um dicionário.
cont = {i: 0 for i in range(1, 10)}
print('Inicio da leitura de dados\nNúmeros menores ou iguais a 0 terminam a leitura\n')
num = int(input('Digíte um número: '))

while num > 0:
    if(num <= 9):
        cont[num] += 1
    elif(num > 9):
        print('Números maiores que 9 serão ignorados')

    num = int(input('Digíte um número: '))

for numero, quant in cont.items():
    if quant > 0:
        print(f'Número: {numero} | Quantidade: {quant}')