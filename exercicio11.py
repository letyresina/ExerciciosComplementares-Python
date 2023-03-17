'''

    Pão = 0,38 cada
    Broa = 4,50
    Ler a quantidade de pães e broas vendidos, soma e mostrar o valor que vai para a poupança
    Poupança = 10% do valor total (0,1)

'''

quantidadePaes = int(input("Informe o valor de pães vendidos no dia: "))

paes = 0.38 * quantidadePaes

quantidadeBroas = int(input("Informe o valor de broas vendidas no dia: "))

broas = 4.50 * quantidadeBroas

valorArrecadado = paes + broas 

poupanca = valorArrecadado * 0.1

valorTotal = valorArrecadado - poupanca

print(f"O valor que vai para a poupança é de R$ {poupanca:.2f} e o valor que fica é de R$ {valorTotal:.2f}")

