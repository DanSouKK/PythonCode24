import random
#gera um numero inteiro aleatorio entre 1 e 100
#numero_random = random.randint(1, 100)
#print(f"Numero inteiro aleatorio entre 1 e 100: {numero_random}")

#em funções passamos parametros(numeros, variaveis). Muitas vezes nao temos acesso a logica por tras.
#Elas servem para facilitar o desenvolvimento e evitar codigos desnecessarios ou "a reinvenção da roda"
#bibliotecas costumam ter varias funções.

#simula o lancamento de uma moeda
resultado = "Cara" if random.randint(0,1) == 0 else "Coroa"
print(f"O resultado do lancamento da moeda é: {resultado}")