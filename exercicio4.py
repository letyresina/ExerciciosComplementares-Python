# Programa que faz conversão de real para dólar 

real = float(input("Informe o valor do real que deseja converter: "))

cotacaoDolar = float(input("Informe o valor da cotação do dólar: "))

conversao = real * cotacaoDolar

print(f"O valor R$ {real} convertido em dólar é de $ {conversao}")