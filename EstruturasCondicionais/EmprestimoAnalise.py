data = float(input("Digite o valor do imóvel: "))
data2 = float(input("Digite os rendimentos mensais: "))
data3 = int(input("Digite o tempo de pagamento em anos: "))

JUROS = 5.1/100

valor_imovel = (JUROS * data) + data

prest_imovel = valor_imovel / (data3 * 12)


