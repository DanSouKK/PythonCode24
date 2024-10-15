#Gerar numeros de 1 a 10, com "pulo" de 2 em 2
soma = 0
x = int(input("Digite primeira entrada: "))
y = int(input("Digite segunda entrada: "))
z = int(input("Digite quantidade de casas que ele ira pular entre as entradas: "))
print(f"Iremos pular {z} casas entre os valores {x} e {y}.")
for i in range(x, y, z):
    soma+=i
    print(f"Os numeros são: {i}")
print(f"A soma dos valores apresentados: {soma}")