# dever de casa: peça para o usuario o tamanho do aro da roda na bicicleta
#recomende o tamanho do guidao, da manete e o do quadro da bicicleta
#o tamanho do guidao sera metade do tamanho do aro da roda  
#o tamanho da manete sera 1/4 do tamanho do aro da roda
#o tamanho do quadro da bicicleta sera o mesmo da roda

print("Como escolher tamanho correto da sua bicicleta?")

aro_roda =int(input("Qual tamanho do aro da roda que você quer? "))
#fazendo calculos e recomendação das peças da bicicleta
manete_tam = aro_roda/4
quadro_tam = aro_roda
guidao = aro_roda/2

#retornado as recomendaçoes para o usuario.
print("Com base no seu aro escolhido os tamanhos recomendados da sua bicicleta é?")
print(f"Tamanho da sua manete deve ser: {manete_tam}")
print(f"Tamanho do seu quadro deve ser: {quadro_tam}")
print(f"Tamanho do seu guidao deve ser: {guidao}")
