import math
data = float(input("Digite o comprimento do cateto oposto: "))
data2 = float(input("Digite o comprimento do cateto adjascente: "))

hipot = math.sqrt((data ** 2) + (data2 **2))

print(f'O comprimento da hipotenusa é {hipot}')