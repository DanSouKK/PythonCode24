#faça um programa que pergunte se o usuario quer um combo ou um item individual. 
#onde hamburguer custa $10
#batata frita custa $10
#refrigerante custa $10
#o combo custa $22 // o cliente pode adicionar 2 itens
#caso ele adicione ofereça o 3rd item por $2, incentivando e vendendo indiretamento o combo

print("Bem vindo ao podrao do Senac! \n Escolha seus produtos!\n")
escolha=int(input("Escolha 1 - Hamburguer = $10 \nEscolha 2 - Batata Frita = $10 \nEscolha 3 - Refrigerante = $10 \nEscolha 4 - Combo Hamburguer+Batata+Refri = $22\n"))

item1 = "Hamburguer"
item2 = "Batata frita"
item3 = "Refrigerante"
item4 = "Combo"

if(escolha==1):
    print(f"Você escolheu {item1}")
    adicional = int(input("Gostaria de escolher mais algum item?\n2 - Batata frita e 3 - Refrigerante\n"))
    if(adicional==2):
        print(f"Você escolheu {item1} e {item2}")
        oferecendocombo= input("Gostaria de adicionar o refrigerante por mais $2? ").lower()
        if(oferecendocombo=="sim"):
            print(f"Seu pedido é {item1} e {item2} e {item3} totalizando em $22.")
        else:
            print(f"Seu pedido é {item1} e {item2} totalizando $20.")
    elif(adicional==3):
        print(f"Você escolheu {item1} e {item3}\n")
        oferecendocombo= input("Gostaria de adicionar batata por mais $2? ").lower()
        if(oferecendocombo=="sim"):
            print(f"Seu pedido é {item1} e {item2} e {item3} totalizando em $22.")
        else:
            print(f"Seu pedido é {item1} e {item3} totalizando $20.")

