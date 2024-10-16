#faça um programa que mostre os 10 primeiros numeros da sequencia fibonacci

print("A sequência de Fibonacci é uma sequência numérica infinita em que cada termo a partir do terceiro é a soma dos dois termos anteriores\n")
#soliticar ao usuario quantidade de numeros que queira apresentar.
qtd_seque = int(input("Quantos numeros da sequencia fibonacci quer apresentar?(max.: 20: )"))

#Criando condicional para limitar o codigo
#if qtd_seque >20:
#    print("O limite maximo é 20. Exibindo os 20 primeiros numeros da sequencia.")
#    qtd_seque = 20


#primeiro, vamos definir os primeiros valores da sequencia.
a = 1 #primeiro digito
b = 1 # segundo digito
#alguns artigos  direcionam primeiro numero como zero, entao basta trocar o primeiro valor para 0, caso queira

#Um loop para verificar os proximos digitos do enuncioado
for i in range (qtd_seque):
    print(f"{i+1}º numero: {a}")
    #como vai funcionar: o proximo numero  é a soma dos dois numeros atuais(a+b)
    #Antes de perder o valor antigo de A, guardamos ele no B
    #Agora valor B se torna o novo A. e o novo B será a soma do a+b
    a, b= b, a+b

