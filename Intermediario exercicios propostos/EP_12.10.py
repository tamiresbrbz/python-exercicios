#Escreva uma função que receba um parâmetro string. Essa função deve retornar True se o string for 
#palíndromo e False caso não seja. Espaços em branco, algarismos e sinais de pontuação devem ser 
#eliminados, se estiverem presentes no parâmetro. 
#Um string palíndromo é aquele que pode ser lido da esquerda para a direita e da direita para a 
#esquerda, por exemplo: IRENE RI -> elimine o espaço em branco IRENERI 
#SUBI NO ONIBUS  
#ANOTARAM A DATA DA MARATONA 
#A CARA RAJADA DA JARARACA 
#AABBCCDDCCBBAA                                   
#(não é uma frase, mas é palíndromo)
import re
def Palindromo(StringP):
    StringP = StringP.lower().replace(" ", "")
    StringP = re.sub(r'[^a-z]', '', StringP)
    StringAux = StringP[::-1]
    print(f'String tratada: {StringP}')
    
    return StringP == StringAux

x = input('Digíte uma frase ou palavra: ')
print(Palindromo(x))