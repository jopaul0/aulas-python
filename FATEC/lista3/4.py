def fibonacci(valor):
    if valor==1 or valor == 2:
        return True, 1
    elif valor<1:
        return False
    
    a,b = 1,1
    for x in range(3,valor+1):
        a,b = b,a+b

    return True, b

valor=int(input('Digite um número: '))

result,number = fibonacci(valor)
if result:
    print(f'O {valor}º número da sequência de Fibonacci é {number}.')
else:
    print(f'O {valor}º número da sequência de Fibonacci não existe.')