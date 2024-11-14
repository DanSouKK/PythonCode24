# Você é um pirata, e durante suas navegações você encontrou um mapa do tesouro
# E seguindo as dicas do mapa você chegou ao tesouro, e apos cavar e desenterra-lo
# Percebe que esta trancado com um cofre muito robusto e possui um sistema de codificação de 3 digitos
# Apos testar algumas combinações você consegue achar uma logica para encontrar os digitos corretos para abrir
# Quando você escolhe os 3 digitos, e encontra algum digito correto ele dá um beep.
# Quando um digito esta correto e na posicao correta, ele da dois beep.
# Quando você digita um numer errado ele não acusa nada.

# Tente descobrir qual numero abre o cofre? Sorte marujo!

import random  # Importa o módulo random para gerar números aleatórios

# Função que verifica a senha e retorna quantos dígitos estão corretos
# fora de posição e quantos estão corretos na posição certa.
def verificar_senha(senha, tentativa):
    # Inicializa os contadores para dígitos fora de posição e na posição certa
    fora_de_posicao, posicao_certa = 0, 0

    # Listas para marcar quais dígitos da senha e da tentativa já foram verificados
    senha_usada = [False] * 3  
    tentativa_usada = [False] * 3

    # Verifica os dígitos que estão na posição correta
    for i in range(3):
        if tentativa[i] == senha[i]:
            posicao_certa += 1  # Incrementa se o dígito está correto e na posição certa
            senha_usada[i] = True  # Marca o dígito da senha como verificado
            tentativa_usada[i] = True  # Marca o dígito da tentativa como verificado

    # Verifica os dígitos corretos, mas que estão fora de posição
    for i in range(3):
        if not tentativa_usada[i]:  # Ignora os dígitos já verificados na posição certa
            for j in range(3):
                if not senha_usada[j] and tentativa[i] == senha[j]:
                    fora_de_posicao += 1  # Incrementa se o dígito correto está fora de posição
                    senha_usada[j] = True  # Marca o dígito da senha como verificado
                    break  # Não verifica mais dígitos para esse índice

    # Retorna o número de dígitos certos fora de posição e os corretos na posição certa
    return fora_de_posicao, posicao_certa

# Função principal do jogo
def jogar():
    # Gera uma senha secreta aleatória de 3 dígitos
    senha = str(random.randint(100, 999))

    # Exibe as instruções para o jogador
    print("Bem-vindo ao jogo! Tente adivinhar a senha do cofre.")
    print("A senha tem 3 dígitos. Cada dica é composta por:")
    print("- O número de dígitos certos mas fora de posição.")
    print("- O número de dígitos certos e na posição correta.")
    
    # Loop principal do jogo, que continua até o jogador acertar a senha
    while True:
        # Pede para o jogador digitar uma tentativa de 3 dígitos
        tentativa = input("Digite sua tentativa de 3 dígitos: ")

        # Valida se a tentativa tem exatamente 3 dígitos e se é um número
        if len(tentativa) != 3 or not tentativa.isdigit():
            print("Por favor, digite um número de 3 dígitos.")
            continue  # Se a tentativa for inválida, solicita uma nova tentativa

        # Chama a função verificar_senha para comparar a tentativa com a senha
        fora_de_posicao, posicao_certa = verificar_senha(senha, tentativa)

        # Exibe a dica para o jogador
        print(f"Dica: ({fora_de_posicao} certos fora de posição, {posicao_certa} certos na posição correta)")

        # Verifica se a tentativa é a senha correta
        if tentativa == senha:
            print("Parabéns! Você descobriu a senha do cofre!")
            break  # Encerra o jogo se o jogador acertou a senha
        else:
            print("Tente novamente.")  # Informa ao jogador que a tentativa foi incorreta

# Inicia o jogo chamando a função jogar
jogar()





# Usamos str em vez de int neste caso para simplificar a comparação dígito a dígito, pois cada posição dos números na senha e na tentativa precisa ser analisada individualmente.

# Aqui está o motivo mais detalhado:

# Comparação de Dígitos: Se a senha e a tentativa são strings, podemos facilmente acessar cada dígito pelo índice (por exemplo, senha[i] e tentativa[i]). Isso permite verificar se um dígito específico está na posição correta ou apenas presente na senha, sem precisar separar manualmente os dígitos de um número inteiro.

# Facilidade de Indexação: Ao usar strings, o código se torna mais direto porque senha[i] e tentativa[i] representam dígitos isolados. Com inteiros, seria necessário dividir o número em centenas, dezenas e unidades para realizar a comparação, o que complica o código.

# Validação de Entrada: Quando a entrada do usuário é uma string, podemos verificar seu comprimento (len(tentativa) != 3) e se ela é numérica (tentativa.isdigit()) antes de convertê-la para um número. Assim, garantimos que a entrada é exatamente um número de três dígitos, evitando entradas incorretas.

# Em resumo, usar str facilita o acesso e a comparação de cada dígito individualmente, tornando o código mais simples e legível.