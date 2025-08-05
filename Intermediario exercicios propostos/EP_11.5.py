#Enunciado: Escreva  um  programa  que  leia  o  arquivo  NUMEROS.TXT  gerado  no
#exercício  proposto  11.4, colocando-os em uma lista. Ordene a lista usando 
#o .sort() e grave os números ordenados no arquivo ORDENADOS.TXT

numeros = []
arq = open('NUMEROS.TXT', 'r')
for linha in arq:
    numeros.append(int(linha.strip()))
arq.close()
ordenada = sorted(numeros)

arq = open('ORDENADOS.TXT', 'w')

for i in ordenada:
    arq.write(f"{i}\n")

arq.close()
print(f"Arquivo 'ORDENADOS.TXT' criado com {len(ordenada)} números ordenados!!")