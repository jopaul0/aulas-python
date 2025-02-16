def multa(peso):
    if peso <= 50:
        multa=0
        excesso=0
    else:
        excesso= peso - 50
        multa = excesso * 4

    return excesso, multa
    

peso = float(input('Digite o peso dos peixes: '))
excesso, multa = multa(peso)
print(f'Excesso de peso: {excesso:.2f} kg')
print(f'Multa: R${multa:.2f}')