# Escreva uma função que carregue e retorne uma lista com todos os 
# elementos da sequência de Fibonacci menores que um parâmetro passado à 
# função.
# Escreva o programa principal para testar a função.
# A sequência de Fibonacci é definida da seguinte forma: a) os dois 
# primeiros termos da sequência são 0 e 1. Do terceiro termo em diante 
# cada termo é a soma dos dois anteriores.
# Caso de teste: Se ValorLimite = 120, então a sequência é:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

def Fibonacci(Limite):
    '''Retorna uma lista com os elementos da sequência de Fibonacci menores que o limite'''
    ListaFib = [0, 1]
    Prox = 0
    while Prox <= Limite:
        Prox = ListaFib[-1] + ListaFib[-2]
        ListaFib.append(Prox)
        ListaFib.pop() if Prox > Limite else None
    return ListaFib

Limite = int(input('Digite um valor limite para a sequência de Fibonacci: '))
print(f'Sequência de Fibonacci com valores menores que {Limite}: {Fibonacci(Limite)}')