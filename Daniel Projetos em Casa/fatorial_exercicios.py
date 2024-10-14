# Explicação sobre o que é fatorial
print("O fatorial de um número é o resultado da multiplicação desse número pelos seus antecessores até 1.")
print("Exemplo: Fatorial de 5 = 5 x 4 x 3 x 2 x 1\n")

# Solicita um número ao usuário
numero = int(input("Digite um número para calcular o fatorial: "))

# Inicializa o resultado
resultado = 1

# Solicita ao usuário se deseja ver o cálculo
resultado_fatorial = input("\nVocê quer incluir os cálculos do número fatoriado?\n\nSim - Quero o cálculo dos números fatoriados.\nNão - Quero apenas o resultado!\nDigite aqui: ").lower()

# Condicional para mostrar o cálculo ou não
if resultado_fatorial == "sim" or resultado_fatorial == "s":
    print(f"{numero}! = ", end="")

# Loop para calcular o fatorial e mostrar o processo se necessário
for i in range(numero, 1, -1):
    if resultado_fatorial == "sim" or resultado_fatorial == "s":
        print(f"{i} x ", end="")
    resultado *= i

# Finaliza com 1, sem necessidade de multiplicação por 1
if resultado_fatorial == "sim" or resultado_fatorial == "s":
    print("1 =", resultado)

# Verifica se o resultado é maior que 1 bilhão
if resultado >= 10**9:
    # Verifica o valor do resultado para mostrar uma aproximação em grandes números
    if resultado >= 10**21:
        print(f"\nResultado aproximado supera: {round(resultado / 10**21, 1)} sixtilhões")
        print("Uau é muito numero! Incrivel, deu trabalho.")
    elif resultado >= 10**18:
        print(f"\nResultado aproximado: {round(resultado / 10**18, 1)} quintilhões")
        print("Este numero é grande! Demorei um pouco mas deu certo!")
    elif resultado >= 10**15:
        print(f"\nResultado aproximado: {round(resultado / 10**15, 1)} quadrilhões")
        print("Impressionante este valor, não acha!!")
    elif resultado >= 10**12:
        print(f"\nResultado aproximado: {round(resultado / 10**12, 1)} trilhões")
        print("Alguns trilhões, bastante numero! Não foi muito complicado!")
    elif resultado >= 10**9:
        print(f"\nResultado aproximado: {round(resultado / 10**9, 1)} bilhões")
        print("Bastante digitos não é mesmo!!!")    
else:
    # Exibe o resultado final completo se for menor que 1 bilhão
    print(f"O fatorial de {numero} é {resultado}")