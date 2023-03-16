# Calcular um valor qualquer de um produto com o desconto de 12%, em que 12% = 0,12 

valorProduto = float(input("Informe o valor do produto: "))

desconto = valorProduto * 0.12

valorFinal = valorProduto - desconto

print(f"O valor {valorProduto} com desconto de 12% é de {valorFinal}")