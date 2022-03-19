data = int(input("Digite o numero final: "))
soma = 0

for i in range(0, data, 3):
    if i % 2 != 0:
        soma += i
        print(f'Numero {i} - A soma dos multiplos de tres está em: {soma}')
    else:
        continue
