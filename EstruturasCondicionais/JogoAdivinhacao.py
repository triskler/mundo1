import random
data = int(input("Digite um numero de 0 a 3: "))
comp = random.randint(0,3)
if(data == comp):
  print(f'Você acertou! Escolhi o numero {comp}.')
else:
  print(f'Você errou! O numero escolhido foi {comp} e não {data}')
