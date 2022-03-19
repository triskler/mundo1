from time import sleep

data = int(input("Digite o numero para ver sua tabuada: "))

print("=-" * 10)
print(f'Tabuada do {data}')
print("=-" * 10)

for i in range(0, 11):
    conta = data * i
    sleep(1)
    print(f'{data} x {i} = {conta}')

