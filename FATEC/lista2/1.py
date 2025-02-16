class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if (a+b>c) and (a+c>b) and (b+c>a):
            self.triangle= True
        else:
             self.triangle= False
    
    def whatTriangle(self):
        if self.triangle:
            if self.a == self.b == self.c:
                print('O triângulo é equilátero.')
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                print('O triângulo é isósceles.')
            else:
                print('O triângulo é escaleno.')
        else:
            print('Não é possível formar um triângulo com essas medidas')

lado1 = float(input('Digite o primeiro lado do triângulo: '))
lado2 = float(input('Digite o segundo lado do triângulo: '))
lado3 = float(input('Digite o terceiro lado do triângulo: '))

triangulo = Triangle(lado1,lado2,lado3)
triangulo.whatTriangle()