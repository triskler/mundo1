data = float(input("Digite a primeira nota: "))
data2 = float(input("Digite a segunda nota: "))

media = (data + data2) / 2


if(media >= 7):
    print(f'Sua media foi {media}, parabéns, está APROVADO!')
elif (media < 7 and media > 5):
    print(f'Sua media foi {media}, está deverá prestar RECUPERAÇÃO!')
elif(media < 5 ):
    print(f'Sua média foi {media}, o aluno foi REPROVADO!')
else:
    print(f'Valores não aceitos, tente novamente')