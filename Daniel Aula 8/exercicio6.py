#faça um programa que diga quais dos 20 primeiros multiplos de 5 sao pares
#e some os impares e mostre a soma no final

soma = 0
for i in range(5, 101, 5):
    if i %2 == 0:
        print(f"Multiplos de 5 sao: {i}")
    else:
        soma+=i
print(f"Soma dos impares: {soma}")    

       
        