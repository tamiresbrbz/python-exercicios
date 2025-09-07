#No exercício resolvido 12.2 foi usado o comando condicional clássico. 
#Altere o código dentro da função substituindo o if-else clássico por um 
#if de única linha.

def Paridade(a):
    return 'Par' if a % 2 == 0 else 'Ímpar'

n = int(input('Digite um número inteiro: '))
print(f'O número {n} é {Paridade(n)}')