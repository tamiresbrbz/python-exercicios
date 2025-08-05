#Escreva uma função que receba como parâmetro de entrada dois números reais Min 
# e Max. Essa função deve ler do teclado um número real e retorná-lo caso esteja 
# dentro do intervalo fechado [Min, Max]. Caso contrário, a função deve exibir 
# uma mensagem de erro e ler um novo valor.
def LeReal(pLMin, pLMax):
    a = float(input(f'Digite um valor real: '))
    while a < pLMin or a > pLMax:
        print(f'O valor {a} está fora dos limites [{pLMin}, {pLMax}]')
        a = float(input('Digite um valor real novamente: '))
    return a

LMin = float(input('Digite o valor mínimo: '))
LMax = float(input('Digite o valor máximo: '))
controle = 's'
while controle.lower() == 's':
    valor = LeReal(LMin, LMax)
    print(f'O valor lido é {valor}')
    controle = input('Deseja digitar outro valor (s/n)? ')
print('Fim do programa')
