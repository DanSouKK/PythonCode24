#faca um programa que gera 4 numeros aleatorios e depois os ordena de forma crescente.
import random

numeros = [random.randint(20, 50) for _ in range(4)]
print(f"Os numeros são: {numeros}")
numeros.sort(reverse = True)
print("\nA ordem decrescente dos numeros são: ", numeros)
numeros.sort(reverse = False)
print("\nA ordem crescente dos numeros são: ", numeros)
