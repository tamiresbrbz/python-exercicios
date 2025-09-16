#Escreva um programa que leia dados dos Estados brasileiros: Sigla, Nome,
#Capital e PIB. A Sigla deve ser usada como chave para o dicionário e o 
#valor deve ser uma tupla formada com (Nome, Capital, PIB). A leitura 
#termina quando um string vazio for fornecido para a Sigla. Exibir os 
#dados na tela.
Estados = {}
while True:        
    sigla = input('Digíte uma sigla: ')
    if sigla == '':
        break
    elif sigla in Estados:
        print(f'ERRO: a sigla {sigla} já existe no cadastro')
        continue

    nome = input('Digíte o nome do Estado: ')
    capital = input('Digíte a capital do Estado: ')
    pib = float(input('Digíte o pib do Estado: '))
    Estados[sigla] = (nome, capital, pib)

print("\nFim da leitura dos dados\n")

print('     {:15} {:15} {:>10}'.format('Estado', 'Capital', 'PIB (R$ bi)'))
for sigla, dados in Estados.items():
    print('({}) {:15} {:15} {:10.1f}'.format(
        sigla,
        dados[0],
        dados[1],
        dados[2] ) )