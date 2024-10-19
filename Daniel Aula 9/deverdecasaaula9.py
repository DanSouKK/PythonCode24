import random

print("Bem-vindo ao jogo de adivinhação!")
print("Você tem que o(s) número(s) entre 1 e 100.")

# Gerando números aleatórios
numero_secreto1 = random.randint(1, 100)

#Configurando modo de jogo!
modo = input("\nVocê quer adivinhar 1 ou 2 números? (Digite 1 ou 2): ")

if modo == "2":
    numero_secreto2 = random.randint(1, 100)
    print("\nVocê escolheu adivinhar 2 números!")
else:
    print("\nVocê escolheu adivinhar 1 número!")

#Identificando qual nivel de dificuldade usuario ira jogar!
tentativas = int(input("\nEm quantas tentativas que adivinhar? (min: 1 e max: 10): "))
if tentativas < 1:
    tentativas = 1
    print(f"Merlin está entre nós! Usará apenas {tentativas} tentativas!Boa sorte!")
elif tentativas <=5:
    print(f"Uhm, vejo que gosta de desafios! Você terá {tentativas} tentativas.")
elif tentativas >5 and tentativas <=7:
    print(f"Entendi, você é um jogador experiente! Você terá {tentativas} tentativas.")
elif tentativas >7 and tentativas <=10:
    print(f"Muito bem, um jogo fácil! Você terá {tentativas} tentativas.")
else:
    tentativas = 10
    print(f"Vamos com calma, você terá um jogo facil com {tentativas} tentativas!")
    

acertou1 = False
acertou2 = False if modo == "2" else True  # Se escolheu 1 número, acertou2 já é verdadeiro.

while tentativas > 0:
    # Verifica se ainda precisa pedir o palpite para o primeiro número
    if not acertou1:
        palpite = int(input("\nDigite seu palpite para o primeiro número: "))
        
        if palpite < numero_secreto1 - 10:
            print("Seu palpite para o primeiro número é muito baixo!")
        elif palpite < numero_secreto1 - 5:
            print("Você está próximo do primeiro número!")
        elif palpite < numero_secreto1 - 20:
            print("Seu palpite está muito longe do primeiro número!")
        elif palpite > numero_secreto1 + 10:
            print("Seu palpite para o primeiro número é muito alto!")
        elif palpite > numero_secreto1 + 5:
            print("Você está próximo do primeiro número!")
        elif palpite > numero_secreto1 + 20:
            print("Seu palpite está muito longe do primeiro número!")
        else:
            print("\nParabéns! Você adivinhou o primeiro número!\n")
            acertou1 = True

    # Verifica se ainda precisa pedir o palpite para o segundo número
    if modo == "2" and not acertou2:
        palpite2 = int(input("\nDigite seu palpite para o segundo número: "))
        
        if palpite2 < numero_secreto2 - 10:
            print("Seu palpite para o segundo número é muito baixo!")
        elif palpite2 < numero_secreto2 - 5:
            print("Você está próximo do segundo número!")
        elif palpite2 < numero_secreto2 - 20:
            print("Seu palpite está muito longe do segundo número!")
        elif palpite2 > numero_secreto2 + 10:
            print("Seu palpite para o segundo número é muito alto!")
        elif palpite2 > numero_secreto2 + 5:
            print("Você está próximo do segundo número!")
        elif palpite2 > numero_secreto2 + 20:
            print("Seu palpite está muito longe do segundo número!")
        else:
            print("\nParabéns! Você adivinhou o segundo número!")
            acertou2 = True

    # Se ambos os números forem adivinhados, o jogo termina
    if acertou1 and acertou2:
        print("\nVocê adivinhou todos os números!")
        print(f"Os numeros eram: \nPrimeiro: {numero_secreto1}\nSegundo: {numero_secreto2}")
        break

    tentativas -= 1
    print(f"\nVocê ainda tem {tentativas} tentativas.")

# Caso as tentativas se esgotem
if tentativas == 0:
    if not acertou1:
        print(f"\nSuas tentativas acabaram! O primeiro número era {numero_secreto1}.")
    if modo == "2" and not acertou2:
        print(f"O segundo número era {numero_secreto2}.")
