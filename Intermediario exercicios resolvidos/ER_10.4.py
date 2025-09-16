#Escreva um programa que leia dados dos Estados brasileiros: Sigla, Nome,
# Capital e PIB. A Sigla deve ser usada como chave para o dicionário e o 
#valor deve ser um dicionário aninhado contendo os objetos Nome, Capital 
#e PIB. Um string vazio para a Sigla termina a leitura. Exibir os dados 
#na tela.
Estados = {}
print('Leitura de dados')
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
    dictItem = {'nome': nome, 'capital': capital, 'pib': pib}
    Estados[sigla] = dictItem

print("\nFim da leitura dos dados\n")

print('     {:15} {:15} {:>10}'.format('Estado', 'Capital', 'PIB (R$ bi)'))
for sigla, dados in Estados.items():
    print('({}) {:15} {:15} {:10.1f}'.format(
        sigla,
        dados['nome'],
        dados['capital'],
        dados['pib'] ) )