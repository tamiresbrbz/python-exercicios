#Enunciado: Escreva um programa que leia um arquivo de entrada contendo números 
#inteiros, sendo um por linha, e os coloque em uma lista. Em seguida pense em 
#alguma forma de remover os valores repetidos, deixando apenas uma cópia de cada 
#valor. A  lista  resultante  após  a  eliminação  dos  repetidos,  deve  ser 
#ordenada  e  salva  no  arquivo UNICOS.TXT, um inteiro por linha.
arq = open('ORDENADOS.TXT', 'r')
lista = []

for linha in arq:
    numero = linha.strip()
    if numero not in lista:
        lista.append(numero)
arq.close()

arq = open('UNICOS.TXT', 'w')
for i in lista:
    arq.write(f'{i}\n')
arq.close()
print(f"Arquivo 'UNICOS.TXT' criado com {len(lista)} números únicos ordenados!!")