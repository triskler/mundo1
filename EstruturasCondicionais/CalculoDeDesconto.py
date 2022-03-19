data = float(input("Digite o valor: "))
data2 = int(input("Digite o desconto: "))

valor = data * (data2/100)
resultado = float(data - valor)

print(f'O valor de R${data} com desconto de {data2}%:')
print(f'R${resultado}')