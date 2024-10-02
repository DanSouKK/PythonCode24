print("Olá, você está na lojinha do Senac")

# Armazenando o valor da variável
idade = int(input("Qual a sua idade? "))

# Valores dos produtos
calca = 120.25
jaqueta = 150.10

# Calculando o desconto
desconto = idade * 2
total_sem_desconto = calca + jaqueta
total_com_desconto = total_sem_desconto - desconto

print("Qual item você vai querer comprar?")
# Apresentando o valor dos produtos
print(f"Calça azul? Custa R$ {calca:.2f}")
print(f"Jaqueta verde? Custa R$ {jaqueta:.2f}")

# Apresentando o valor do desconto recebido
print(f"Você receberá um desconto de R$ {desconto:.2f} em ambos os itens.")

# Apresentando o valor total da compra
print(f"Total da sua compra deu: R$ {total_sem_desconto:.2f}")
print(f"Seu desconto é: R$ {desconto:.2f}")
print(f"Sua compra no total deu: R$ {total_com_desconto:.2f}")