from time import sleep

data = int(input("Digite um numero: "))
count = 0
print("==>  <==" * 10)
for i in range(1, data + 1):
    conta = data % i
    if conta != 0:
        sleep(1)
        print(f'O numero {i} não divisivel por {data}')
    else:
        sleep(1)
        print(f'\033[1;36mO numero {i} é divisivel por {data}\033[m')
        count += 1
sleep(1)
print("==> <==" * 10)
if count <= 2:
    sleep(1)
    print(f'\033[1;32m{data} É PRIMO!')
else:
    sleep(1)
    print(f'\033[1;31m{data} NÃO É PRIMO!')

