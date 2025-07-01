#Enunciado: Escreva um programa que grave o arquivo NUMEROS.TXT com 2.000 números, 
#um em cada linha, gerados com a função randint() do módulo random no 
# intervalo [1, 5.000].  
#Variação: Altere este programa substituindo o tamanho fixo de 2.000 por uma 
# quantidade de entrada a ser lida do teclado.
import random
arq = open('NUMEROS.TXT', 'w')
y = 0
n = 0
while n <1 or n > 5000:
    n = int(input("Dígite a quantidade de números a serem gerados (entre 1 e 5000): "))
    if n < 1 or n > 5000:
        print("Número inválido!!\n"
        "Deve ser entre 1 e 5000.\n")
    else:
        while y < n:
            i = random.randint(1, 5000)
            arq.write(f'{i}\n')
            y += 1
        arq.close()
        print(f"Arquivo 'NUMEROS.TXT' criado com {n} números!!")
            

