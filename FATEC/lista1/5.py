m = int(input('Digite o preço da mercadoria: '))
d = int(input('Digite o percentual de desconto: '))
vd = m * d / 100
nm = m - vd
print('O novo valor é R$%.2f'%nm)