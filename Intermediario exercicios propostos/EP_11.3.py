#Enunciado: Escreva um programa que leia um número inteiro N (10 < N < 10.000) e grave um arquivo com N linhas
#com os dados listados na tabela abaixo. O arquivo deve ter o nome 'Estoque.csv e deve usar o
#caractere ';' (ponto e vírgula) como delimitador. Não é necessário que o arquivo esteja ordenado.
#Campo Descrição
#Código do produto Número inteiro entre 10000 e 50000. Gerar aleatórios. Não pode haver
#repetição deste código e pede-se que não sejam sequenciais.
#Quantidade em estoque Número inteiro entre 1 e 3800. Gerar aleatórios.
#Preço unitário compra Número real entre 1.80 e 435.90. Gerar aleatórios.
#Alíquota do ICMS Alíquota do imposto ICMS. Essa alíquota deve ser 7%, 12% ou 18%. (Não
#colocar o caractere '%' no arquivo). Gerar aleatórios.
#Dicas/sugestões (você pode segui-las ou não – é sua escolha)
#- Para garantir que Código do Produto não tenha repetidos use um dicionário na geração dos dados.
#- Gere os dados e coloque no dicionário. Depois grave no arquivo de saída.
#- O valor dos elementos do dicionário pode ser no formato de tupla ou de dicionário aninhado.
arq = open('Estoque.csv', 'w')
produtos = {}
n = 0
import random

while n < 10 or n > 10000:
    n = int(input("Digite a quantidade de produtos (10 < N < 10000): "))
    if(n<10 or n>10000):
        print("Número inválido. Deve ser entre 10 e 10000.\nTente novamente!\n")
    else:
        while len(produtos) < n:
            codigo = random.randint(10000, 50000)
            if codigo not in produtos:
                produtos[codigo] = {
                    'quantidade': random.randint(1, 3800),
                    'preco_unitario': random.uniform(1.80, 435.90),
                    'aliquota_icms': random.choice([7, 12, 18])
                }
        arq.write("Código do produto;Quantidade em estoque;Preço unitário;Alíquota do ICMS\n")
        for codigo, dados in produtos.items():
            arq.write(f'{codigo};{dados["quantidade"]};{round(dados["preco_unitario"], 2)};{dados["aliquota_icms"]}\n')
        arq.close()
        print(f"Arquivo 'Estoque.csv' criado com {n} produtos!!")


