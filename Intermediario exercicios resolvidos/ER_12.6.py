# Exercício Resolvido 12.6 - Enuncioado contido no Ebook

def CalculaMedia(pNotas):
    '''Rece o string pNotas, faz a separação dos valores, calcula e retorna a média'''
    pNotas = pNotas.split(' ')
    for i in range(len(pNotas)):
        pNotas[i] = float(pNotas[i])
    media = (pNotas[0] + pNotas[1] + pNotas[2]) * 0.3 + pNotas[3] * 0.1
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