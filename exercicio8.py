# Programa que lê o valor do salário e dá um aumento de 25%
# 25% == 0.25

salario = float(input("Informe o valor do salário do funcionário: "))

aumentoPorcentagem = salario * 0.25

salarioFinal = salario + aumentoPorcentagem

print(f"O salário final será de {salarioFinal}")