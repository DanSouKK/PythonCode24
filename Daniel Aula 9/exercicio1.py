# Criar um sistema de perguntas e respostas

print("Verdadeiro ou Falso Kahoot!")
pontos = 0

while True:
    contador = int(input("Quantas perguntas quer que apresente? min: 2, max: 3: "))
    
    # Validação do número de perguntas
    if contador < 2 or contador > 3:
        print("Por favor, insira um número entre 2 e 3.")
        continue

    print("Responda V - Verdadeiro ou F - Falso!")
    pontos = 0  # Reinicia a pontuação a cada rodada

    for i in range(contador):
        resposta1 = input("\nPython é uma linguagem de alto nível de semântica dinâmica? (V/F) ").lower()
        if resposta1 == "v":
            print("Você acertou. Python é uma linguagem dinâmica de alto nível!")
            pontos += 1
        else:
            print("Resposta incorreta. Python é uma linguagem de alto nível e bem dinâmica.")

        resposta2 = input("\nPython é derivado de outra linguagem? (V/F) ").lower()
        if resposta2 == "f":
            print("Você acertou! Python foi criado do zero.")
            pontos += 1
        else:
            print("Resposta incorreta.")

        resposta3 = input("\nA sintaxe de acumulador pode ser representada por += ou -=? (V/F) ").lower()
        if resposta3 == "v":
            print("Você acertou! A sintaxe está correta.")
            pontos += 1
        else:
            print("Você errou. Em Python, a sintaxe de acumulação pode ter + ou - antes do =.")

    # Sistema de vitória ou derrota
    if pontos >= 2:
        print("Parabéns! Você acertou a maioria.")
        print(f"Você acertou {pontos} perguntas!")
    else:
        print("Infelizmente, você não acertou a maioria das perguntas.")
        print(f"Você acertou {pontos} perguntas!")

    # Pergunta para jogar novamente
    retornar = input("Você deseja jogar novamente? (sim/não) ").lower()
    if retornar != "sim":
        print("Bom jogo!")
        break