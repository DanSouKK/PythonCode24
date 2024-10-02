#pergunte a idade de uma pessoa, e calcule desconto seguintes produtos
  #calca azul = $ 120
  #jaqueta verde = $150
# sabendo que o valor do desconto é equilavente a idade, exemplo.
# idade = desconto
# 45 = $45 desconto e etc

print("Ola voce esta na lojinha do Senac")
#armazenando o valor da variavel
idade = int(input("Qual a sua idade? "))
#valor dos produtos
calca = float(120.25)
jaqueta = float(150.10)
#valor dos produtos com os descontos
total = calca+jaqueta-idade*2
print("Qual item vai querer comprar?")
#apresentando o valor dos produtos
print("Calça azul? Custa ",calca)
print("Jaqueta verde? Custa ",jaqueta)
#apresentando o valor de descontos recebido
print("você recebera desconto de $",idade,"em ambos itens.")
#apresentando o valor total da compra
print("Total da sua comprar deu: ","Calça = ",calca, "+ jaqueta ", jaqueta, " = ",calca+jaqueta)
print("Seu desconto é: ",idade*2)
print("Sua compra no total deu: $",total)