#Altere o programa anterior mudando a regra de cálculo da média final. Na
#nova regra as notas de prova P1, P2 e P3 devem ser analisadas e a menor
#nota deve ser descartada. As duas melhores notas serão chamadas de N1 e
#N2. A nota de trabalho será considerada e a nova fórmula é:
#MF = 0.4 * N1 + 0.4 * N2 + 0.2 * NT

def CalculaMedia(pNotas):
    '''Recebe o string pNotas, faz a separação dos valores, calcula e retorna a média'''
    pNotas = pNotas.split(' ')
    for i in range(len(pNotas)):
        pNotas[i] = float(pNotas[i])
    if pNotas[0] < pNotas[1] and pNotas[0] < pNotas[2]:
        N1 = pNotas[1]
        N2 = pNotas[2]
    elif pNotas[1] < pNotas[0] and pNotas[1] < pNotas[2]:
        N1 = pNotas[0]
        N2 = pNotas[2]
    elif pNotas[2] < pNotas[0] and pNotas[2] < pNotas[1]:
        N1 = pNotas[0]
        N2 = pNotas[1]
    else: #caso de empate, considerar as duas primeiras notas
        N1 = pNotas[0]
        N2 = pNotas[1]
    float(N1)
    float(N2)

    media = 0.4 * N1 + 0.4 * N2 + 0.2 * pNotas[3]
    situacao = 'APROVADO' if media >= 7 else 'REPROVADO'
    pNotas.append(media)
    pNotas.append(situacao)
    return pNotas

notas = input('Digite 4 notas (P1 P2 P3 NT): ')
resultado = CalculaMedia(notas)

print (f'P1: {resultado[0]:.1f}; ', end=' ')
print(f'P2: {resultado[1]:.1f}; ', end=' ')
print(f'P3: {resultado[2]:.1f}; ', end=' ')
print(f'NT: {resultado[3]:.1f}; -> ', end=' ')
print(f'Média: {resultado[4]:.1f}; ', end=' ')
print(f'Situação: {resultado[5]}')
print('\nFim do programa')