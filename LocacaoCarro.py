data = int(input("Quantos dias estava em posse do carro: "))
data2 = float(input("Numero de kilometros rodados: "))

resultado = (60 * data) + (data2 * 0.15)
print(f'O valor a pagar é de R${resultado}')