#crie um programa que simule o jogo sudoku

import random

# função para gerar um tabuleiro
def tabuleiro_sudoku():
    base = 3
    lado = base * base #gerar uma tabuleiro 9x9

    #função auxiliar para embaralhar 
    def embaralhar(s):
        return random.sample(s, len(s))
    
    #criar uam lista de posições base pra organizar os numeros
    def grupo(base):
        return[g*base + i for g in embaralhar(range(base)) for i in embaralhar(range(base))]

    # oraganizar linhas e colunas do tabuleiro
    def organizador():
        rBase = range(base)
        linhas = [g*base + r for g in embaralhar(rBase) for r in embaralhar(rBase)]
        colunas = [g*base + c for g in embaralhar(rBase) for c in embaralhar(rBase)]
        nums = embaralhar(range(1, base*base + 1))
        #preencher o tabuleiro com base nas linhas e colunas e embaralhar os numeros.
        tabuleiro = [[nums[(base * (r % base) + r //base + c)% lado]for c in colunas]for r in linhas]
        return tabuleiro
    
    # função pra remover alguns numeros para preencher
    def esconder(tabuleiro):
        tabuleiro_jogo = [[tabuleiro[r][c]if random.random()< 0.5 else 0 for c in range(lado)]for r in range(lado)]
        return tabuleiro_jogo
    #criar tabuleiro completo e organizado
    tabuleiro = organizador() 
    #ocultar alguns numeros do tabuleiro
    tabuleiro_jogo = esconder(tabuleiro)
    return tabuleiro_jogo

#função para exibir o tabuleiro inteiro
def exibir_tabuleiro(tabuleiro):
    print("\nTabuleiro: ")
    for linha in tabuleiro:
        print(" ".join(str(num)if num != 0 else "." for num in linha))

# Verificar se o movimento é valido
def move_true(tabuleiro, linha, coluna, nums):
    #verificando se ja tem um numero na linha
    if nums in tabuleiro[linha]:
        return False
    #verificando na coluna
    if nums in [tabuleiro[r][coluna]for r in range(9)]:
        return False
    #verificando em cada quadrado se ja tem o numero
    inicio_linha, inicio_coluna = 3 * (linha // 3), 3 * (coluna // 3)
    for r in range(inicio_linha, inicio_linha + 3):
        for c in range(inicio_coluna, inicio_coluna + 3):
            if tabuleiro[r][c] == nums:
                return False
    return True

#função para ver se o jogador completou o tabuleiro
def win_check(tabuleiro):
    for linha in tabuleiro:
        if 0 in linha:
            return False
    return True

#função pro codigo principal do jogo
def jogar():
    tabuleiro = tabuleiro_sudoku()
    exibir_tabuleiro(tabuleiro)
    
    while not win_check(tabuleiro):
        try:
            linha = int(input("\nDigite a linha(0-8): "))
            coluna = int(input("\nDigite a coluna(0-8): "))            
            nums = int(input("\nDigite o numero(1-9): "))
            #verifica se o movimento que usuario escolheu esta okay.
            if move_true(tabuleiro, linha, coluna, nums):
                tabuleiro[linha][coluna] = nums
                exibir_tabuleiro(tabuleiro)
            else:
                print("Movimento invalido! Tenta outra vez!")
        except ValueError:
            print("Entrada invalida! Digite os numeros corretos!")
    print("\nParabéns! Voce completou o tabuleiro Sudoku.")

# Executando o jogo!!!
if __name__ == "__main__":
    jogar()

    
    
