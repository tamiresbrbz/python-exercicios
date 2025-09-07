#Crie uma função que receba um ângulo em graus, e retorne esse ângulo 
# convertido para radianos. O valor de PI está disponível no módulo math.
#  Importe o módulo e use math.pi
#Escreva o programa principal para testar a função.
#Regra AngRadiano = AngGraus * PI / 180
import math
def rad(graus):
    '''Converte o ângulo em graus para radianos'''
    angRad = graus * math.pi / 180
    return angRad

g = float(input('Digite um ângulo em graus: '))
print(f'O ângulo {g} em radianos é: {rad(g)}')