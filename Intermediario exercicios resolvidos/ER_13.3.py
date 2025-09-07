#Escreva um programa que converta uma lista de temperaturas registradas 
#na escala Fahrenheit para graus na escala Celsius. Exiba os valores
#resultantes com uma casa decimal.
#A conversão é feita com uso da seguinte fórmula:
#𝐶𝑒𝑙𝑠𝑖𝑢𝑠=(𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡−32)*5/9

TempF = [83, 91, 79, 95, 104, 100, 98]
R = [(lambda fahr: (fahr - 32) * 5 / 9) (x) for x in TempF] #função lambda dentro de uma list comprehension
print('Temperaturas em Fahrenheit e Celsius:')
for tf, tc in zip(TempF, R):
    print(f'{tf:.1f}°F = {tc:.1f}°C', end='\n') #exibe a temperatura em Fahrenheit com uma casa decimal e um espaço