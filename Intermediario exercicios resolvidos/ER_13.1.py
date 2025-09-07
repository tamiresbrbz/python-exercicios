#Considere que você deve aplicar um aumento percentual a todos os preços 
# que estão em uma lista. Escreva um programa que leia essa lista do 
# teclado. Os valores devem ser lidos enquanto não for digitado zero. 
# Na sequência leia a porcentagem de aumento.
#Em seguida, usando list comprehension, faça a aplicação desse aumento a
# todos os valores e mostre na tela.
#o aumento deve ser aplicado apenas aos valores menores que 100 reais.
Lista = []
print('Forneças os preços dos produtos para a lista. Digite 0 para encerrar a lista.')
preco = (float(input('Digite um valor real: ')))
while preco != 0:
    Lista.append(preco)
    preco = (float(input('Digite um valor real: ')))

Percent = float(input('Digite a procentagem de aumento: '))
print(f'\nLista original: \n{Lista}\n')
print(f'Valores que foram acrescidos de {Percent}%:')
Lista2 = [x + (x * Percent / 100) for x in Lista if x < 100]
for valor in Lista2:
    print(f'R$ {valor:.2f}')

