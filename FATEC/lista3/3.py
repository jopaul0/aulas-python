def primo(valor):
    if valor <= 1:
        return False
    divisores=0 

    for x in range(1, valor+1):
        if x!=0 and valor % x == 0:
            divisores += 1
    
    if divisores==2:
        return True
    else:
        return False

valor = int(input('Digite um número: '))
if primo(valor):
    print(f'{valor} é um número primo')
else:
    print(f'{valor} não é um número primo')