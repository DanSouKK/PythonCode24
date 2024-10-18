#faça um programa que simula o jogo da forca
import random  # Importa a biblioteca random para gerar escolhas aleatórias.

print("### Bem Vindo ao Jogo da Forca! ###")
# Lista de palavras possíveis para o jogo da forca.
# O jogo vai escolher aleatoriamente uma dessas palavras para o jogador adivinhar.
palavras = ['esporte', 'bicicleta', 'computador', 'montanha', 'oceano',
            'celular', 'viagem', 'teclado', 'telefone', 'filme',
            'futebol', 'livro', 'planeta', 'universo', 'carro',
            'escola', 'amigo', 'musica', 'cidade', 'astronauta']

# Escolhe uma palavra aleatória da lista para o jogador adivinhar.
palavra = random.choice(palavras)

# Inicializa duas variáveis importantes para o jogo:
# - letras_adivinhadas: guarda as letras que o jogador já tentou.
# - palavra_oculta: é uma lista com o mesmo número de caracteres da palavra, mas com '_' no lugar de cada letra,
#   representando a palavra que o jogador ainda não adivinhou. Cada vez que uma letra correta é adivinhada,
#   essa lista será atualizada com as letras reveladas.
letras_adivinhadas = []
palavra_oculta = ['_'] * len(palavra)

# Função que exibe o estado atual da palavra oculta, ou seja, a palavra que o jogador está tentando adivinhar.
# Exemplo: Se a palavra for "python" e o jogador já adivinhou as letras 'p' e 'y', a saída será "p y _ _ _ _".
def mostrar_palavra(palavra_oculta):
    print(" ".join(palavra_oculta))

# Função que define o número de tentativas baseado no tamanho da palavra e na dificuldade escolhida pelo jogador.
# O jogador pode escolher entre três níveis de dificuldade: fácil, médio e difícil, cada um com um número diferente de tentativas.
def definir_tentativas(palavra):
    # Calcula o tamanho da palavra (número de letras) para mostrar ao jogador.
    tamanho_palavra = len(palavra)
    
    # Inicia um loop que continuará até o jogador escolher uma dificuldade válida.
    while True:
        # Informa ao jogador quantas letras tem a palavra.
        print(f"\nA palavra tem {tamanho_palavra} letras.")
        
        # Solicita ao jogador que escolha o nível de dificuldade, lendo a entrada como uma string em letras minúsculas.
        dificuldade = int(input("\nEscolha o nível de dificuldade!\n1 - Fácil\n2 - Médio\n3 - Dificil\nEscolha: "))
        
        # Verifica se o jogador escolheu o nível "fácil".
        if dificuldade == 1:
            # Para o nível fácil, o número de tentativas é definido aleatoriamente entre 13 e 15.
            return random.randint(13, 15)
        
        # Verifica se o jogador escolheu o nível "médio".
        elif dificuldade == 2:
            # Para o nível médio, o número de tentativas é definido aleatoriamente entre 11 e 13.
            return random.randint(11, 13)
        
        # Verifica se o jogador escolheu o nível "difícil".
        elif dificuldade == 3:
            # Para o nível difícil, o número de tentativas é definido aleatoriamente entre 10 e 11.
            return random.randint(10, 11)
        
        # Se o jogador inserir um valor inválido, o loop continua até uma escolha válida ser feita.
        else:
            print("\nNível de dificuldade inválido. Tente novamente.")

# Define o número de tentativas com base no tamanho da palavra e na dificuldade escolhida pelo jogador.
tentativas = definir_tentativas(palavra)

# Exibe uma mensagem inicial para o jogador explicando quantas tentativas ele tem.
print("\nBem-vindo ao jogo da forca!")
print(f"\nVocê tem {tentativas} tentativas para adivinhar a palavra.")

# Loop principal do jogo, que continua até que:
# 1. O jogador adivinhe todas as letras (não há mais '_' em palavra_oculta).
# 2. O jogador fique sem tentativas (tentativas == 0).
while tentativas > 0 and '_' in palavra_oculta:
    # Mostra o estado atual da palavra oculta, com as letras já adivinhadas e os espaços restantes.
    mostrar_palavra(palavra_oculta)
    
    # Solicita ao jogador que insira uma letra para tentar adivinhar.
    letra = input("\nDigite uma letra: ").lower()

    # Verifica se o jogador já tentou essa letra anteriormente.
    if letra in letras_adivinhadas:
        # Se a letra já foi tentada, informa o jogador e pede para tentar outra.
        print(f"Você já tentou a letra '{letra}'. Tente outra.\n")        
        continue  # Volta para o início do loop sem penalizar uma tentativa.

    # Adiciona a letra na lista de letras já tentadas.
    letras_adivinhadas.append(letra)

    # Verifica se a letra escolhida está presente na palavra.
    if letra in palavra:
        # Se a letra está na palavra, percorre cada posição da palavra e revela as ocorrências da letra.
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_oculta[i] = letra
        print(f"\nBoa! A letra '{letra}' está na palavra.")
    else:
        # Se a letra não estiver na palavra, o jogador perde uma tentativa.
        tentativas -= 1
        print(f"\nA letra '{letra}' não está na palavra. Você perdeu uma tentativa.")
        print(f"Você tem {tentativas} tentativas restantes.")

# Verifica se o jogador ganhou (adivinhou todas as letras) ou perdeu (ficou sem tentativas).
if '_' not in palavra_oculta:
    # Se não há mais '_' em palavra_oculta, o jogador venceu.
    print("\nParabéns! Você adivinhou a palavra:")
else:
    # Se o jogador ficou sem tentativas, ele perdeu e a palavra correta é mostrada.
    print("\nVocê perdeu! A palavra era:", palavra)

# Mostra a palavra oculta no final do jogo, seja em caso de vitória ou derrota.
mostrar_palavra(palavra_oculta)
