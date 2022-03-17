data = input("Digite um numero: ")
if(len(data) == 4):
  print(f'Este numero tem: ')
  print(f'{data[-1]} unidades')
  print(f'{data[-2]} dezenas')
  print(f'{data[-3]} centenas')
  print(f'{data[-4]} milhares')
elif(len(data) == 3):
  print(f'Este numero tem: ')
  print(f'{data[-1]} unidades')
  print(f'{data[-2]} dezenas')
  print(f'{data[-3]} centenas')
elif(len(data) == 2):
  print(f'Este numero tem: ')
  print(f'{data[-1]} unidades')
  print(f'{data[-2]} dezenas')
else:
  print(f'Este numero tem: ')
  print(f'{data[-1]} unidades')
