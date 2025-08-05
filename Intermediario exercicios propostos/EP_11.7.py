#Enunciado: Escreva um programa para registrar os seguintes dados de uma frota
#de veículos de uma empresa: 
#Placa (string – chave – obrigatório todas as letras maiúsculas) 
#Marca 
#Modelo 
#Tipo (caminhão, furgão, automóvel, motocicleta, etc) 
#Kilometragem  
#Data da Compra (string no formato AAAAMMDD – ano,mês,dia) 
#O programa deve ficar em laço enquanto a Placa for digitada. O laço termina 
#quando for digitado FIM para a placa. Se for digitada uma placa com letras 
#minúsculas o programa deve convertê-las para maiúsculas com o método .upper(). 
#Para cada veículo leia todos os dados e carregue em um dicionário. Se uma 
#placa já existente for digitada o programa deve avisar que já existe, mostrar
#seus dados e se usuário quiser fazer alteração em algum dado basta digitar o
#novo valor. Para os campos em que nada for digitado deve ser mantido o valor
#já cadastrado. 
#Ao final do laço grave todos os dados em um arquivo CSV usando o caractere
#";" como delimitador. 
#Detalhe: Este  exercício  é  uma  extensão  do  exercício  proposto  10.6,
#acrescentando  a  parte  referente  à gravação do arquivo
def coleta_dados():
    marca = str(input('Digite a marca: '))
    modelo = str(input('Digite o modelo: '))
    tipo = str(input('Digite o tipo: '))
    km = float(input('Digite a kilometragem: '))
    data = str(input('Digite a data da compra (AAAAMMDD): '))
    return (marca, modelo, tipo, km, data)

veiculos = {}

placa = input('Digite a placa do veículo (ou FIM para encerrar):').upper()
while placa != 'FIM':
    if placa in veiculos:
        res = input(f'Placa {placa} já cadastrada! Deseja alterar os dados? (S/N)').lower().strip()
        if res == 's':
            veiculos[placa] = coleta_dados()
        else:
            print('Cadastro mantido!')
    else:
        veiculos[placa] = coleta_dados()
    placa = input('Digite a placa do veículo (ou FIM para encerrar):').upper()

arq = open('veiculos.csv', 'w')
arq.write('Placa;Marca;Modelo;Tipo;Kilometragem;Data da Compra\n')

for placa, dados in veiculos.items():
    arq.write(f"{placa};{dados[0]};{dados[1]};{dados[2]};{dados[3]};{dados[4]}\n")
arq.close()
print(f"Arquivo 'veiculos.csv' criado com {len(veiculos)} veículos cadastrados!!")
        


        
