import random, math
#codigo de geração de inimigos do rpg do aventureiro

#alguns exemplos de nome dos inimigos!
prefixos = ["Ela", "Ara", "The", "Dro", "Fa", "Mor", "Bar", "Nor", "Gal", "Heru", "Oro", "Ing"]
sufixos = ["dor", "wyn", "las", "iel", "nor", "rok", "mir", "ion", "ar", "rodel", "anar", "izel"]
tipos = ["Goblin", "meio-orc", "Troll", "Esqueleto", "Zumbi", "Ogro"]

#função para gerar um nome aleatorio pro inimigo.
def gerar_nome():
    tipo = random.choice(tipos)
    prefixo = random.choice(prefixos)
    sufixo = random.choice(sufixos)
    return f"{tipo} {prefixo}{sufixo}"

#função para criar um inimigo aleatorio!
def random_enemy(x=1, y=20): # Valores padrão definidos

    # Garante que x e y estão dentro do intervalo de 1 a 20
    x = max(1, min(x, 20))
    y = max(1, min(y, 20))

    nd = random.randint(x, y)
    hp_enemy = 100 * nd
    atk = random.randint(1, 15) + math.ceil(nd / 2)
    defense = random.randint(1, 15) + math.ceil(nd / 2)
    crit_rate = random.randint(1, 15) + math.ceil(nd / 2)
    accuracy = random.randint(1, 12) + math.ceil(nd / 2)

    # Retorna um dicionário contendo as informações do inimigo
    enemy = {
        "Nome": gerar_nome(),
        "HP": hp_enemy,
        "ATK": atk,
        "DEF": defense,
        "Crit. rate": crit_rate,
        "Taxa de Acerto": accuracy,
        "N/D": nd
    }

    return enemy


# exemplo de chamada da função de criar inimigo com base em uma escolha de dificuldade
while True:
    try:
        #perguntando ao usuario se ele deseja configurar a dificuldade do inimgo, caso contrario irar gerar um aleatorio
        opcao = input("Deseja definir a dificuldade do inimigo? (s/n): ").lower()
        
        if opcao == 's':
            x = int(input("Digite o valor mínimo para o nível de dificuldade (ND) (1-20): "))
            y = int(input("Digite o valor máximo para o nível de dificuldade (ND) (1-20): "))

            # Verifica se os valores são válidos
            if x < 1 or x > 20 or y < 1 or y > 20 or x > y:
                print("Os valores devem estar entre 1 e 20 e o mínimo deve ser menor ou igual ao máximo.")
                continue  # Retorna ao início do loop

            break  # Sai do loop se os valores forem válidos
        
        elif opcao == 'n':
            break  # Sai do loop se o usuário não deseja definir a dificuldade

        else:
            print("Opção inválida, por favor escolha 's' ou 'n'.")
    
    except ValueError:
        print("Por favor, insira números válidos.")

# Gera o inimigo com os valores válidos ou de forma padrao
enemy_gerado = random_enemy(x, y)  # nome da função para gerar inimigo
print("\nCaracterísticas do Inimigo:")
for chave, valor in enemy_gerado.items():
    print(f"{chave}: {valor}")