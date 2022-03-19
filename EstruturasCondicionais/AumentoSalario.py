data = float(input("Digite o salário do funcionário: "))
reajuste = 0
if data <= 1250:
    reajuste = data * (15/100)

elif data >= 1250:
    reajuste = data * (10/100)

data = data + reajuste

print(f'O novo salario será de {data} e a aplicação foi de {reajuste}')
