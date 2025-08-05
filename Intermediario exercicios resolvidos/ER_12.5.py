from random import randint

def CarregaLista(qtde, a, b):
    '''carrega uma lista com qtde elementos aleatórios entre a e b'''
    L = []
    for i in range(qtde):
        L.append(randint(a, b))
    return L

q = int(input("Digíte a quantidade desejada: "))
lmin = int(input("Digite o limite mínimo: "))
lmax = int(input("Digite o limite máximo: "))
valores = CarregaLista(q, lmin, lmax)
print(f"Lista gerada >> {valores}")
print(f"A lista gerada tem {q} elementos")
