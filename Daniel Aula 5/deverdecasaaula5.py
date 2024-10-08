#faca um programa que peça ao usuario para inserir 5 numeros. o programa deve calcular a soma acumulada desses numeros e exibir o resultado final.
#usar variavel acumuladora para armazenar e soma dos numeros.

print("------------- Mini Calculadora!---------------\n")
#variavel acumuladora e um contador para dimensionar/limitar o codigo.
soma = 0
contador = 1
#pedindo o primeiro numero
numero = float(input(f"Digite o {contador}º numero: "))
soma += numero
contador +=1
#pedindo segundo numero
if contador<=5:
    numero = float(input(f"Digite o {contador}º numero: "))
    soma += numero
    contador +=1
else:
    pass
#pedindo terceiro numero
if contador<=5:
    numero = float(input(f"Digite o {contador}º numero: "))
    soma += numero
    contador +=1
else:
    pass
#pedindo o quarto numero
if contador<=5:
    numero = float(input(f"Digite o {contador}º numero: "))
    soma += numero
    contador +=1
else:
    pass
#pedindo o quinto numero
if contador<=5:
    numero = float(input(f"Digite o {contador}º numero: "))
    soma += numero
    contador +=1
else:
    pass
print(f"\nA soma dos 5 numeros é: {soma:.2f}.\n")
print("### fim ###")

