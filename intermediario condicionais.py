#Comandos condicionais aprofundamento - capítulo 8
print('\n------------------CONDICIONAIS------------------\n')
#condicional match case
print('\n------------------MATCH CASE------------------\n')
n = -1
while n != 0:
    n = int(input('Digite um inteiro: '))
    match n:
        case 1:
            print(' você digitou um')
        case 2:
            print(' você digitou dois')
        case 3:
            print(' você digitou três')
        case _: #será true se nenhum outro acima for true, deve ser o último item
            print(' você digitou outra coisa')

print('\n\nFim do Programa')

#condicional inline
print('\n------------------INLINE------------------\n')
x = 10
y = 9
print(x) if x>= y else print(y) #usa-se quando há 1 único comando

print(f'O valor de X é {x}') if x >= y else print(f'O valor de Y é {y}')

#condicional if única linha
print('\n------------------IF ÚNICO------------------\n')
Codigos = [103, 117, 121, 135, 161, 189, 200, 204, 216] 
Lista = [] 
print('Alternativa com if clássico')
for codigo in Codigos:
    if 120 <= codigo and codigo <=200:
        Lista.append(codigo) #append --> acrescenta itens ao final da lista
print(f'    códigos filtrados --> {Lista}')

Lista = [] #esvazia a lista
print(f'Código com if de única linha')
for codigo in Codigos:
    Lista.append(codigo) if 120 <= codigo and codigo <=200 else 0 
    #o else 0 não tem funcionalidade, essa forma serve paea diminuir o codigo
print(f'    códigos filtrados --> {Lista}')

#retorno de valor com if inline
print('\n------------------IF ILINE RETORNO------------------\n')
x = int(input('Digite um inteiro: '))
paridade = 'par' if x % 2 == 0 else 'ímpar'
print(f'O valor de {x} é {paridade}')