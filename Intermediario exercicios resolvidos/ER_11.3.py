#Escreva um programa que permaneça em laço lendo números reais até que 
#seja digitado 0. Todos os valores digitados, exceto o zero, devem ser 
#gravados em um arquivo em disco, um por linha, com três casas decimais. 
#Usar o método .writelines()

lst = []

x = float(input('Digite um número real: '))
while x != 0:
    lst.append(f'{x:.3f}\n')
    x = float(input('Digite um número real: '))
print(lst)
arq = open('saida_ER_11.3.txt', 'w')
arq.writelines(lst) #ordena os itens por linha a cada inserção
arq.close()