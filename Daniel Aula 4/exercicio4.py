#faça um programa que calcule o IMC do usuario e de classificação conforme tabela
#Menor que 18,5 	Magreza 	
#Entre 18,5 e 24,9 	Normal 	
#Entre 25,0 e 29,9 	Sobrepeso 	
#Entre 30,0 e 39,9 	Obesidade 	
#Maior que 40,0 	Obesidade Grave
print("Qual seu IMC - Indice de Massa Corporal? Responda abaixo as questões.")
#pedindo o usuario suas informações
peso=float(input("Qual seu peso? em KG: "))
altura=float(input("Qual sua altura? "))
#fazendo calculo da altura ao quadrado para fazer o calculo do imc. sabendo que imc= peso/ altura²
altura_quadrado = altura*altura

#calculo do imc para validar retornos abaixo.
IMC=peso/altura_quadrado
#retornos dos resultados
if(IMC<16):
    print(f"Seu IMC é {IMC:.2f} oque indica que você esta muito abaixo do peso normal. Grau de magreza III.")
elif(IMC>=16 and IMC<=16.99):
    print(f"Seu IMC é {IMC:.2f} oque indica que você esta abaixo do peso normal. Grau de magreza II.")
elif(IMC>=17 and IMC<=18.49):
    print(f"Seu IMC é {IMC:.2f} oque indica que você esta abaixo do peso normal. Grau de Magreza I.")
elif(IMC>=18.5 and IMC<=24.99):
    print(f"Seu IMC é {IMC:.2f} oque indica que seu peso está normal.")
elif(IMC>=25 and IMC<=29.99):
    print(f"Seu IMC é {IMC:.2f} oque indica que está acima do peso. Obesidade em Grau I.")
elif(IMC>=30 and IMC<=39.99):
    print(f"Seu IMC é {IMC:.2f} oque indica que está acima do peso. Obesidade em Grau II.")
elif(IMC>40):
    print(f"Seu IMC é {IMC:.2f} oque indica que está acima do peso. Obesidade em Grau III.")