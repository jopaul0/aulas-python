s = int(input('Digite o valor do salário: '))
p = int(input('Digite a porcentagem do aumento (sem o %): '))

a = s * p / 100
ns = s+a

print('O novo salário é R$ %.2f'% ns)