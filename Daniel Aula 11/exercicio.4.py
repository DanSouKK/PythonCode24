#faca um programa que tenha uma função chamada converter.
#essa funcao deve receber uma temperatura em celcius e retornar fahreinreit.

from exemplos.funcoes import celcius

temperatura = float(input("Digite a temperatura em celcius: "))
resultado = celcius(temperatura)
print(f"A conversão de {temperatura}°C em F°: {resultado}°F")