#faça um programa que diga se o numero é par ou impar
numero = int(input("Digite um numero: "))
#condição para testar se o numero divido por 2 tem resto 0 ou diferente //
if(numero % 2 == 0):
    print(f"Você digitou {numero}, este é um numero par.")
else:
    print(f"Você digitou {numero}, este é um numero impar.")