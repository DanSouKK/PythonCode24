#faça um programa que receba "x" entradas que usuario solicitar
#no final faça a soma e imprima o resultado dos valores de cada entrada.

#Solicita usuario quantidade de entradas que ira usar
qtd = int(input("Quantos numeros para coletar: "))
#Variavei para acumular valores
contagem_pares = 0 
contagem_impares = 0
soma_pares = 0
soma_impares = 0

for i in range(qtd):
    #Solicita valores inteiros para o usuario
    numero = int(input("Digite um numero: "))
    #Verifica se valores sao par
    if numero % 2 == 0:
        #Acumula valoresem respectivas variaveis e faz a soma
        contagem_pares += 1
        soma_pares += numero
    else:
        contagem_impares += 1
        soma_impares += numero
#Soma de todos valores inputados pelo usuarios
soma_total = soma_impares + soma_pares
#Imprime resultados
print(f"\nQuantidade de numeros pares coletados: {contagem_pares}")
print(f"\nQuantidade de numeros impares coletados: {contagem_impares}")
print(f"\nSoma dos valores pares: {soma_pares}")
print(f"Soma dos valores impares: {soma_impares}")
print(f"\nSoma total dos numeros: {soma_total}")
