#Escreva um programa que calcule a somatória de todos os números inteiros contidos em uma lista. 
#Implemente essa solução usando uma função recursiva. 
#Use fatiamento. Considere que L = L[0] + L[1:], ou seja, uma lista pode ser entendida como sendo a 
#união de seu primeiro elemento ( L[0] ) com o resto da lista (fatiamento L[1:]).  
#O caso base ocorre quando L está vazia, len(L) == 0, e enquanto len(L) > 0 ocorre o caso recursivo.
def CalculaSomatoria(Lista):
    if len(Lista) > 1:
        Lista[0] = Lista[0] + Lista [-1]
        Lista.pop(-1)
        CalculaSomatoria(Lista)
    else:
        return Lista

Lista = [12, 5, 6, 4, 3]
CalculaSomatoria(Lista)
print(Lista)