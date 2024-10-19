#criando uma lista com 3 pokemons
pokemons = ["Pikachu","Charmander","Bulbasaur"]

#exibindo a lista
print("Lista de pokemons: ",)

#acessando o primeiro pokemon da lista
print("Primeiro pokemon: ", pokemons[0])

#adicionando um novo pokemon lista 
pokemons.append("Squirtle")
print("Lista de pokemon apos adicionar Squirtle: ", pokemons)

#removendo o pokemon "charmander da lista"
pokemons.remove("Charmander")
print("Lista de pokemon apos remover Charmander: ", pokemons)

#exibindo o tamanho da lista
print("Numero de pokemons na lista: ", len(pokemons))