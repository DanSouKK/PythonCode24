#Eu sou obrigado a votar?


#variavel perguntando idade do usuario
idade = int(input("Qual sua Idade? "))
#recebendo e validando variavel recebida para retornar uma condição
if(idade>=18 and idade<=65):
      print("Sim, você é obrigado a votar!")
#retornado o caso contrario caso nao atenda os criterios
else:
    print("Não, você nao é obrigado a votar!")
