data = float(input("Digite o primeiro segmento: "))
data2 = float(input("Digite o segundo segmento: "))
data3 = float(input("Digite o terceiro segmento: "))

lista = [data, data2, data3]
menor = min(lista)
lista.remove(min(lista))
maior = max(lista)
lista.remove(max(lista))
medio = lista[0]

if (menor + medio <= maior):
    print("Estes segmentos NÃO formam um triângulo.")
elif (menor == medio == maior):
    print(f'Estes segmentos formam um triângulo EQUILATERO.')
elif (menor != medio != maior):
    print(f'Estes segmentos formam um triângulo ESCALENO')
else:
    print(f'Estes segmentos formam um triangulo ISOSCELES')

