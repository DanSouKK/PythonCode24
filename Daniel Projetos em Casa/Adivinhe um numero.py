# Defina o número secreto
numero_secreto = 42
tentativas = 10

print("Bem-vindo ao jogo de adivinhação!")
print("Você tem 10 tentativas para adivinhar o número entre 1 e 100.")

while tentativas > 0:
    palpite = int(input("Digite seu palpite: "))
    
    if palpite < numero_secreto-10:
        print("\nSeu palpite é muito baixo!")
    elif palpite < numero_secreto-5:
        print("\nVocê está proximo!")
    elif palpite > numero_secreto+10:
        print("\nSeu palpite é muito alto!")
    elif palpite > numero_secreto+5:
        print("\nVocê está proximo!")
    else:
        print("Parabéns! Você adivinhou o número!")
        break  # Sai do loop se o usuário adivinhou corretamente
    
    tentativas -= 1  # Reduz o número de tentativas restantes
    print(f"\nVocê ainda tem {tentativas} tentativas.")

if tentativas == 0:
    print(f"\nSuas tentativas acabaram! O número era {numero_secreto}.")
