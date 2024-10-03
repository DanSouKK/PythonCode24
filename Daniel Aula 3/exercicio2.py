#Calcule o IMC do usuario com base na formula de Indice de Massa Corporal
#IMC = Peso dividido por altura ao quadrado. IMC = Peso(kg)/Altura(m²)

print("Qual seu IMC - Indice de Massa Corporal?")

#solicitando ao usuario os dados para calculo
peso = float(input("Qual seu peso em kg? "))
altura = float(input("Qual sua altura em metros? "))

#fazendo calculo do IMC
altura_quadrado = altura*altura

#calculo do IMC
IMC = peso/altura_quadrado

#retornando resultado ao usuario
print(f"Com base em seus valores indicados, seu peso {peso}kg")
print(f"Sua altura fornecida de :{altura}m.")

#limitando meu resultado IMC em X casas decimais
print(f"Seu IMC é de: {IMC:.2f}.")

print("--------------------------------")
#Com base do IMC como esta sua saude de acordo com a tabela?
print("IMC Menor que 16.9 = Muito abaixo do Peso.")
print("IMC entre 17.0 e 18.40 = Abaixo do Peso.")
print("IMC entre 18.5 e 24.90 = Peso Normal.")
print("IMC entre 25.0 e 29.90 = Acima do peso.")
print("IMC entre 30.0 e 34.90 = Obesidade Grau I.")
print("IMC entre 35.0 e 40.0 = Obesidade Grau II.")
print("IMC maior que 40.1 = Obsesidade Grau III.")