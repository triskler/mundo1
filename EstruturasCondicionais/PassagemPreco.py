data = int(input("Digite o numero de pessoas: "))
data2 = float(input("Digite a distancia percorrida: "))

if data2 <= 100:
  valor = 0.50
elif data2 > 100:
  valor = 0.40

passagem = data * (data2 * valor)

print(f' O valor da passagem para {data} pessoas, em uma distancia de {data2} Km,\n custará {passagem:.2f}')