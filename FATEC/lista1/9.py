km = int(input('Digite a quantidade de km rodados: '))
d = int(input('Digite a quantidade de dias alugados: '))

t= (d*60) + (km*0.15)

print('O valor total a ser pago é R$%.2f'%t)