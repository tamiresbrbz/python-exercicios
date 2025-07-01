__version__ = "0.0.1"
__author__ = "Tamires"
__license__ = "Unlicense"

numeros = list(range(1, 11))

for numero in numeros:
    print("Tabuada do", numero)
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


