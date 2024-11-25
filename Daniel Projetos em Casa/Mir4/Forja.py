# Forja do Mir4 para criação de armas, armaduras e joias
# Dicionário de multiplicadores para criar itens de uma raridade a partir de outra
multiplicador_raridade = {
    "incomum": 10,
    "raro": 10,
    "epico": 10,
    "lendario": 10
}

# Custos em cobre, aço negro e pó brilhante para cada raridade
custos = {
    "incomum": {"cobre": 400, "aco_negro": 200},
    "raro": {"cobre": 2000, "aco_negro": 1000, "po_brilhante": 2},
    "epico": {"cobre": 20000, "aco_negro": 5000, "po_brilhante": 25},
    "lendario": {"cobre": 100000, "aco_negro": 25000, "po_brilhante": 125}
}

# Quantidades de matéria-prima para cada tipo de raridade de arma, armadura e joias
quantidade_arma = {
    "incomum": {"aço": 40, "esfera perversa": 4, "pedra de sombra lunar": 1, "escama de dragão": 1},
    "raro": {"aço": 75, "esfera perversa": 25, "pedra de sombra lunar": 25, "escama de dragão": 1},
    "epico": {"aço": 300, "esfera perversa": 100, "pedra de sombra lunar": 100, "escama de dragão": 1},
    "lendario": {"aço": 300, "esfera perversa": 100, "pedra de sombra lunar": 100, "escama de dragão": 1}
}

quantidade_armadura = {
    "incomum": {"aço": 20, "esfera perversa": 2, "pedra de sombra lunar": 1, "escama de dragão": 1},
    "raro": {"aço": 75, "esfera perversa": 25, "pedra de sombra lunar": 25, "escama de dragão": 1},
    "epico": {"aço": 300, "esfera perversa": 100, "pedra de sombra lunar": 100, "escama de dragão": 1},
    "lendario": {"aço": 300, "esfera perversa": 100, "pedra de sombra lunar": 100, "escama de dragão": 1}
}

quantidade_joias = {
    "incomum": {"aço": 40, "esfera perversa": 4, "pedra de sombra lunar": 1, "escama de dragão": 1},
    "raro": {"aço": 75, "esfera perversa": 25, "pedra de sombra lunar": 25, "escama de dragão": 1},
    "epico": {"aço": 300, "esfera perversa": 100, "pedra de sombra lunar": 100, "escama de dragão": 1},
    "lendario": {"aço": 300, "esfera perversa": 100, "pedra de sombra lunar": 100, "escama de dragão": 1}
}

materias_primas = ["aço", "esfera perversa", "pedra de sombra lunar", "escama de dragão"]

def calcular_materiais_por_raridade(tipo, raridade_desejada):
    # Seleciona o dicionário de quantidade conforme o tipo escolhido
    quantidade = {
        "arma": quantidade_arma,
        "armadura": quantidade_armadura,
        "joias": quantidade_joias
    }[tipo]

    total_materiais = {material: quantidade[raridade_desejada][material] for material in materias_primas}
    total_po_brilhante = 0
    total_cobre = 0
    total_aco_negro = 0

    raridades = ["comum", "incomum", "raro", "epico", "lendario"]

    # Exibe a receita na raridade escolhida, adaptada ao tipo do item
    receita = ", ".join([f"{quantidade[raridade_desejada][material]} {material} {raridade_desejada}" for material in materias_primas])
    print(f"\nReceita para {tipo.capitalize()} {raridade_desejada.capitalize()} ({receita})\n")

    for raridade in raridades[1:raridades.index(raridade_desejada)+1]:
        for material in materias_primas:
            if material != "escama de dragão":
                total_materiais[material] *= multiplicador_raridade[raridade] if raridade != raridade_desejada else 1
        
        if "po_brilhante" in custos[raridade]:
            total_po_brilhante += custos[raridade]["po_brilhante"] * (total_materiais[materias_primas[0]] // multiplicador_raridade[raridade])
        
        total_cobre += custos[raridade]["cobre"] * (total_materiais[materias_primas[0]] // multiplicador_raridade[raridade])
        total_aco_negro += custos[raridade]["aco_negro"] * (total_materiais[materias_primas[0]] // multiplicador_raridade[raridade])

    # Exibe o resultado com as matérias-primas conforme o tipo de item
    print(f"Para criar um(a) {tipo} {raridade_desejada}, você precisará das seguintes matérias-primas(incomum):")
    for material, quantidade in total_materiais.items():
        print(f"- {quantidade} unidades de {material}")
    print(f"- {total_po_brilhante} de pó brilhante")
    print(f"- {total_cobre} de cobre")
    print(f"- {total_aco_negro} de aço negro")

def escolher_segmento():
    print("Escolha o segmento que você deseja criar:")
    print("1. Arma")
    print("2. Armadura")
    print("3. Joias")
    opcao = input("Digite o número correspondente ao segmento desejado: ")

    segmentos = {
        "1": "arma",
        "2": "armadura",
        "3": "joias"
    }

    tipo_escolhido = segmentos.get(opcao)
    if tipo_escolhido:
        escolher_raridade(tipo_escolhido)
    else:
        print("Opção inválida. Tente novamente.")

def escolher_raridade(tipo):
    print(f"Escolha a raridade do(a) {tipo} que você deseja criar:")
    print("1. Comum")
    print("2. Incomum")
    print("3. Raro")
    print("4. Épico")
    print("5. Lendário")
    opcao = input("Digite o número correspondente à raridade desejada: ")

    raridades = {
        "1": "comum",
        "2": "incomum",
        "3": "raro",
        "4": "epico",
        "5": "lendario"
    }

    raridade_desejada = raridades.get(opcao)
    if raridade_desejada:
        calcular_materiais_por_raridade(tipo, raridade_desejada)
    else:
        print("Opção inválida. Tente novamente.")

# Executa a função para escolher o segmento
escolher_segmento()
