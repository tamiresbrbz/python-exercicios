#Escreva uma função que receba uma lista como parâmetro de entrada e retorne
# uma tupla contendo quatro valores na seguinte ordem: a soma, a média, o 
# menor e o maior valor dentre todos os elementos nela contidos. Considere 
# que nessa lista ocorram apenas números reais. Escreva um programa para 
# testar essa função, exibindo na tela os resultados.

def Estatistica(Lista):
    y = 0
    Soma = 0
    Media = 0
    for x in Lista:
        Soma = Soma + x
        Media = Media + x
    Maior = max(Lista)
    Menor = min(lista)
    Tupla = (Soma, Media/len(Lista), Maior, Menor)
    return Tupla

def ExibeEstatistica(Tupla):
    print('{:7} {:7} {:7} {:7}'.format('Soma', 'Media', 'Maior', 'Menor'))
    print(f'{Tupla[0]:4}{Tupla[1]:9}{Tupla[2]:8}{Tupla[3]:8}')

lista = input('Digite a sequência de número da lista: ')
lista = lista.split(' ')

for x in range(len(lista)):
    lista[x] = int(lista[x])

Tupla = Estatistica(lista)
ExibeEstatistica(Tupla)


