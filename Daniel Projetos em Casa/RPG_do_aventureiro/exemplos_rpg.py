#exemplos de chamadas para o programa do rpg do aventureiro

# Loop para obter a dificuldade do inimigo
# caso necessario precisar no programa para eventuais tipos de inimigos.
while True:
    try:
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

#chamando a função e exibindo resultado do aventureiro
personagem_gerado = criar_personagem_aleatorio()#nome da função para gerar aventureiro
print("\nCaracterísticas do Personagem:")
for chave, valor in personagem_gerado.items():
    print(f"{chave}: {valor}")
