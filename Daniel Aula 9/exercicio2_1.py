# Defina o número secreto
import random
numero_secreto = random.randint(1, 200)
tentativas = int(input("Quantas tentativas quer tentar adivinhar o numero: (min 1- max 10): "))
if tentativas >= 10:
    tentativas = 10
elif tentativas <=1:
    tentativas = 1
elif tentativas<=5:
    print(f"\nUhm um mestre da adivinhação!Boa sorte você tem {tentativas} chances!")
elif tentativas >5 and tentativas <=7:
    print(f"\nMuito bem, gosta de desafios! Você tem {tentativas} tentativas!")
else:
    print(f"\nJogo fácil, vamos começar com {tentativas} tentativas.")

tentativas_iniciais = tentativas
print("\nBem-vindo ao jogo de adivinhação!")
print(f"Você tem {tentativas} tentativas para adivinhar o número entre 1 e 200.")

while tentativas > 0:
    palpite = int(input("Digite seu palpite: "))
    
    if palpite < numero_secreto-10:
        print("\nSeu palpite é muito baixo!")
    elif palpite < numero_secreto-5:
        print("\nVocê está proximo!")
    elif palpite < numero_secreto-20:
        print("\nSeu palpite está muito longe!")
    elif palpite > numero_secreto+10:
        print("\nSeu palpite é muito alto!")
    elif palpite > numero_secreto+5:
        print("\nVocê está proximo!")
    elif palpite > numero_secreto+20:
        print("\nSeu palpite está muito longe!")
    else:
        tentativas_restantes = tentativas - 1
        # Apresentar uma mensagem especial, se o usuário usar poucos palpites para acertar
        if tentativas_restantes < tentativas_iniciais / 2:
            print(f"Uau! Você foi incrível, adivinhou em apenas {tentativas_iniciais - tentativas} tentativas.")
        else:
            print("Parabéns! Você adivinhou o número!")
        break  # Sai do loop se o usuário adivinhou corretamente
    
    tentativas -= 1  # Reduz o número de tentativas restantes
    print(f"\nVocê ainda tem {tentativas} tentativas.")

if tentativas == 0:
    print(f"\nSuas tentativas acabaram! O número era {numero_secreto}.")
