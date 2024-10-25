from funcoes.funcoes_rpg import criar_personagem_aleatorio, random_enemy

#testando chamadas de funções 
if __name__ == "__main__":
    # Gera um personagem aleatório
    personagem_gerado = criar_personagem_aleatorio()
    print("\nCaracterísticas do Personagem:")
    for chave, valor in personagem_gerado.items():
        print(f"{chave}: {valor}")

    # Gera um inimigo aleatório
    enemy = random_enemy()
    print(f"\nNome do inimigo: {enemy['Nome']}\nHP: {enemy['HP']}\nATK: {enemy['ATK']}\nDEF: {enemy['DEF']}\nCrit_rate: {enemy['Crit_rate']}\nTaxa de Acerto: {enemy['Taxa de Acerto']}")

## fim ### deu errado, nao flui como gostaria!!