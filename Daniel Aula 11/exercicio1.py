#voce é um aventureiro carregando uma mochila que comporta 3 itens, atualmente ela tem 3 itens:
#uma espada, uma pocao, um escudo. Ao longo da aventura encontra um arco no chao e precisa decidir
#se o coloca na mochila ou nao. Caso coloque, precisara descartar algum item a sua escolha

#faça um programa simulando essa historia e decisao usando lista.
x= True
mochila = ["espada", "escudo", "pocao"]

items = ["arco longo", "arco curto", "espada longa","katana", "machado grande", "machado duplo", "cajado", "grimorio", "escudo", "ervas", "pocao", "pergaminho"]

armas = ["espada", "arco longo", "katana", "arco curto", "espada longa", "machado grande", "machado duplo", "cajado", "grimorio", "flechas"]
print("Você esta se aventurando por uma clareira.\n Em busca de um abrigo antes que escureça.\n     Enquanto você adentra a floresta.\n         Voce encontra uma carroça quebrada na estrada.")
print("E alguns itens pelo chão:")
print(items)
print("\nSeu inventario atual:",mochila)
validar = input("\nGostaria de adicionar o novo item a mochila?S/N ").lower()
if validar == "s":    
    print(f"\nSua mochila esta cheia com ",mochila)
    while x == True:
        remover = input("\nQual item gostaria de remover? ").lower()
        if remover in mochila:
            mochila.remove(remover)
            while True:
                adicionar = input("\nQual item gostaria de adicionar? ").lower()
                if adicionar in items:
                    mochila.append(adicionar)
                    print(f"\nInventário atualizado: {mochila}")
                    x = False
                    break                    
                else:
                    print("Item inválido. Tente novamente.")
        else:
            print("Item inválido, tente novamente.")
else:
    print("\nNada acontece!")

#enquanto voce segue o seu caminho na floresta, um bandido armado surge e exige sua pocao
#voce tem a opção de sacar sua espada e enfrentar o bandido ou entregar sua pocao ao bandido
#se tentar lutar contra o bandido sem ter uma espada no inventario voce perde a batalha e jogo acabada.
#se tiver com espada o jogo continua.
#se voce entregar a pocao, voce perde ela da mochila e segue o jogo.
#mas se voce disser que ira entregar a pocao sem te-la na mochila, o bandido ficara furioso e sera fim do jogo.
#caso escolha uma opçao invalida o bandido se a aproveita da sua hesitacao  e lhe ataca, resultando no fim do jogo.
    

print("\nSeguindo sem caminho floresta adentro.\n\nSurge em meio às árvores um bandido.\n\nEle lhe para exigindo sua poção.\n")
acao = int(input("Qual será sua ação: \n1 - Sacar sua arma e lutar!\n2 - Entregar a poção.\n3 - Ficar parado e observar ao redor.\n"))

if acao == 1:
    if any(armas in mochila for armas in armas): #verifica se voce tem uma arma no inventario.
        print("\nVocê luta arduamente contra o bandido.\n\nApós alguns ataques, você derrota o bandido.")
    else:
        print("\nVocê tenta lutar, mas não tem uma arma.\n\nO bandido lhe derruba e acaba lhe acertando um golpe letal.\n\n|Game Over.|")

elif acao == 2:
    if "pocao" in mochila:  # Verifica se a poção está na mochila
        print("\nVocê se assusta com o bandido e, sem hesitar, entrega sua poção.\n\nEle foge rapidamente entre as árvores.")
        mochila.remove("pocao")  # Remove a poção da mochila
        print(f"Você perdeu sua poção e o bandido fugiu.\nVoce verifica sua mochila para ver se nao perdeu outras coisas: ",mochila)
    else:
        print("\nVocê tenta entregar a poção, mas não a tem na mochila.\n\nO bandido fica furioso e lhe dá um golpe fatal.\n\n|Game Over.|")

elif acao == 3:
    print("\nVocê fica atordoado com a situação.\n\nO bandido, vendo sua hesitação, lhe ataca.\nE acaba lhe matando.\n\n|Game Over.|")

else:
    print("\nAção inválida!\n\n O bandido aproveita sua hesitação e lhe ataca.\n\n|Game Over.|")
