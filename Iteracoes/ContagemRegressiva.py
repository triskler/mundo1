from time import sleep

data = int(input("Insira o numero para iniciar a contagem regressiva: "))

for i in range(data):
    print(data)
    sleep(1)
    data = data - 1
if data < 1:
    print("BOOM!")