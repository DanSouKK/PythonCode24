#faca um programa que gera 4 numeros aleatorios e depois os ordena de forma crescente.
import random

num1 = random.randint(20, 50)
num2 = random.randint(20, 50)
num3 = random.randint(20, 50)
num4 = random.randint(20, 50)

print(f"\nOs numeros gerados foram {num1}, {num2}, {num3}, {num4} ")
if num1 > num2:

    num1, num2 = num2, num1

if num1 > num3:

    num1, num3 = num3, num1

if num1 > num4:

    num1, num4 = num4, num1

if num2 > num3:

    num2, num3 = num3, num2

if num2 > num4:

    num2, num4 = num4, num2

if num3 > num4:

    num3, num4 = num4, num3

print(f"\nOrdem crescente dos numeros são: {num1}, {num2}, {num3}, {num4}")
print(f"\nOrdem decrescente dos numeros são: {num4}, {num3}, {num2}, {num1}")
    

