#Escreva uma função recursiva para determinar o N-ésimo termo da sequência de Fibonacci. Escreva 
#o programa principal para testar essa função. Neste programa deve ser lido um valor inteiro N e, 
#usando a função recursiva, devem ser calculado e exibido o N-ésimo termo da sequência. 
#A sequência de Fibonacci é definida da seguinte forma: a) os dois primeiros termos da sequência 
#são 0 e 1. Do terceiro termo em diante cada termo é a soma dos dois anteriores. 
#Casos de teste: p/ N = 5 -> termo = 3    p/ N = 7 -> termo = 8    p/ N = 10 -> termo = 34  

def Fibonacci(N):
    if N == 1:
        return 0
    elif N == 2:
        return 1
    else:
        return Fibonacci(N-1) + Fibonacci(N-2)

N = int(input('Digíte qual termo deve ser retornado: '))
print(Fibonacci(N))

# 0 1 1 2 3 5 8 13 21 34