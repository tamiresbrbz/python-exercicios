import time
print("------------------------------OLÁ MUNDO DO PYTHON-----------------------------")

print("Olá, mundo!")
time.sleep(2)
print("Agora sou uma programadora de Python.")
print("Aguarde 1.5 segundos")
time.sleep(1.5)
print("Última linha do programa\n")
print("------------------------------CLASSE DE OBJETOS-----------------------------")

class Carro:
    def __init__(self, cor='preto', ano='2025'): #esse dados vão aparecer caso o objeto seja chamado e não seja atribuido dados a ele
        self.rodas = 4
        self.volante = 1
        self.bancos = 3
        self.cor = cor
        self.ano = ano

    def cordocarro(self):
        print('A cor do carro é ' + self.cor)
    
    def anocarro(self):
        print('O carro é do ano ' + self.ano)

meucarro = Carro('vermelho', '2018')
meucarro.cordocarro()
meucarro.anocarro()

print("Última linha do programa\n")
print("-----------------------------ESTRUTURA DE DADOS-----------------------------")

lVazia = [] #aqui cria-se uma lista vazia
print(lVazia)

lNumeros = [1, 2, 3]
print(lNumeros)

valor = True
lDados = [77, 'ovo', valor, lNumeros] #lista mista com varios tipos de dados
print(lDados)

print (len(lDados)) #conta a quantidade de dados da lista

lDados.append(965) #acrescenta um ítem à lista
print(lDados)

print (len(lDados)) #conta novamente a quantidade de dados da lista

tupla = (2, 3, 4) #parece com a lista mas não aceita acrescimo de dados, nem deletar dados, ela não pode
print( tupla)     #ser modificada dps de criada, é útil para aumentar o processamento do pc, pois ele vai saber exatamente a memória utilizada

conjunto_num = {1, 2, 3, 1, 2}#set --> os elementos não se repetem
print(conjunto_num) #os números repetidos não aparecem
print(len(conjunto_num))

dicionario = {'gato': 'felino domesticado', 'banana': 'fruta amarela', 
              'legenda':'829', 'cidade': 'San Andreas', 'residente': True}
print(dicionario['gato'])
print(dicionario['banana'],'\n',dicionario['cidade']) #o dicionario armazena informações em variaveis

A = []
A.append(12) #acrescenta o número ao final da lista
A.append(11)
A.append(90)
print(A)

print("Última linha do programa\n")
print("-----------------------------FUNÇÃO-----------------------------")

def somaNumeros(A, B): #cria uma função
    return A + B 

print(somaNumeros(3, 7))

def divideesoma (A, B, C): #cria mais uma função
    D = A + B
    D = D/C
    return D 

print(divideesoma(4, 5, 6))

print("Última linha do programa\n")
print("-----------------------------VARIAVEIS E TIPO DE DADOS-----------------------------")

inteiro = '10'
decimal = '5.5'
complexo = '5+4j'
simples = 'Maria gosta de flores'
duplas = "João gosta de frutas"
tripla = '''Samira é programadora'''
samiraFlorista = 'False'
samiraProgramadora = 'True'

print('o numero', decimal, 'é um decimal') 
print('Samira é uma programadora?', samiraProgramadora)
print(complexo)
print(inteiro, end='...') #muda o último ítem do print pelo estipulado, por padrão possui pulo de linha
print(decimal) 
print(decimal, inteiro, sep='<-->') #troca o separador pelo estipulado nas aspas
print('um\tdois\ttrês') #cria uma tabulação
print('um\ndois\ntrês') #pula linha

print("Última linha do programa\n")
print("-----------------------------BOOLEANO-----------------------------")

lista = [12, 26, 65, 87, None]

for valor in lista:
    if bool(valor) == True:
        print(f'{valor} é um número válido')
    else:
        print(f'{valor} é um valor vazio')

print("Última linha do programa\n")
print("-----------------------------STRING-----------------------------")

texto = "Estou estudando Python no 'LinkedIn Learning'"
print(texto)
print(texto[0])
print(texto[16:22])
print(texto[26:]) #fatiamente inicio:final
print(texto.lower()) #formata a string para ter apenas letras minusculas
print(texto.upper()) #formata a string para ter apenas letras maiusculas
print(texto.title()) #torna todas as letras iniciais maiusculas
print(texto.capitalize()) #torna apenas a primeira letra da frase maiuscula

from datetime import datetime
print(f'Data e horário atual: {datetime.now()}')
a = 4
b = 3

print('A divisão de {} por {} é {:.3f}'.format(a, b, a/b)) #format define o formato do dado ':.3f' define que havera apenas 3 casas decimais depois da vírugla

a = 'olá mundo'
b = 'Alfred'

print('{0}, me chamo {1}'.format(a, b)) #format define onde as variáveis ficam
print('{1}, me chamo {0}'.format(a, b)) #define onde elas ficam e como aparecem
print('{}, me chamo {}'.format(a, b))
print('{c}, me chamo {d}'.format(c='Olá', d='Bruce'))

print("Última linha do programa\n")
print("-----------------------------NUMERICO-----------------------------")

print(type(2))
print(type(2.56))
print(type(2.56+2))
print(type(2+2))
print(round(2.56, 1)) #arredonda números, segundo parametro é a quantidade de casas decimais

print("Última linha do programa\n")
print("-----------------------------OPERADORES-----------------------------")
A = 7
B = 9
#Operadores aritméticos
C = A + B
print(C)
C = A * B
print(C)
C = 'Maçã' + '-' + 'Verde'
print(C)
C = 3 * 'Piu '
print(C)
C = A ** B
print(C)
C = A - B
print(C)
C = B/B
print(C)
C = B//A #resulta na parte inteira da divisão
print(C)
C = B%A
print(C)
C = A * B + A - B
print(C)
#Operadores relacionais --> resultam em valores true ou false
C = A > B
print(C)
C = A < B
print(C)
C = A == B
print(C)
C = A != B
print(C)
print ('ser' == 'Folhas')
s1 = 'Valores: A é {} e B é {}'.format(A, B) #.format --> formas de incluir valores em prints
s2 = f'Valores: A é {A} e B é {B}' #fString --> --> formas de incluir valores em prints
print(s1)
print(s1)
#Operadores lógicos --> retornam false ou true
C = 10 in [1, 2, 3, 4, 5] 
print(C)
C = 'mar' in 'amar' #in --> está contido em
print(C)
C = 'mar' not in 'amar' #not in --> não está contido em
print(C)
C = 'atar' not in 'amar'
print(C)
#função input e seu comportamento
N = input('Digite um numero: ')
print(N)
F = input('Digite um numero: ')
print(F)
R = N + F 
print(R) #vai retornar os números concatenados, pq ele entende como string
N = int(N) #converte uma string em numero inteiro
print(N)
F = float(F) #converte uma string em numero decimal
print(F)
R = N + F #agora que os números foram convertidos ele soma como int e float
print(R)
R = N * F
print(R)
B = int(input ('Digite um numero inteiro: ')) #o número da entra no input convertido
print(B)

print("Última linha do programa\n")
print("-----------------------------TRATAMENTO DE ESCEÇÕES-----------------------------")

#protege o programa contra erros, trata os erros do programa
try:
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    r = a / b
    print('o resultado é:', r)
except ZeroDivisionError:
    print('O valor de B não pode ser zero')
except ValueError:
    print('Digíte números inteiros para A e B')
except:
    print('Erro ao receber o número')
print('Fim do programa!\n\n')

import this