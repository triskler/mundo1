data = input("Digite seu nome completo: ")
data = data.upper()
primeira = data.find('A')
ultima = data.rfind('A')
count = 0
for palavra in data:
  if(palavra == 'A'):
    count += 1
  else:
    continue;
print(f'A letra A aparece {count} vezes')
print(f'A primeira ocorrencia foi no espaço {primeira +1}')
print(f'A ultima ocorrencia foi na posição {ultima +1}')