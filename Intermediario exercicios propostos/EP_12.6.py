#Crie uma função que receba um número de 1 a 12 e retorne nome do mês 
# correspondente. Se o valor for outro o retorno da função deve ser o 
# string "Inválido".
#Escreva o programa principal para testar a função.
def NomeMes(N):
    '''Retorna o nome do mês correspondente ao número N'''
    ListaMeses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                  'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    if 1 <= N <= 12:
        return print(f'O número {N} se refere ao mês: {ListaMeses[N-1]}')
    else:
        return print('Valor inválido! Digite um número entre 1 e 12.')

N = int(input('Digite um número entre 1 e 12: '))
NomeMes(N)
