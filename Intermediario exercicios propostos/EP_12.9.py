#Escreva uma função que receba uma lista de números inteiros e elimine os eventuais elementos 
#repetidos nela contidos e a retorne.  
#Dentro da função use a classe set. 
#Escreva o programa principal para testar a função.
def EliminaDuplicatas(Lista):
    Nova = set(Lista)
    return Nova

Lista = [23, 45, 65, 2, 1, 2, 45, 23]
print(Lista)
print(EliminaDuplicatas(Lista))