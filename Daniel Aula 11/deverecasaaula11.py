#crie um programa que simule uma calculadora basica. o programa deve permitir que o usuario escolha entre as seguintes operações
#soma, subtracao, multiplicacao e divisao.
#apos a escolha o programa deve solicitar ao usuario dois numeros para realizar a operacao escolhida e exibir o resultado
#o programa deve utilizar funcoes pre definidas importadas.


#importando pastas
from exemplos_2.minhas_funcoes import somar, divisao, multiplicar, subtrair, cumprimentar

#chamando função
cumprimentar()
print("Calculadora Básica!")

while True:
    # Solicitando ao usuário o tipo de operação desejada
    operacao = int(input("\nEscolha o tipo de operação que deseja:\n1 - Somar.\n2 - Subtração.\n3 - Multiplicação.\n4 - Divisão.\n5 - Sair.\n"))

    if operacao == 5:
        print("Saindo da calculadora...")
        break  # Sai do loop e encerra o programa

    if operacao in (1, 2, 3, 4):
        num1 = float(input("\nEscolha o primeiro número: "))
        num2 = float(input("\nEscolha o segundo número: "))

        if operacao == 1:
            print("Operação de Soma.")
            resultado = somar(num1, num2)
            print(f"\nA soma de {num1} e {num2} = {resultado}.")
        elif operacao == 2:
            print("Operação de Subtração.")
            resultado = subtrair(num1, num2)
            print(f"\nA subtração de {num1} por {num2} = {resultado}.")
        elif operacao == 3:
            print("Operação de Multiplicação.")
            resultado = multiplicar(num1, num2)
            print(f"\nA multiplicação de {num1} por {num2} = {resultado}.")
        elif operacao == 4:
            print("Operação de Divisão.")
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
            else:
                resultado = divisao(num1, num2)
                print(f"\nA divisão de {num1} por {num2} = {resultado}.")
    else:
        print("Operação inválida. Escolha uma opção válida.")



