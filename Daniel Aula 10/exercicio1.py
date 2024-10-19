#faca um  programa que gera 3 numeros aleatorios e voce tem 1 tentativa para descobrir qual é o maior.

import random   

num1 = random.uniform(1, 15)
num2 = random.uniform(1, 15)
num3 = random.uniform(1, 15)
print("Foram gerados 3 numero aleatorios entre 1 e 15!\nTente adivinhar qual deles é o maior!")
escolha = input("\nQual dos numeros você acha que é maior? 1, 2 ou 3 digite aqui: ")
if (escolha == 1 and num1 > num2 > num3 or escolha == 2 and num2 > num1 > num3 or escolha == 3 and num3 > num2 > num1):
    print(f"Voce acertou")
else:
    print("Você errou!")
print(f"Os numeros eram\nPrimeiro numero:{num1:.2f}\nSegundo numero: {num2:.2f}\nTerceiro numero: {num3:.2f}")

