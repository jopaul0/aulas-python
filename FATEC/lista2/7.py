import math
def calculaTinta(m2):
    litros = m2/3
    latas = math.ceil(litros/18)
    valor = latas * 80
    return litros,latas,valor

m2 = float(input('Digite a área em metros quadrados: '))
litros,latas,valor = calculaTinta(m2)
print(f'Você precisará de {litros:.2f} L de tinta.\nVocê precisará de {latas} latas de tinta.\nO valor total será de R$ {valor:.2f}.')