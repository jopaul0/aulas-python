def troco(valor):
    moedas = [50, 20, 10, 5, 2, 1]
    troco = []
    for moeda in moedas:
        while valor >= moeda:
            valor -= moeda
            troco.append(moeda)
    return troco
        
valor=int(input('Digite o valor: '))
print('O troco deverá ser dado com: ', troco(valor)) 

    
