#faca um programa que calcule o IPVA de um carro com base no valor do mesmo. O IPVA é 4% do valor do carro

print("Qual valor do IPVA do seu carro?")
#pedindo ao usuario para fornecer o modelo do carro
modelo_carro = input("Qual modelo do seu carro?")
#pedindo o ano do veiculo
ano_carro = int(input("Qual ano fabricação do seu carro?"))

#pedindo valor do carro
valor_do_carro = float(input("Qual valor do seu carro? digite apenas os numeros sem virgula $"))
imposto = valor_do_carro*0.04 

#retornando mensagem ao usuario sobre valor do imposto e modelo do carro fornecido
print(f"Veiculo: {modelo_carro}/ Ano de fabricação {ano_carro}")

print(f"O valor do imposto do seu carro é de: ${imposto}")