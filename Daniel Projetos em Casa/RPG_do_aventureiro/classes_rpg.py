#Bárbaro: Guerreiro feroz que utiliza força bruta e raiva em combate. Consegue resistir a altos níveis de dano e causa grande destruição em lutas corpo a corpo.
#Bardo: Aventureiro versátil que usa música e conhecimento para inspirar aliados, enganar inimigos e lançar magias. É uma classe de suporte que oferece auxílio estratégico em diversas situações.
#Clérigo: Devoto de uma divindade, com habilidades de cura e proteção. Especialista em magias divinas, pode atuar tanto como curador quanto como guerreiro sagrado.
#Druida: Guardião da natureza que lança magias relacionadas ao ambiente e animais. Pode se transformar em diversas criaturas e tem habilidades para controlar a vida selvagem.
#Feiticeiro: Conjurador de magias com poder inato. Ao contrário dos magos, não precisa estudar para aprender magias e é muito poderoso em batalhas mágicas.
#Guerreiro: Classe focada no combate corpo a corpo e com armas. Possui uma variedade de habilidades marciais e é adaptável para qualquer estilo de luta.
#Ladino: Perito em furtividade, disfarces e ataques furtivos. Habilidoso em desarmar armadilhas, abrir fechaduras e manipular situações sociais.
#Mago: Estudioso das artes arcanas, capaz de conjurar magias poderosas e complexas. Tem um grande repertório de magias, mas é fisicamente vulnerável.
#Monge: Lutador que usa a disciplina do corpo e mente para lutar sem armas. Possui habilidades que aumentam sua velocidade, resistência e capacidade de evitar ataques.
#Paladino: Guerreiro sagrado com habilidades de cura e magia divina, focado em proteger e defender os inocentes. É um combatente leal e resistente ao mal.
#Patrulheiro (Ranger): Especialista em combate à distância e sobrevivência na natureza. Possui um companheiro animal e habilidades para caçar e rastrear criaturas.
#Feiticeiro Guerreiro (Hexblade): Um combatente que mescla habilidades de guerra com magia sombria, lançando maldições e ataques poderosos enquanto luta.
#Ninja: Classe furtiva com habilidades para ataques rápidos, evasão e combate dissimulado. Focada em ataques surpresa e habilidades de espionagem.
#Assassin: Perito em morte silenciosa, recebe bônus de ataque furtivo e habilidades para eliminar alvos sem ser detectado. Perfeito para ladinos que desejam se especializar em ataques letais e furtivos.
#Samurai: Guerreiro com forte código de honra e habilidades de combate com espada. É resistente e possui técnicas especiais de luta.

import random

