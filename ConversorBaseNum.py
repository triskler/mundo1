data = int(input("Digite um numero inteiro: "))

hexConv = hex(data)
octConv = oct(data)
binConv = bin(data)

print(f'O numero {data} é {hexConv[2:]} em hexadecimal\n {octConv[2:]} em Octal \n {binConv[2:]} em binário.')
