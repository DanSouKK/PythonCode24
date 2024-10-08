#faça um programa que pergunte se o usuario quer um combo ou um item individual. 
#onde hamburguer custa $10
#batata frita custa $10
#refrigerante custa $10
#o combo custa $22 // o cliente pode adicionar 2 itens
#caso ele adicione ofereça o 3rd item por $2, incentivando e vendendo indiretamento o combo
print("Bem vindo ao podrao do Senac! \n Escolha seus produtos!\n")
escolha=int(input("Escolha 1 - Hamburguer = $10 \nEscolha 2 - Batata Frita = $10 \nEscolha 3 - Refrigerante = $10 \nEscolha 4 - Combo Hamburguer+Batata+Refri = $22\nDigite aqui: "))

item1 = "Hamburguer"
item2 = "Batata frita"
item3 = "Refrigerante"
item4 = "Combo"
#caso usuario escolha opção 1
if(escolha==1):
    print(f"\nVocê escolheu 1 {item1}.")
    adicional = int(input("Gostaria de escolher mais algum item?\n1 - Batata frita\n2 - Refrigerante\n0 - Seguir para carrinho.\nDigite aqui: "))
    #caso usuario queira acidional              
    if(adicional==1): #escolhendo adicional da opcao 2
        print(f"Você escolheu 1 {item1} e 1 {item2}")
        #oferencendo combo para usuario
        oferecendocombo= input("\nGostaria de adicionar o refrigerante por mais $2? ").lower()
        if(oferecendocombo=="sim"):# resultado do combo caso usuario escolha sim na oferta
            print(f"Seu pedido é 1 {item1}, 1 {item2} e 1 {item3} totalizando em $22.")
            print("\n####   fim   ####")
        else:
            print(f"Seu pedido é 1 {item1} e 1 {item2} totalizando $20.")
            print("\n####   fim   ####")
    #opcao numero 3 no adicional
    elif(adicional==2): 
        print(f"Você escolheu 1 {item1} e 1 {item3}\n")
        oferecendocombo= input("\nGostaria de adicionar batata por mais $2? ").lower()
        if(oferecendocombo=="sim"):#oferta do combo para usuario
            print(f"Seu pedido é 1 {item1}, 1 {item2} e 1 {item3} totalizando em $22.")
            print("\n####   fim   ####")
        else:
            print(f"Seu pedido é 1 {item1} e 1 {item3} totalizando $20.")
            print("\n####   fim   ####")
    #caso ele nao queira um adicional
    elif(adicional == 0):
         print(f"Seu pedido é 1 {item1} totalizando $10.")
         print("\n####   fim   ####")
#caso o usuario inicie com a escolha numero 2
if(escolha==2):
    print(f"\nVocê escolheu 1 {item2}.")
    #ofertando um adicional ao cliente
    adicional = int(input("Gostaria de escolher mais algum item?\n1 - Hamburguer\n2 - Refrigerante\n0 - Seguir para carrinho.\nDigite aqui: "))              
    if(adicional==1):
        print(f"Você escolheu 1 {item2} e 1 {item1}")
        #ofertando combo ao usuario
        oferecendocombo= input("\nGostaria de adicionar o refrigerante por mais $2? ").lower()
        if(oferecendocombo=="sim"):
            print(f"Seu pedido é 1 {item2}, 1 {item1} e 1 {item3} totalizando em $22.")
            print("\n####   fim   ####")
        else:
            print(f"Seu pedido é 1 {item2} e 1 {item1} totalizando $20.")
            print("\n####   fim   ####")
    elif(adicional==2):# caso ele escolha oferta de adicional numero 2
        print(f"Você escolheu 1 {item2} e 1 {item3}\n")
        oferecendocombo= input("\nGostaria de adicionar hamburguer por mais $2? ").lower()
        if(oferecendocombo=="sim"):
            print(f"Seu pedido é 1 {item2}, 1 {item3} e 1 {item1} totalizando em $22.")
            print("\n####   fim   ####")
        else:
            print(f"Seu pedido é 1 {item2} e 1 {item3} totalizando $20.")
            print("\n####   fim   ####")
    #caso ele nao queira nenhum adicional
    elif(adicional == 0):
         print(f"Seu pedido é 1 {item2} totalizando $10.")
         print("\n####   fim   ####")
if(escolha==3):
    print(f"\nVocê escolheu 1 {item3}.")
    #ofertando um adicional do hambuguer ou batata
    adicional = int(input("Gostaria de escolher mais algum item?\n1 - Hamburguer\n2 - Batata Frita\n0 - Seguir para carrinho.\nDigite aqui: "))              
    if(adicional==1):
        print(f"Você escolheu 1 {item3} e 1 {item1}")
        #ofertando combo para o usuario/cliente
        oferecendocombo= input("\nGostaria de adicionar a batata frita por mais $2? ").lower()
        if(oferecendocombo=="sim"):
            print(f"Seu pedido é 1 {item3}, 1 {item1} e 1 {item2} totalizando em $22.")
        else:#caso ele recuse o combo
            print(f"Seu pedido é 1 {item3} e 1 {item1} totalizando $20.")
            print("\n####   fim   ####")
    elif(adicional==2):# caso ele escolha oferta de adicional numero 2
        print(f"Você escolheu 1 {item3} e 1 {item3}\n")
        oferecendocombo= input("\nGostaria de adicionar hamburguer por mais $2? ").lower()
        #ofertando o combo ao usuario/cliente
        if(oferecendocombo=="sim"):
            print(f"Seu pedido é 1 {item3}, 1 {item2} e 1 {item1} totalizando em $22.")
        else:#senao fechara apenas com refri e batata
            print(f"Seu pedido é 1 {item3} e 1 {item2} totalizando $20.")
            print("\n####   fim   ####")
    #caso ele nao queira nenhum adicional
    elif(adicional == 0):
         print(f"Seu pedido é 1 {item3} totalizando $10.")
         print("\n####   fim   ####")
if(escolha==4):  
    print(f"Você escolheu 1 {item4}, Hamburguer + Batata + Refrigerante.\n")
    print("Seu total a pagar é $22. Bom apetite, volte sempre\n")
    print("\n####   fim   ####")