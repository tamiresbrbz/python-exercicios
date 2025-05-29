#Escreva um programa que permaneça que leia um arquivo de entrada, sabendo
#que esse arquivo tem um número inteiro em cada linha. Todos os números 
#lidos devem ser mostrados na tela. Mostrar também a soma dos valores, a 
#quantidade, a média aritmética, o menor valor e o maior valor.
#Usar um laço while e na leitura usar o método .readline()
lst = []
arqEntr = open('entrada_er_11.4.txt', 'r') #abre o arquivo de entrada e r para ler
linha = arqEntr.readline()

while linha != '':
    lst.append(int(linha))
    linha = arqEntr.readline()
arqEntr.close()

if len(lst) != 0:
    print(f'Lista lida do arquivo\n{lst}')
    print(f'Soma dos valores = {sum(lst)}\nQuantidade = {len(lst)}\nMédia = {sum(lst)/len(lst)}')
    print(f'Mínimo dos valores = {min(lst)}\nMáximo dos valores = {max(lst)}')
else:
    print('ERRO: Lista vazia')

print('\nFim do Progama')
