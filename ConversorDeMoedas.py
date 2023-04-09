'''''#exercicio de conversor de moeda
r=float(input('Quanto de dinheiro voce tem na carteira? R$'))
d=r/5.61
print('Com R${:.2f} voce compra US${:.2f}'.format(r,d))'''

import requests
import json
'''Link da API de importações e seleção das moedas'''
cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL,PYG-BRL,JPY-BRL')
cotacao = cotacao.json()
dolar = cotacao['USDBRL']["bid"]
euro = cotacao['EURBRL']["bid"]
libra = cotacao['GBPBRL']["bid"]
iene = cotacao['JPYBRL']["bid"]
guaraniparaguaio = cotacao['PYGBRL']["bid"]
bitcoin = cotacao['BTCBRL']["bid"]


'''Inicio do programa'''
print('-'*50)
pergunta = float(input('Quantos reais você quer converter? R$ '))
opcao = 0
while opcao != 7:
    print('''  
    Para qual moeda voce quer converter?
    \033[31m[1]\033[m - Dólar
    \033[31m[2]\033[m - Euro
    \033[31m[3]\033[m - Libra
    \033[31m[4]\033[m - Iene
    \033[31m[5]\033[m - Guarani Paraguaio
    \033[31m[6]\033[m - Bitcoin
    \033[31m[7]\033[m - Sair do programa''')
    print('-' * 50)
    opcao = int(input('Digite uma das opções acima: '))
    if opcao == 1:
        m1 = float(pergunta) / float(dolar)
        print('Dólar = US$\033[34m{}\033[m. Com R$\033[34m{}\033[m você compra US$\033[34m{:.2f}\033[m dolares'.format(dolar, pergunta, m1))
    if opcao == 2:
        m2 = float (pergunta) / float(euro)
        print('Euro = €\033[34m{}\033[m. Com R$\033[34m{}\033[m você compra €\033[34m{:.2f}\033[m Euros'.format(euro, pergunta, m2))
    if opcao == 3:
        m3 = float(pergunta) / float(libra)
        print('Libra = £\033[34m{}\033[m. Com R$\033[34m{}\033[m você compra £\033[34m{:.2f}\033[m Libras'.format(libra, pergunta, m3))
    if opcao == 4:
        m4 = float(pergunta) / float(iene)
        print('Iene = ¥\033[34m0.050\033[m. Com R$\033[34m{}\033[m você compra ¥\033[34m{:.2f}\033[m Ienes'.format(iene, pergunta, m4))
    if opcao == 5:
        m5 = float(pergunta) / float(guaraniparaguaio)
        print('Guarani Paraguaio = ₲\033[34m{}\033[m. Com R$\033[34m{}\033[m você compra ₲\033[34m{:.2f}\033[m Guaranis'.format(guaraniparaguaio, pergunta, m5))
    if opcao == 6:
        m6 = float(pergunta) / float(bitcoin)
        print('Bitcoin = ₿\033[34m{}\033[m. Com R$\033[34m{}\033[m você compra ₿\033[34m{:.2f}\033[m Bitcoins'.format(bitcoin, pergunta, m6))
    if opcao == 7:
        print('Programa finalizado')# ConversorDeMoedas
