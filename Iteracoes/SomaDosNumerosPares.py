data = int(input("Digite o primeiro numero: "))
data2 = int(input("Digite o segundo numero: "))
data3 = int(input("Digite o terceiro numero: "))
data4 = int(input("Digite o quarto numero: "))
data5 = int(input("Digite o quinto numero: "))
data6 = int(input("Digite o sexto numero: "))

conta = 0
lista = [data, data2, data3, data4, data5, data6]

for i in range(0, 6):
    if lista[i] % 2 == 0:
        conta += lista[i]
    else:
        continue

print(f'O valor da soma dos numeros pares é {conta}')
