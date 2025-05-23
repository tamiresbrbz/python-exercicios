#Escreva um programa que leia e armazene em um dicionário os seguintes dados dos 
#seus contatos: nome, número celular, email e data de aniversário.A chave deve 
#ser o nome. O valor deve ser uma tupla contendo os demais dados. Se o nome já
#existir no dicionário o programa deve perguntar se o usuário deseja alterar o
#cadastro. Ao digitar um string vazio para o nome, o programa interrompe a leitura. 
#Antes de encerrar o programa apresente os dados em um formato de tabela.
def coleta_dados():
    celular = input('Digíte o número de celular: ')
    email = input('Digíte o email: ')
    anv = input('Digíte a data de aniversário: ')
    return (celular, email, anv)

contatos = {}

while True:
    nome = input('Digíte o nome do contato (ou ENTER para sair): ').strip()
    
    if nome != '':
        if(nome in contatos):
            alterar = input('Esse contato já existe, deseja alterar? (S/N)').strip().lower()
            if alterar == 's':
                contatos[nome] = coleta_dados()          
            else:
                print('Contato mantido sem alterações.\n')
        else:
            contatos[nome] = coleta_dados()
    else:
        break

print('\n{:16} {:12} {:18} {:12}'.format('Nome', 'Celular', 'Email', 'Aniversário'))
for nome, dados in contatos.items():
    print('{:16} {:12} {:18} {:12}'.format(
        nome,
        dados[0],
        dados[1],
        dados[2],
    ))
        


            