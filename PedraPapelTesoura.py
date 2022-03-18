from time import sleep
from random import randint

print("Suas opções são:")
print("[0] para PEDRA;")
print("[1] para PAPEL;")
print("[2] para TESOURA;")

data = int(input("Qual será sua jogada? "))
lista = ["PEDRA", "PAPEL", "TESOURA"]
comp = randint(0, 2)
jogadaPC = lista[comp]
jogadaPlayer = lista[data]




print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("=-" * 15)

if data == 0:
    if comp == 0:
        print(f'EMPATE! Você escolheu {jogadaPlayer}\n computador escolheu {jogadaPC}')
    elif comp == 1:
        print(f'PERDEU! Você escolheu {jogadaPlayer}\n computador escolheu {jogadaPC}')
    elif comp == 2:
        print(f'VENCEU! Você escolheu {jogadaPlayer}\n computador escolheu {jogadaPC}')
    else:
        print(f'ERRO! OPÇÃO INVALIDA!')
elif data == 1:
    if comp == 0:
        print(f'VENCEU! Você escolheu {jogadaPlayer}\n computador escolheu {jogadaPC}')
    elif comp == 1:
        print(f'EMPATE! Você escolheu {jogadaPlayer}\n computador escolheu {jogadaPC}')
    elif comp == 2:
        print(f'PERDEU! Você escolheu {jogadaPlayer}\n computador escolheu {jogadaPC}')
elif data == 2:
    if comp == 0:
        print(f'PERDEU! Você escolheu {jogadaPlayer}\n computador escolheu {jogadaPC}')
    elif comp == 1:
        print(f'GANHOU! Você escolheu {jogadaPlayer}\n computador escolheu {jogadaPC}')
    elif comp == 2:
        print(f'EMPATE! Você escolheu {jogadaPlayer}\n computador escolheu {jogadaPC}')
    else:
        print("ERRO!")
else:
    print("ERRO!")

print("=-" * 15)


