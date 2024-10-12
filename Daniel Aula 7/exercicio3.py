#faça um programa que diga se o numero é primo ou nao
#peço o usuario um numero qualquer.
numero = int(input("Digite um numero: "))
#uso a variavel de apoio que definirar se o um numero é primo ou nao
primo = True
#faco um loop que vai do numero 2 ate o numero antecessor a ele
for i in range(2, numero):
    if (numero%i==0):
        #se um numero for divisivel por qualquer numero sem ser 1 ou ele mesmo, primo sera falso
        primo = False
    #se um numero for falso, é porque ele é divisivel por mais algum numero sem ser 1 e ele mesmo
if (primo == False):
    print("Este numero NÃO É PRIMO.")
else:
    print("Este é um numero PRIMO.")