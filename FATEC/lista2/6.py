def salario(ganhoPorHora, horasTrabalhadas):
    salarioBruto= ganhoPorHora * horasTrabalhadas
    ir = salarioBruto * 0.11
    inss = salarioBruto * 0.08
    sindicato = salarioBruto * 0.05
    salarioLiquido = salarioBruto - ir - inss - sindicato
    return salarioBruto,ir,inss,sindicato,salarioLiquido

ganhoPorHora= float(input('Digite o quanto você ganha por hora: '))
horasTrabalhadas=int(input('Digite a quantidade de horas trabalhadas no mês: '))
salarioBruto,ir,inss,sindicato,salarioLiquido = salario(ganhoPorHora,horasTrabalhadas)

print(f'Salário Bruto: R${salarioBruto:.2f}')
print(f'IR: R${ir:.2f}')
print(f'INSS: R${inss:.2f}')
print(f'Sindicato: R${sindicato:.2f}')
print(f'Salário Liquido: R${salarioLiquido:.2f}')

