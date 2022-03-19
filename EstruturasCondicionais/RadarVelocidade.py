data = int(input("Insira a velocidade do veiculo: "))
limite = 90
if data > limite +10:
  print(f'MULTADO! Sua velocidade foi de {data} Km/h em uma via de {limite} km/h')
elif data <= limite +10:
  print(f'CUIDADO! sua velocidade é de {data} km/h numa via de {limite} km/h')
else:
  print(f'DIRIJA COM SEGURANÇA! Tenha uma boa viagem!')