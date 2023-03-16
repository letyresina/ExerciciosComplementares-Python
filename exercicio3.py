# Receber a quantidade de frangos para calcular os gastos com a automatização
# No pé direito, um chip de identificação que custa 0,40 centavos
# No pé esquerdo, dois anéis para indicar o tipo de alimento que deve consumir custando 0,35 centavos
# Em que: 0,35 x 2 = 0,70 centavos 

frango = int(input("Informe a quantidade de frangos que possui nesse lote: "))

custoID = frango * 0.40

custoAnel = frango * 0.70

custoTotal = custoID + custoAnel 

print(f"O custo total com {frango} frangos é de {custoTotal}")

