data = int(input("Digite oano aser analisado: "))

if data % 4 == 0 and data % 100 != 0 or data % 400 == 0:
  print(f'O ano {data} é BISSEXTO')
else:
  print(f'O ano {data} NÃO É BISSEXTO')