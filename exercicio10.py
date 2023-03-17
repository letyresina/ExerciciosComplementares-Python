'''
    Comentário em bloco (aprendido em aula!)

    Encanador ganha 80 por dia, escrever programa que recebe a quantidade de dias
    e desconta 8% (0,08) de imposto de renda!

'''

dias = int(input("Informe a quantidade de dias que o encanador trabalhará: "))

salarioBruto = dias * 80.00

porcentagem = salarioBruto * 0.08

salarioLiquido = salarioBruto - porcentagem

print(f"O salário líquido é de R$ {salarioLiquido}")

