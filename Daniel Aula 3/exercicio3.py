# faca um programa que calcule o tamanho da sapato de um cachorro sabendo que sempre sera o dobro do tamanho da coleira dele.
#calcule tambem o tamanho da fucinheira sabendo que é o triplo do tamanho da coleira.

#sapato = coleira*2
#fucinheiro = coleira*3

#o programa deve pedir o tamanho da coleira do cachorro do usuario e retornar os valores de tamanho do sapato e fucinheira.

print("Qual tamanho do sapato e fucinheira comprar para seu cachorro!?")
#pedindo informação do tamanho da coleira do cachorro
coleira_tam = float(input("Qual tamanho da coleira do seu cachorro? em centimetros. :"))

#fazendo calculos dos tamanhos do sapato e fucinheira do cachorro
sapato_tam = coleira_tam*2
fucinheira_tam = coleira_tam*3

#retornando informacao dos tamanhos calculados
print("Seguem aqui as informação para suas compras!!")
print(f"O Tamanho dos sapataos para seu Cão é :{sapato_tam:.2f}cm.")
print(f"O tamanho da fucinheiro do seu cão é: {fucinheira_tam:.2f}cm.")
