# Soma do custo de fábrica com percentagem do distribuidor (28%)
# Mais impostos aplicados ao custo de fábrica (45%)
# Calcular custo do consumidor 

custoFabrica = float(input("Informe o valor de fábrica do carro: "))

porcentagemDistribuidor = custoFabrica *  0.28
porcentagemImpostos =  custoFabrica *  0.45

custoConsumidor = custoFabrica + porcentagemDistribuidor + porcentagemImpostos;

print(f"O valor que o consumidor pagará é de {custoConsumidor}")