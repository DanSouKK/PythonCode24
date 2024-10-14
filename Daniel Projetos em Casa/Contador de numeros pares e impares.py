# Inicializa contadores
contagem_pares = 0
contagem_impares = 0
soma_pares = 0
soma_impares = 0

print("Digite um número (ou um número negativo para encerrar): ")

while True:
    numero = int(input("Digite aqui: "))
    
    if numero < 0:
        break  # Encerra o loop se o número for negativo    
    
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        contagem_pares += 1 
        #fazer calculo dos valores inseridos
        soma_pares += numero   
        #verifica se a contagem de pares é multiplo de 5
        if contagem_pares % 5 == 0:
            print("Vi que você gosta dos numeros pares!")
    else:
        contagem_impares += 1
        soma_impares += numero        
        if contagem_impares % 5 == 0:
            print("Vi que você gosta dos numeros impares!")

# Exibe os resultados
print(f"Números pares: {contagem_pares}")
print(f"Soma dos seus numeros pares digitado: {soma_pares}")
print(f"Números ímpares: {contagem_impares}")
print(f"Soma dos seus numeros impares digitado: {soma_impares}")