def whatBigger(number1,number2,number3):
    if number1 > number2 and number1 > number3:
        return number1
    elif number2 > number3:
        return number2
    else:
        return number3
    
number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))
number3 = int(input('Digite o terceiro número: '))

print(f'O maior número é o {whatBigger(number1,number2,number3)}')
