#crie um programa que pergunte nome do cliente, modelo do carro, cor do veiculo e imprima uma mensagem agradecendo a preferencia

#saudacao 
print("Seja bem vindo ao lava-jato do  Senac!")
#recebendo informacoes do cliente
nome = input("Qual seu nome e sobrenome?")
print("Ola, ", nome)
carro = input("Qual carro voce esta dirigindo? ")
print("entendi, seu carro é um:",carro)
cor_carro = input("Qual a cor do seu veiculo?")
print("okay,",cor_carro)
#realizando confirmacao dos dados recebidos
print("Estamos cadastrando aqui seu veiculo, ", carro,"de cor ",cor_carro)
print("Obrigado pela preferencia",nome,)
#fazendo pedido de escolha do servico
print("Qual tipo de lavagem gostaria no seu carro hoje? ",nome)
lavagem = input("Digite aqui o tipo de lavagem: ")
print("Okay entendi, ",lavagem)
#solicitando tempo para execução do servico
print("para quando quer o serviço? Hoje ou amanha? ")
dataser = input("Escolha uma data: ")
print("Tudo bem, vamos providenciar seu serviço para ",dataser)
#finalizando e cadastrando pedido do cliente
print(nome, "agradecemos pela prefencia, em breve pode recolher seu carro")