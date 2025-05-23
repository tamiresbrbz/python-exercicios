#Escreva um programa para registrar os seguintes dados de uma frota de 
# veículos de uma empresa:
#Placa (string – chave – obrigatório todas as letras maiúsculas)
#Marca
#Modelo
#Tipo (caminhão, furgão, automóvel, motocicleta, etc)
#Kilometragem
#Data da Compra (string no formato AAAAMMDD – ano,mês,dia)
#O programa deve ficar em laço enquanto a Placa for digitada. O laço 
#termina quando for digitado FIM para a placa. Se for digitada uma placa
#com letras minúsculas o programa deve convertê-las para maiúsculas com o
#método .upper().
#Para cada veículo leia todos os dados e carregue em um dicionário. Se uma
#placa já existente for digitada o programa deve avisar que já existe, 
#mostrar seus dados e se usuário quiser fazer alteração em algum dado 
#basta digitar o novo valor. Para os campos em que nada for digitado deve 
#ser mantido o valor já cadastrado.
#Ao final do laço mostre os dados na tela com uma formatação legível.
#Desafio Inclua no programa uma validação da placa, seguindo as seguintes regras:
#a) Deve ter 7 caracteres
#b) Os três primeiros devem ser letras
#c) Os caracteres 4, 6 e 7 devem ser algarismos
#d) O caractere 5 pode ser número (placa antiga) ou letra (nova placa padrão Mercosul)
def coleta_dados():
    marca = input('Digite a marca: ')
    modelo = input('Digite o modelo: ')
    tipo = input('Digite a tipo: ')
    km = int(input('Digite a kilometragem: '))
    data = input('Digite a data da compra: ')
    return(marca, modelo, tipo, km, data)

def valida_placa(placa):
    if len(placa) != 7:
        return False
    elif not placa[:3].isalpha():
        return False
    elif not placa[3].isdigit():
        return False
    elif not placa[4].isalnum():
        return False
    elif not placa[5].isdigit():
        return False
    elif not placa[6].isdigit():
        return False
    else:
        return True


veiculos = {}

while True:
    placa = input('Digíte a placa do veículo (Ou fim para encerrar): ')
    placa = placa.upper()

    if placa == 'FIM':
        break

    elif not valida_placa(placa):
        print('\nPlaca inválida! Tente novamente')
        continue
    
    elif placa in veiculos:
        print(f'\n{placa}: {veiculos[placa]}')
        x = input('A placa já existe no cadastro, deseja alterar?(S/N): ').strip().lower()
        if x == 's':
            veiculos[placa] = coleta_dados()
        else:
            print('Cadastro mantido sem alteração\n')
    else:
        veiculos[placa] = coleta_dados()
    
print(f'{"Placa":<10} {"Marca":<15} {"Modelo":<15} {"Tipo":<15} {"Kilometragem":<15} {"Data compra":<15}')
for placa, dados in veiculos.items():
    print(f'{placa:<10} {dados[0]:<15} {dados[1]:<15} {dados[2]:<15} {dados[3]:<15} {dados[4]:<15}')