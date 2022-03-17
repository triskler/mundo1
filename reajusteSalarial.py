data = float(input("Digite o sálario do funcionario: "))
data2 = int(input("Digite o reajuste: "))

valor = data * (data2/100)
resultado = data + valor
print(f'O salário do funcionário passou de R${data} para R${resultado} aplicando {data2}% de reajuste.')
