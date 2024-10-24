#apos a aventura, o aventureiro resolveu treinar mais seu combate; faça uma simulação
#onde o aventureiro tem uma lista[100, 20], onde 100 é a vida dele
#20 é o poder de ataque dele e a cada 7 segundos de treino, ele aumenta seu ataque em 1 com limite
#maximo de 30 para seu poder de ataque.
import time, random

poder_combate_aventureiro = [1000, 20]  # Vida, Ataque
poder_combate_bandido = [600, 20] # Vida, Ataque

hp_player = poder_combate_aventureiro[0]
atk_player = poder_combate_aventureiro[1]
hp_enemy = poder_combate_bandido [0]
atk_enemy =poder_combate_bandido [1]


print("Após longa jornada, nosso aventureiro decide treinar seu poder de combate!!!")
time.sleep(1)
print("Ele encontrou um local de ataque e começou a fazer seus testes!!")
time.sleep(1)
print("Ele percebe que, conforme avança com treinamento, vai ficando mais forte!!!")
time.sleep(1)
print("Então decide treinar até chegar ao seu máximo!")

print("\nStatus Player\n// HP atual: ", hp_player, "\n // Ataque: ", atk_player)


while atk_player < 30:
    print("O poder de ataque atual é", atk_player)
    treino = input("Gostaria de treinar mais? S/N \n").lower()
    
    if treino == "s":
        atk_player += 1
        print("Após árduo treinamento!")
        time.sleep(1)  # Pausa após o treinamento
        print(" // HP atual: ", hp_player, "\n // Ataque: ", atk_player)
    elif treino == "n":
        print("Descansando...")
        time.sleep(1)  # Pausa ao descansar
        print(" // HP atual: ", hp_player, "\n // Ataque: ", atk_player)
        break
    elif atk_player >=30:
        print("Você esta esgostado!!")
        time.sleep(1)
        print("Descanse um pouco!!")
        break
    else:
        print("Opção inválida! Por favor, digite 'S' ou 'N'.")
        time.sleep(1)  # Pausa para a mensagem de erro

#A batalha segue as seguintes regras:

#O aventureiro e o assaltante atacam simultaneamente, causando dano um ao outro com o valor de "Ataque".
#A batalha continua até que a "Vida" de um dos personagens chegue a zero ou abaixo.
#Após cada rodada de ataque, o status de cada personagem (seus valores de "Vida" e "Ataque") deve ser exibido.
#Haverá um intervalo de 4 segundos entre as rodadas de ataque para simular a pausa entre os golpes.
#Ao final da batalha, o loop deve parar e os valores finais de "Vida" de ambos os personagens devem ser mostrados.

#Escreva o código para simular essa batalha e exiba o status de ambos os personagens a cada rodada de ataque        
#faça uma variavel sorte que simule um ataque critico, caso acerte um golpe critico aplica de 2x - 10x o poder de ataque do dano ao adversario

      

print("\nApos terminar seu treinamento, você vagueia pela floresta...")
time.sleep(1)
print("           Depois de algum tempo você encontra um bandido, que lhe surpreende...")
time.sleep(1)
print("                     Ele lhe exige que entregue seus pertences...")
time.sleep(1)

acao = int(input("\nQual ação ira escolher?\n1 - Lutar...\n2 - Entregar os pertences...\n3 - Fugir..."))
if acao == 1:
    print("\nA batalha começa entre o Aventureiro e o Bandido!")
    time.sleep(2)
    print("\nStatus Enemy\n// HP atual: ", hp_enemy, "\n // Ataque: ", atk_enemy)
    # Loop da batalha
    while hp_player > 0 and hp_enemy > 0:
        # Ataque
        crit_rate_player = random.randint(1, 10)
        crit_rate_enemy = random.randint(1, 10)        
        hp_player -= atk_enemy * crit_rate_enemy
        hp_enemy -= atk_player * crit_rate_player
        
        # Exibir status após cada rodada
        print("\n=== Status Atual ===")
        print(f"Aventureiro - Vida: {hp_player}, Ataque: {atk_player}")
        print(f"Bandido - Vida: {hp_enemy}, Ataque: {atk_enemy}")
        
        # Pausa entre os ataques
        time.sleep(4)

    # Final da batalha
    print("\n=== Fim da Batalha ===")
    if hp_player <= 0 and hp_enemy <= 0:
        print("Ambos os combatentes caem em batalha!")
    elif hp_player <= 0:
        print("O Aventureiro foi derrotado!")
    else:
        print("O Bandido foi derrotado!")

    # Exibir valores finais
    print(f"Vida final do Aventureiro: {hp_player}")
    print(f"Vida final do Bandido: {hp_enemy}")



    