# Classes de RPG com habilidades e equipamentos permitidos
classes = {
    "Guerreiro": {
        "Habilidades": {"Ataque": "+3", "Defesa": "+2", "Habilidade": "Ataque Extra"},
        "Equipamentos": {
            "Armaduras": ["Qualquer armadura"],
            "Armas": ["Qualquer arma"],
            "Escudos": ["Qualquer escudo"]
        }
    },
    "Mago": {
        "Habilidades": {"Magia": "+4", "Defesa Mágica": "+2", "Habilidade": "Magia Arcana"},
        "Equipamentos": {
            "Armaduras": ["Nenhuma"],
            "Armas": ["Adaga", "Cajado", "Grimório"],
            "Escudos": ["Nenhum"]
        }
    },
    "Paladino": {
        "Habilidades": {"Ataque": "+2", "Defesa": "+3", "Habilidade": "Imposição de Mãos"},
        "Equipamentos": {
            "Armaduras": ["Qualquer armadura"],
            "Armas": ["Qualquer arma"],
            "Escudos": ["Qualquer escudo"]
        }
    },
    "Ladino": {
        "Habilidades": {"Crit Rate": "+3", "Taxa de Acerto": "+2", "Habilidade": "Ataque Furtivo"},
        "Equipamentos": {
            "Armaduras": ["Armadura leve"],
            "Armas": ["Qualquer arma"],
            "Escudos": ["Qualquer escudo"]
        }
    },
    "Bárbaro": {
        "Habilidades": {"Ataque": "+4", "Pontos de Vida": "+20", "Habilidade": "Fúria"},
        "Equipamentos": {
            "Armaduras": ["Armadura leve"],
            "Armas": ["Qualquer arma"],
            "Escudos": ["Qualquer escudo"]
        }
    },
    "Druida": {
        "Habilidades": {"Magia": "+3", "Defesa": "+1", "Habilidade": "Forma Selvagem"},
        "Equipamentos": {
            "Armaduras": ["Armadura leve"],
            "Armas": ["Clava", "Adaga", "Bastão"],
            "Escudos": ["Nenhum"]
        }
    },
    "Bardo": {
        "Habilidades": {"Magia": "+2", "Crit Rate": "+1", "Habilidade": "Inspiração"},
        "Equipamentos": {
            "Armaduras": ["Armadura leve"],
            "Armas": ["Espada curta", "Lira", "Adaga"],
            "Escudos": ["Nenhum"]
        }
    },
    "Monge": {
        "Habilidades": {"Defesa": "+3", "Crit Rate": "+2", "Habilidade": "Mãos Desarmadas"},
        "Equipamentos": {
            "Armaduras": ["Nenhuma"],
            "Armas": ["Punhos", "Bastão"],
            "Escudos": ["Nenhum"]
        }
    },
    "Ranger": {
        "Habilidades": {"Ataque": "+2", "Taxa de Acerto": "+3", "Habilidade": "Combate com Duas Armas"},
        "Equipamentos": {
            "Armaduras": ["Armadura leve"],
            "Armas": ["Arco longo", "Espada curta"],
            "Escudos": ["Nenhum"]
        }
    },
    "Feiticeiro": {
        "Habilidades": {"Magia": "+4", "Crit Rate": "+1", "Habilidade": "Explosão Arcana"},
        "Equipamentos": {
            "Armaduras": ["Nenhuma"],
            "Armas": ["Adaga", "Cajado"],
            "Escudos": ["Nenhum"]
        }
    },
    "Clérigo": {
        "Habilidades": {"Magia": "+3", "Defesa Mágica": "+2", "Habilidade": "Cura"},
        "Equipamentos": {
            "Armaduras": ["Armadura pesada", "Armadura média"],
            "Armas": ["Clava", "Espada longa"],
            "Escudos": ["Qualquer escudo"]
        }
    },
    "Necromante": {
        "Habilidades": {"Magia": "+3", "Defesa Mágica": "+2", "Habilidade": "Invocação de Mortos-Vivos"},
        "Equipamentos": {
            "Armaduras": ["Nenhuma"],
            "Armas": ["Cajado", "Adaga"],
            "Escudos": ["Nenhum"]
        }
    },   
    
    "Assassino": {
        "Habilidades": {"Crit Rate": "+3", "Defesa": "+1", "Habilidade": "Mergulho nas Sombras"},
        "Equipamentos": {
            "Armaduras": ["Armadura leve"],
            "Armas": ["Adaga", "Espada curta"],
            "Escudos": ["Nenhum"]
        }
    }
}

def escolher_classe():
    print("Escolha sua classe:")
    for i, classe in enumerate(classes.keys(), 1):
        print(f"{i}. {classe}")

    # Solicita ao jogador que escolha uma classe válida
    while True:
        try:
            escolha = int(input("\nDigite o número da classe escolhida: "))
            if 1 <= escolha <= len(classes):
                classe_escolhida = list(classes.keys())[escolha - 1]
                habilidades = classes[classe_escolhida]["Habilidades"]
                equipamentos = classes[classe_escolhida]["Equipamentos"]
                
                print(f"\nClasse escolhida: {classe_escolhida}")
                print("Habilidades:")
                for atributo, bonus in habilidades.items():
                    print(f"  {atributo}: {bonus}")

                print("\nEquipamentos permitidos:")
                for tipo, lista in equipamentos.items():
                    print(f"  {tipo}: {', '.join(lista)}")
                
                break
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

# Exemplo de chamada
escolher_classe()
