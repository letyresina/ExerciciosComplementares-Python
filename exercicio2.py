# Programa que lê um valor inteiro em segundos e converte para horas, minutos e segundos 

segundos = int(input("Informe o valor inteiro em segundos que deseja converter: "))

horas = segundos // 3600

segundosRestantes = segundos % 3600
minutos = segundosRestantes // 60

segundosFinais = segundosRestantes % 60

print(f"Os segundos {segundos}, convertidos fica {horas} horas, {minutos} minutos e {segundosFinais} segundos.")