#faça um programa que simule o armario de uma escola e permita colocar o nome do aluno responsavel/pagante da gaveta
#o armario tem dimensao 5x5
#a escola adicionou um novo armario 3x3 perto das salas de aula e o chamou de armario VIP
#caso o aluno adquira uma gaveta no armario comum custara R$30,00 ao mes
#o vip custara R$ 50,00.
#adicione no sistema essa selecao e retorne para usuario o custo.


tamanho_armario = 5
tamanho_armariovip = 3

# Inicializa o armario
armario = [["X"] * tamanho_armario for _ in range(tamanho_armario)]
armariovip = [["X"] * tamanho_armariovip for _ in range(tamanho_armariovip)]

def mostrar_armario(armario):
    for linha in armario:
        print(" ".join(linha))
def mostrar_armario(armariovip):
    for linha in armariovip:
        print(" ".join(linha))

print("Armarios Comuns: ")
mostrar_armario(armario)
print("\nArmarios VIP")
mostrar_armario(armariovip)

while True:
    print("\nTemos duas opções de armarios: \nComum, no corredor central - R$ 30/mes.\nVIP, que fica proximo as salas de aula - R$50/mes.")
    escolha = int(input("\nQual armario quer utilizar?\n1 - Comum \n2 - VIP \n0 - Sair\n"))
    if escolha == 0:
        print("\nEncerrando...")
        break  # Sai do loop e encerra o programa
    nome = input("\nQual o seu nome? ")
    if escolha == 1:
        linha = int(input("\nEscolha uma linha (0 - 4):  "))
        coluna = int(input("\nEscolha uma coluna (0 - 4): "))
        if armario[linha][coluna] == "X":  # Verifica se a gaveta está livre
            armario[linha][coluna] = nome
            mostrar_armario(armario)
        else:
            print("\n!!! Gaveta já está sendo utilizada. Escolha outra.")         
        
    elif escolha == 2:
        linha = int(input("\nEscolha uma linha (0 - 2):  "))
        coluna = int(input("\nEscolha uma coluna (0 - 2): "))
        if armariovip[linha][coluna] == "X":  # Verifica se a gaveta está livre
            armariovip[linha][coluna] = nome
            mostrar_armario(armariovip)            
        else:
            print("\n!!! Gaveta já está sendo utilizada. Escolha outra.")        
    else:
        print("\nEscolha incorreta!")
        








