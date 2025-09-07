#No exercício resolvido 12.4 não foi feita uma validação do código lido
#do teclado. Sendo assim, experimente digitar códigos que são menores que
#10000 ou maiores que 99999 e veja o que acontece.
#Em seguida implemente a validação do código lido e só efetue o cálculo 
#do dígito verificador se ele for válido.

def Valida(cod):
    if cod == 0:
        return cod
    elif cod < 10000 or cod > 99999:
        print('Código inválido. Deve ser um número de 5 dígitos.')
        codigo = int(input('Digite um código de 5 dígitos (0 para encerrar): '))
        Valida(codigo)
    else:
        return cod
         
def CalcDigito(cod):
    s = str(cod)
    dv = 0
    peso = 2
    for a in s:
        dv += peso * int(a)
        peso += 1
    return dv % 7

codigo = int(input('Digite um código de 5 dígitos (0 para encerrar): '))
Valida(codigo)
while codigo > 0:
    digito = CalcDigito(codigo)
    print(f'Código: {codigo} - Dígito verificador: {digito}')
    codigo = int(input('Digite um código de 5 dígitos (0 para encerrar): '))
    Valida(codigo)
print('Fim do programa')