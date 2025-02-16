c = int(input('Digite a quantidade de cigarros fumados por dia: '))
a = int(input('Digite a quantidade de anos fumados: '))

t = (c*10/1440)*(a*365)

print('A redução de vida foi de %d dias'%t) 