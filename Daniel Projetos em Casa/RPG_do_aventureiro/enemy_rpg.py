import random

# Exemplos de nome dos inimigos
prefixos = ["Ela", "Ara", "The", "Dro", "Fa", "Mor", "Bar", "Nor", "Gal", "Heru", "Oro", "Ing"]
sufixos = ["dor", "wyn", "las", "iel", "nor", "rok", "mir", "ion", "ar", "rodel", "anar", "izel"]
tipos = ["Goblin", "meio-orc", "Troll", "Esqueleto", "Zumbi", "Ogro"]

# Função para gerar um nome aleatório para o inimigo
def gerar_nome():
    tipo = random.choice(tipos)
    prefixo = random.choice(prefixos)
    sufixo = random.choice(sufixos)
    return f"{tipo} {prefixo}{sufixo}"

# Função para criar um inimigo aleatório
def random_enemy(x=1, y=20):
    #nivel de dificuldade = ND    
    nd = random.randint(x, y)  # Nível de dificuldade do inimigo
    
    # Definindo os limites dos atributos de acordo com o ND
    if nd == 1:
        pontos_de_vida_base = random.randint(300, 500)
        ataque_base = random.randint(10, 25)
        defesa_base = random.randint(10, 20)
        magia_base = random.randint(10, 25)
        defesa_magica_base = random.randint(10, 20)
        taxa_acerto_base = random.randint(10, 25)
        crit_rate_base = random.randint(10, 20)
    elif nd == 2:
        pontos_de_vida_base = random.randint(400, 600)
        ataque_base = random.randint(15, 30)
        defesa_base = random.randint(15, 25)
        magia_base = random.randint(15, 30)
        defesa_magica_base = random.randint(15, 25)
        taxa_acerto_base = random.randint(15, 30)
        crit_rate_base = random.randint(15, 25)
    elif nd == 3:
        pontos_de_vida_base = random.randint(500, 700)
        ataque_base = random.randint(20, 35)
        defesa_base = random.randint(20, 30)
        magia_base = random.randint(20, 35)
        defesa_magica_base = random.randint(20, 30)
        taxa_acerto_base = random.randint(20, 35)
        crit_rate_base = random.randint(20, 30)
    elif nd == 4:
        pontos_de_vida_base = random.randint(600, 800)
        ataque_base = random.randint(25, 40)
        defesa_base = random.randint(25, 35)
        magia_base = random.randint(25, 40)
        defesa_magica_base = random.randint(25, 35)
        taxa_acerto_base = random.randint(25, 40)
        crit_rate_base = random.randint(25, 35)
    elif nd == 5:
        pontos_de_vida_base = random.randint(700, 900)
        ataque_base = random.randint(30, 45)
        defesa_base = random.randint(30, 40)
        magia_base = random.randint(30, 45)
        defesa_magica_base = random.randint(30, 40)
        taxa_acerto_base = random.randint(25, 40)
        crit_rate_base = random.randint(25, 35)
    elif nd == 6:
        pontos_de_vida_base = random.randint(800, 1100)
        ataque_base = random.randint(45, 110)
        defesa_base = random.randint(45, 110)
        magia_base = random.randint(40, 110)
        defesa_magica_base = random.randint(45, 110)
        taxa_acerto_base = random.randint(40, 110)
        crit_rate_base = random.randint(30, 81)
    elif nd == 7:
        pontos_de_vida_base = random.randint(900, 1200)
        ataque_base = random.randint(50, 120)
        defesa_base = random.randint(50, 120)
        magia_base = random.randint(50, 120)
        defesa_magica_base = random.randint(50, 120)
        taxa_acerto_base = random.randint(50, 120)
        crit_rate_base = random.randint(36, 87)
    elif nd == 8:
        pontos_de_vida_base = random.randint(1000, 1300)
        ataque_base = random.randint(60, 130)
        defesa_base = random.randint(60, 130)
        magia_base = random.randint(60, 130)
        defesa_magica_base = random.randint(60, 130)
        taxa_acerto_base = random.randint(60, 130)
        crit_rate_base = random.randint(37-88)
    elif nd == 9:
        pontos_de_vida_base = random.randint(1200, 1400)
        ataque_base = random.randint(120, 140)
        defesa_base = random.randint(120, 140)
        magia_base = random.randint(120, 140)
        defesa_magica_base = random.randint(120, 140)
        taxa_acerto_base = random.randint(120, 140)
        crit_rate_base = random.randint(38-89)
    elif nd == 10:
        pontos_de_vida_base = random.randint(1300, 1500)
        ataque_base = random.randint(130, 150)
        defesa_base = random.randint(130, 150)
        magia_base = random.randint(130, 150)
        defesa_magica_base = random.randint(130, 150)
        taxa_acerto_base = random.randint(130, 150)
        crit_rate_base = random.randint(39-90)
    elif nd == 11:
        pontos_de_vida_base = random.randint(1450, 1800)
        ataque_base = random.randint(145, 180)
        defesa_base = random.randint(145, 180)
        magia_base = random.randint(145, 180)
        defesa_magica_base = random.randint(145, 180)
        taxa_acerto_base = random.randint(145, 180)
        crit_rate_base = random.randint(40-91)
    elif nd == 12:
        pontos_de_vida_base = random.randint(1700, 2100)
        ataque_base = random.randint(170, 210)
        defesa_base = random.randint(170, 210)
        magia_base = random.randint(170, 210)
        defesa_magica_base = random.randint(170, 210)
        taxa_acerto_base = random.randint(170, 210)
        crit_rate_base = random.randint(41-92)
    elif nd == 13:
        pontos_de_vida_base = random.randint(2000, 2400)
        ataque_base = random.randint(200, 240)
        defesa_base = random.randint(200, 240)
        magia_base = random.randint(200, 240)
        defesa_magica_base = random.randint(200, 240)
        taxa_acerto_base = random.randint(200, 240)
        crit_rate_base = random.randint(42-93)
    elif nd == 14:
        pontos_de_vida_base = random.randint(2350,2900)
        ataque_base = random.randint(235, 290)
        defesa_base = random.randint(235, 290)
        magia_base = random.randint(235, 290)
        defesa_magica_base = random.randint(235, 290)
        taxa_acerto_base = random.randint(235, 290)
        crit_rate_base = random.randint(43, 94)
    elif nd == 15:
        pontos_de_vida_base = random.randint(2800, 3300)
        ataque_base = random.randint(280, 330)
        defesa_base = random.randint(280, 330)
        magia_base = random.randint(280, 330)
        defesa_magica_base = random.randint(280, 330)
        taxa_acerto_base = random.randint(280, 330)
        crit_rate_base = random.randint(44, 95)
    elif nd == 16:
        pontos_de_vida_base = random.randint(3200, 3600)
        ataque_base = random.randint(320, 360)
        defesa_base = random.randint(320, 360)
        magia_base = random.randint(320, 360)
        defesa_magica_base = random.randint(320, 360)
        taxa_acerto_base = random.randint(320, 360)
        crit_rate_base = random.randint(45, 96)
    elif nd == 17:
        pontos_de_vida_base = random.randint(3500, 3900)
        ataque_base = random.randint(350, 390)
        defesa_base = random.randint(350, 390)
        magia_base = random.randint(350, 390)
        defesa_magica_base = random.randint(350, 390)
        taxa_acerto_base = random.randint(350, 390)
        crit_rate_base = random.randint(46, 97)
    elif nd == 18:
        pontos_de_vida_base = random.randint(3800, 4400)
        ataque_base = random.randint(380, 440)
        defesa_base = random.randint(380, 440)
        magia_base = random.randint(380, 440)
        defesa_magica_base = random.randint(380, 440)
        taxa_acerto_base = random.randint(380, 440)
        crit_rate_base = random.randint(47, 98)
    elif nd == 19:
        pontos_de_vida_base = random.randint(4300, 4800)
        ataque_base = random.randint(430, 480)
        defesa_base = random.randint(430, 480)
        magia_base = random.randint(430, 480)
        defesa_magica_base = random.randint(430, 480)
        taxa_acerto_base = random.randint(430, 480)
        crit_rate_base = random.randint(48, 99)    
    elif nd == 20:
        pontos_de_vida_base = random.randint(4800, 5200)
        ataque_base = random.randint(480, 520)
        defesa_base = random.randint(450, 600)
        magia_base = random.randint(480, 520)
        defesa_magica_base = random.randint(450, 600)
        taxa_acerto_base = random.randint(480, 520)
        crit_rate_base = random.randint(50, 100)
    
    # Função para calcular variação
    def aplicar_variacao(valor_base):
        variacao = random.uniform(0.88, 1.12)  # Variação de 8% a 12%
        return int(valor_base * variacao)

    # Aplica a variação a cada atributo
    pontos_de_vida = aplicar_variacao(pontos_de_vida_base)
    ataque = aplicar_variacao(ataque_base)
    defesa = aplicar_variacao(defesa_base)
    magia = aplicar_variacao(magia_base)
    defesa_magica = aplicar_variacao(defesa_magica_base)
    taxa_acerto = aplicar_variacao(taxa_acerto_base)
    crit_rate = aplicar_variacao(crit_rate_base)

    # Criação do inimigo com os atributos organizados
    inimigo = f"""
    ===========================
          Inimigo Gerado
    ===========================
    Nome: {gerar_nome()}
    Nível de Dificuldade: {nd}
    Pontos de Vida: {pontos_de_vida}
    Ataque: {ataque}
    Defesa: {defesa}
    Ataque Magia: {magia}
    Defesa Mágica: {defesa_magica}
    Taxa de Acerto: {taxa_acerto}
    Crítico: {crit_rate}
    ===========================
    """
    print(inimigo)

# Função para obter os parâmetros de dificuldade do usuário
def obter_dificuldade():
    while True:
        opcao = input("Deseja definir a dificuldade do inimigo? (s/n): ").lower()
        
        if opcao == 's':
            try:
                x = int(input("Digite o valor mínimo para o nível de dificuldade (ND) (1-20): "))
                y = int(input("Digite o valor máximo para o nível de dificuldade (ND) (1-20): "))
                # Verifica se os valores são válidos
                if 1 <= x <= 20 and 1 <= y <= 20 and x <= y:
                    return x, y
                else:
                    print("Os valores devem estar entre 1 e 20 e o mínimo deve ser menor ou igual ao máximo.")
            except ValueError:
                print("Por favor, insira um valor numérico.")
        elif opcao == 'n':
            return 1, 20  # Retorna valores padrão se não desejar definir a dificuldade
        else:
            print("Opção inválida, por favor escolha 's' ou 'n'.")

# Gera o inimigo com os valores válidos ou de forma padrão
x, y = obter_dificuldade()
random_enemy(x, y)
