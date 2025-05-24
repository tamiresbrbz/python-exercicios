#Escreva um programa que permaneça em laço lendo números inteiros até que
#seja digitado 0. Todos os valores digitados, exceto o zero, devem ser 
#gravados em um arquivo em disco, um por linha.
#Usar o método .write()
arq = open('saida_ER_11.1.txt', 'w') #1º parametro:nome do arquivo com extensão
                                     #2º parametro:w indicando q o arquivo serve para gravação
A = int(input('Digite um inteiro: '))
while A != 0:
    arq.write(f'{A}\n')
    A = int(input('Digite um inteiro: '))

arq.close() #é necessário que o arquivo seja finalizado, para não perder dados

print('\nFim do Programa')

#Se ja houver um arquivo ele vai ser sobrescrito