# Programa que calcula porcentagem de voto branco, nulo e válido em base da base total

votoBranco = int(input("Informe a quantidade de votos brancos: "))

votoNulo = int(input("Informe a quantidade de votos nulos: "))

votoValido = int(input("Informe a quantidade de votos válidos: "))

quantidadeTotal = votoBranco + votoNulo + votoValido 

porcentagemBranco = (votoBranco * 100) / quantidadeTotal

#Exemplo de formatação para mostrar somente os dois primeiros para usuário: 
# print(f"Teste {porcentagemBranco:.2f}")

porcentagemNulo = (votoNulo * 100) / quantidadeTotal

porcentagemValido = (votoValido * 100) / quantidadeTotal

print(f"O porcentual de votos brancos são de {porcentagemBranco:.2f}%")
print(f"O porcentual de votos nulos são de {porcentagemNulo:.2f}%")
print(f"O porcentual de votos válidos são de {porcentagemValido:.2f}%")

