#Escreva um programa que permaneça que leia um arquivo de entrada, sabendo que esse 
#arquivo tem um número inteiro em cada linha. Todos os números lidos devem ser 
#mostrados na tela. Mostrar também a soma dos valores, a quantidade, a média 
#aritmética, o menor valor e o maior valor. Usar aqui o mesmo arquivo de entrada do 
#exercício anterior.
#Usar um iterador for e o arquivo como iterável.
lst = []

for linha in open('entrada_er_11.4.txt', 'r'):
    lst.append(int(linha))

if len(lst) != 0:
    print(f'Lista lida do arquivo\n{lst}')
    print(f'Soma dos valores = {sum(lst)}\nQuantidade = {len(lst)}\nMédia = {sum(lst)/len(lst)}')
    print(f'Mínimo dos valores = {min(lst)}\nMáximo dos valores = {max(lst)}')
else:
    print('ERRO: Lista vazia')

print('\nFim do Progama')