print("Bem-vindo ao sistema de reciclagem!")

# Variáveis acumuladoras para contar os materiais reciclados
papel = 0
plastico = 0
metal = 0
vidro = 0
organico = 0
nao_organico = 0

# Loop para continuar reciclando
continuar = "sim" or "s"
ultimo_material = ""
penul_material = ""
while continuar.lower() in [ "sim" or "s"]:
    # Solicita o material que o usuário deseja reciclar
    
    material = input("\nQual material você deseja reciclar? (papel, plastico, vidro, metal, organico, nao organico): ").lower()
    while material == ultimo_material == penul_material:
        print(f"Você ja reciclou este {material} 2x seguidas, recicle outro material!")
        material = input("\nQual material você deseja reciclar? (papel, plastico, vidro, metal, organico, nao organico): ").lower()
    # Verifica o material e contabiliza na lixeira correta
    if material == "papel":
        print("Descarte o papel na lixeira AZUL.\n")
        papel += 1
        if material == ultimo_material:           
          print("Pontos duplos!")
          papel +=1                                  
    elif material == "plastico":
        print("Descarte o plástico na lixeira VERMELHA.\n")
        plastico += 1
        if material == ultimo_material:           
          print("Pontos duplos!")
          plastico +=1  
    elif material == "vidro":
        print("Descarte o plástico na lixeira VERDE.\n")
        vidro += 1
        if material == ultimo_material:           
          print("Pontos duplos!")
          vidro +=1  
    elif material == "metal":
        print("Descarte o metal na lixeira AMARELA.\n")
        metal += 1
        if material == ultimo_material:           
          print("Pontos duplos!")
          metal +=1  
    elif material == "organico":
        print("Descarte o material orgânico na lixeira MARROM.\n")
        organico += 1
        if material == ultimo_material:           
          print("Pontos duplos!")
          organico +=1  
    elif material == "nao organico":
        print("Descarte o material não orgânico na lixeira CINZA.\n")
        nao_organico += 1
        if material == ultimo_material:           
          print("Pontos duplos!")
          nao_organico +=1  
    # caso usuario digite material nao identificado no programa.  
    else:
        print("Erro: material não reconhecido. Tente novamente.\n")
    penul_material = ultimo_material
    ultimo_material = material
    
    # Pergunta se o usuário deseja continuar
    continuar = input("Você deseja continuar reciclando? (sim/nao): ")
    # validacao de string correta para continuar ou nao o codigo.
    while continuar not in ["sim", "nao"]:
      print("\nERRO: Resposta inválida. Por favor, responda com 'sim' ou 'nao'.")
      continuar = input("\nVocê deseja continuar reciclando? (sim/nao): ").lower()

# Exibe o resumo dos materiais reciclados
print("\nResumo dos materiais reciclados:")
print(f"Papel: {papel}")
print(f"Plástico: {plastico}")
print(f"Metal: {metal}")
print(f"Vidro: {vidro}")
print(f"Orgânico: {organico}")
print(f"Não orgânico: {nao_organico}")
print("\n Obrigado por reciclar seus materiais.")