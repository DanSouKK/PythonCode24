#faca um programa que pergunte quantas rodas tem um veiculo.
#se tiver 4 rodas, retornar carro ou van
#ser tiver 2 rodas, retornar motocicleta

print("Qual tipo de seu veiculos! ")
#recebendo uma informação e armazenando na variavel
qnt_rodas=int(input("Quantas rodas possui seu veiculo? "))

#validando apenas numeros pares, com exceção do numero 1 para validação
qnt_rodas%2==0 and qnt_rodas!=1
if(qnt_rodas==4):
    print("Seu veiculo é um carro ou uma minivan.")
elif(qnt_rodas==2):
    print("Seu veiculo é uma moto!")
elif(qnt_rodas==1):
    print("Seu veiculo é um monociclo.")
elif(qnt_rodas==6):
    print("Seu veiculo é um onibus de 3 eixos!")
elif(qnt_rodas>=8 and qnt_rodas<=20):
    print(f"Identifiquei que seu veiculo possui {qnt_rodas} rodas, podendo ser um caminhão ou carreta!")
#retornando caso nao atenda os criterios de numeros pares e qualquer outro impar exceto 1.
else:
    print("Desculpe, nao foi encontrado um veiculo correspondente ao numero de rodas!")