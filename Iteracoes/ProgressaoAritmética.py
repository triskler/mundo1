print("===" * 7)
print("Calculadora de Progressão Aritmetica")
print("===" * 7)

termoInicial = int(input("Digite o termo inicial: "))
razao = int(input("Digite a razão: "))
termos = int(input("Digite quantos termos deseja: "))

numeroTermos = termoInicial + (termos - 1) * razao
passo = termoInicial
print("===>" * 20)


for i in range(termoInicial, numeroTermos + 1, razao):
    print(f'{passo}', end=" => ")
    passo += razao

print("ACABOU!")
print("===>" * 20)
