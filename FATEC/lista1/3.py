d = int(input('Digite os dias: '))
h = int(input('Digite as horas: '))
m = int(input('Digite os minutos: '))
s = int(input('Digite os segundos: '))

t = (d*24*60*60) + (h*60*60) + (m*60) + s
print('O total de segundos é ', t)