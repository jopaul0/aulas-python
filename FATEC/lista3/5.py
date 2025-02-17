def euclides(a,b):
    while True:
        if a==0:
            return b
        elif b==0:
            return a
        elif a%b==0:
            return b
        else:
            a,b = b,a%b
        

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

print(f'O MDC é {euclides(a,b)}')