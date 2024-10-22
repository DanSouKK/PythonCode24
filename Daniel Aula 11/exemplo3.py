#funcao: calcula o quadrado de um numero

def quadrado(numero):
    return numero ** 2
def raiz_quadrada(numero):
    return numero ** 0.5

numero = float(input("Digite um numero: "))
resultado = quadrado(numero) # recebe o retorno da funcao
print(f"O Quadrado de {numero} é {resultado} e sua raiz é {raiz_quadrada(numero)}")


