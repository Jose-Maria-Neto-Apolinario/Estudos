print('Calculo de salario com seus 30% de periculosidade:')
print()

salario = float(input('Salario mensal:'))
print()

percentual = 30 / 100
periculosidade = salario * percentual
final = salario + periculosidade

print('O valor do salario sem o adicional de periculosidade é R${}, percentual de periculosidade é de {}%'.format(salario, percentual))
print()
print('Valor do seu adicional de periculosidade é de: R${}. Valor final do salario: R${}'.format(
    periculosidade, final))
