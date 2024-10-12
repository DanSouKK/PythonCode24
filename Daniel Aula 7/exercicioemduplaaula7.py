#no exercicio abaixo é uma simulação paralela e reciclagem de residuos do qual tornamos em um game do tipo jogo da memoria e pontuação
#neste exercicio beneficiamos o usuario que tiver mais acertos consecutivos porem o limitamos a "x" acertos consecutivos.

# Bem-vindo ao sistema de reciclagem!
print("Bem-vindo ao sistema de reciclagem!")

# Variáveis para armazenar a quantidade de cada tipo de material reciclado
papel = 0
plastico = 0
metal = 0
vidro = 0
organico = 0
nao_organico = 0

# Define que o usuário deseja continuar reciclando ao iniciar o loop
continuar = "sim"  # Aqui o operador "or" não é necessário. Pode ser só "sim" para inicialização correta.

# Variáveis para armazenar o último e o penúltimo material reciclado, para evitar repetições
ultimo_material = ""
penul_material = ""

# Loop principal que continua pedindo ao usuário para reciclar até que ele decida parar
while continuar.lower() == "sim":
    # Solicita que o usuário informe qual material deseja reciclar
    material = input("\nQual material você deseja reciclar? (papel, plastico, vidro, metal, organico, nao organico): ").lower()

    # Verifica se o mesmo material foi inserido três vezes consecutivas, impedindo essa repetição
    while material == ultimo_material == penul_material:
        print(f"Você já reciclou {material} 2x seguidas, por favor, recicle outro material!")
        material = input("\nQual material você deseja reciclar? (papel, plastico, vidro, metal, organico, nao organico): ").lower()

    # Verifica o tipo de material inserido e o associa à lixeira correta, contabilizando o número de itens reciclados
    if material == "papel":
        print("Descarte o papel na lixeira AZUL.\n")
        papel += 1
        # Pontuação extra se o usuário reciclar o mesmo material duas vezes consecutivas
        if material == ultimo_material:           
            print("Pontos duplos!")
            papel += 1  # Contabiliza ponto extra por acertos consecutivos
    elif material == "plastico":
        print("Descarte o plástico na lixeira VERMELHA.\n")
        plastico += 1
        if material == ultimo_material:           
            print("Pontos duplos!")
            plastico += 1
    elif material == "vidro":
        print("Descarte o vidro na lixeira VERDE.\n")
        vidro += 1
        if material == ultimo_material:           
            print("Pontos duplos!")
            vidro += 1
    elif material == "metal":
        print("Descarte o metal na lixeira AMARELA.\n")
        metal += 1
        if material == ultimo_material:           
            print("Pontos duplos!")
            metal += 1
    elif material == "organico":
        print("Descarte o material orgânico na lixeira MARROM.\n")
        organico += 1
        if material == ultimo_material:           
            print("Pontos duplos!")
            organico += 1
    elif material == "nao organico":
        print("Descarte o material não orgânico na lixeira CINZA.\n")
        nao_organico += 1
        if material == ultimo_material:           
            print("Pontos duplos!")
            nao_organico += 1
    else:
        # Caso o usuário insira um material não reconhecido
        print("Erro: material não reconhecido. Tente novamente.\n")

    # Atualiza as variáveis para armazenar o último e penúltimo material reciclado
    penul_material = ultimo_material
    ultimo_material = material

    # Pergunta se o usuário deseja continuar reciclando
    continuar = input("Você deseja continuar reciclando? (sim/nao): ").lower()

    # Validação da resposta, exigindo que o usuário digite "sim" ou "nao" corretamente
    while continuar not in ["sim", "nao"]:
        print("\nERRO: Resposta inválida. Por favor, responda com 'sim' ou 'nao'.")
        continuar = input("\nVocê deseja continuar reciclando? (sim/nao): ").lower()

# Exibe um resumo de todos os materiais reciclados ao final do processo
print("\nResumo dos materiais reciclados:")
print(f"Papel: {papel}")
print(f"Plástico: {plastico}")
print(f"Metal: {metal}")
print(f"Vidro: {vidro}")
print(f"Orgânico: {organico}")
print(f"Não orgânico: {nao_organico}")
print("\nObrigado por reciclar seus materiais.")