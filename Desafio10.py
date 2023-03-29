


'''''#exercicio de conversor de moeda
r=float(input('Quanto de dinheiro voce tem na carteira? R$'))
d=r/5.61
print('Com R${:.2f} voce compra US${:.2f}'.format(r,d))'''

print('-'*50)
pergunta = float(input('Quanto de dinheiro você tem? R$ '))
opcao = 0
while opcao != 5:
    print('''  
    Qual Moeda voce quer converter?
    \033[31m[1]\033[m - Dólar
    \033[31m[2]\033[m - Euro
    \033[31m[3]\033[m - Libra
    \033[31m[4]\033[m - Iene
    \033[31m[5]\033[m - Sair do programa''')
    opcao = int(input('Digite uma das opções acima: '))
    if opcao == 1:
        m1 = pergunta / 5.53
        print('Dólar = US$\033[34m5.74\033[m. Com R$\033[34m{}\033[m você compra US$\033[34m{:.2f}\033[m dolares'.format(pergunta, m1))
    if opcao == 2:
        m2 = pergunta / 6.34
        print('Euro = €\033[34m6.47\033[m. Com R$\033[34m{}\033[m você compra €\033[34m{:.2f}\033[m Euros'.format(pergunta, m2))
    if opcao == 3:
        m3 = pergunta / 7.71
        print('Libra = £\033[34m7.71\033[m. Com R$\033[34m{}\033[m você compra £\033[34m{:.2f}\033[m Libras'.format(pergunta, m3))
    if opcao == 4:
        m4 = pergunta / 0.050
        print('Iene = ¥\033[34m0.050\033[m. Com R$\033[34m{}\033[m você compra ¥\033[34m{:.2f}\033[m Ienes'.format(pergunta, m4))
    if opcao == 5:
        print('Programa finalizado')# ConversorDeMoedas
