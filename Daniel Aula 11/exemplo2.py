armas = ["espada", "arco longo", "katana", "arco curto", "espada longa", "machado grande", "machado duplo", "cajado", "grimorio"]
mochila = ["espada", "escudo", "pocao"]  # Exemplo de mochila

print("\nSeguindo sem caminho floresta adentro.\n\nSurge em meio às árvores um bandido.\n\nEle lhe para exigindo sua poção.\n")
acao = int(input("Qual será sua ação: \n1 - Sacar sua arma e lutar!\n2 - Entregar a poção.\n3 - Ficar parado e observar ao redor.\n"))

if acao == 1:
    if "espada" in mochila:  # Verifica se a espada está na mochila
        print("\nVocê luta arduamente contra o bandido.\nApós alguns ataques, você derruba o bandido.")
    else:
        print("\nVocê tenta lutar, mas não tem uma espada.\nO bandido lhe derruba e acaba lhe acertando um golpe letal.\n|Game Over.|")

elif acao == 2:
    if "pocao" in mochila:  # Verifica se a poção está na mochila
        print("\nVocê se assusta com o bandido e, sem hesitar, entrega sua poção.\nEle foge rapidamente entre as árvores.")
        mochila.remove("pocao")  # Remove a poção da mochila
    else:
        print("\nVocê tenta entregar a poção, mas não a tem na mochila.\nO bandido fica furioso e lhe dá um golpe fatal.\n|Game Over.|")

elif acao == 3:
    print("\nVocê fica atordoado com a situação.\nO bandido, vendo sua hesitação, lhe ataca.\nE acaba lhe matando.\n|Game Over.|")

else:
    print("\nAção inválida! O bandido aproveita sua hesitação e lhe ataca.\n|Game Over.|")