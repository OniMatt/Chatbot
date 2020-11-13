import random

#randomiza as cidades das rotas

substring1 = "caminhão 1"
substring2 = "caminhão 2"
substring3 = "caminhão 3"
substring4 = "caminhao"
substring5 = "bom dia"
substring6 = "caminhão"
substring7 = 'caminhao 1'
substring8 = "caminhao 2"
substring9 = "caminhao 3"
substring10 = "oi"
substring11 = "tchau"
substring12 = "obrigado"
substring13 = "obrigada"

#strings que o chatbot reconhece.

cityList1 = ['Canoas', 'Esteio', 'Sapucaia', 'São Leopoldo', 'Portão', 'São Sebastião do Caí', 'São Vendelino']

#rota serra

cityList2 = ['Gravataí', 'Glorinha', 'Santo Antônio da Patrulha', 'Osório']

#rota litoral

cityList3 = ['Eldorado do Sul', 'Guaíba', 'Butiá', 'Sentinela do Sul', 'Camaquã', 'Cristal', 'São Lourenço do Sul', 'Três Vendas']

#rota região sul

fullstring = ""

fullstring = input("Nos pergunte sobre algum caminhão!:")

#input do usuário.

while fullstring != "sair":

    if substring1 in fullstring:
        print("Caminhão 1 saiu de Porto Alegre ao meio dia em destino à Carlos Barbosa")
        print("Carregando um kit de facas")
        print("Atualmente em:", random.choice(cityList1))
    elif substring2 in fullstring:
        print("Caminhão 2 saiu de Canoas ontem às 9:30 em destino à Tramandaí")
        print("Carregando dois ármarios")
        print("Atualmente em:", random.choice(cityList2))
    elif substring3 in fullstring:
        print("Caminhão 3 saiu de Canoas às 13:24 em destino à Pelotas")
        print("Carregando um jogo de panelas")
        print("Atualmente em:", random.choice(cityList3))
    elif substring6 in fullstring:
        print("Especifique entre os caminhões: 1, 2 ou 3")
    elif substring7 in fullstring:
        print("Caminhão 1 saiu de Porto Alegre ao meio dia em destino à Carlos Barbosa")
        print("Carregando um kit de facas")
        print("Atualmente em:", random.choice(cityList1))
    elif substring8 in fullstring:
        print("Caminhão 2 saiu de Canoas ontem às 9:30 em destino à Tramandaí")
        print("Carregando dois ármarios")
        print("Atualmente em:", random.choice(cityList2))
    elif substring9 in fullstring:
        print("Caminhão 3 saiu de Canoas às 13:24 em destino à Pelotas")
        print("Carregando um jogo de panelas")
        print("Atualmente em:", random.choice(cityList3))
    elif substring4 in fullstring:
        print("Especifique entre os caminhões: 1, 2 ou 3")
    elif substring5 in fullstring:
        print("Bom dia meu campeão, veio rastrear seu caminhão? Nos pergunte sobre ele!")
    elif substring10 in fullstring:
        print('Oi! Veio rastrear algum caminhão? Escolha entre 1, 2 e 3!')
    elif substring11 in fullstring:
        print("Obrigado por usar nosso chatbot, até a próxima!")
        quit()
    elif substring12 in fullstring:
        print("De nada!, mais alguma pergunta?")
    elif substring13 in fullstring:
        print("De nada!, mais alguma pergunta?")
    fullstring = input("Nos pergunte sobre algum caminhão!:")

#respostas que o bot pode usar dependendo da frase usada.