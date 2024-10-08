#faca um programa que diga se um numero é divisivel por 3 e que diga se um numero é divisivel por 5

print("Este numero é divisivel por 3 e por 5?")
numero=int(input("Digite um numero: "))
if(numero%3==0 and numero%5 == 0):
    print("Este é um numero divisivel por 3 e por 5!")
else:
    print("Esté não é um numero divisivel por 3 e/ou 5!")