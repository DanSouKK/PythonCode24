#faça um programa que receba "x" entradas do usuario
#no final faça soma somente dos valores impares coletados e imprima resultado

#Solicita usuario quantidade de entradas que tera no programa
qtd = int(input("Quantos numeros para coletar: "))
#Variavel acumuladora
soma_impares = 0

for i in range(qtd):
    #Solicita valores de cada entrada ao usuario, com base na questão anterior
    numero = int(input("Digite um numero: "))
    #Verifica se valor é impar
    if numero % 2 != 0:
        soma_impares += numero
#Imprime e retorna o resultado 
print(f"Soma dos valores impares: {soma_impares}")
