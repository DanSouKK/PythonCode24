#faça um programa onde o pikachu comeca com uma lista de 4 poderes
#poderes = ["choque do trovao", "calda de ferro", "ataque rapido", "esquiva"]
#faça um programa que voce ao adicionar um novo poder, precisa remover outro. ou seja, o pikachu precisa ter sempre apenas 4 poderes

poderes = ["choque do trovao","calda de ferro","ctaque rapido","esquiva"]
print("Poderes do Pikachu:",poderes)
pokemons = ["Pikachu","Charmander","Bulbasaur"]
validar = input("Gostaria de adicionar um novo poder ao pikachu?S/N ").lower()
if validar == "s":
    adicionar = input("Qual poder gostaria de adicionar? ").lower()
    remover = input("Qual poder gostaria de remover? ").lower()
    poderes.remove(remover)
    poderes.append(adicionar)
print("Poderes apos atualização: ",poderes)

    
