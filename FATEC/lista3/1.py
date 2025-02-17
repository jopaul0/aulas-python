def isTriangle(number):
    if number < 0:
        return False
    
    x=0
    while True:
        produto = x * (x+1) * (x+2)
        x+=1
        if produto == number:
            return True
        elif produto>number:
            return False
        
    
number = int(input('Digite um número: '))
if isTriangle(number):
    print(f'O número {number} é triagular.')
else:
    print(f'O número {number} não é triagular.')