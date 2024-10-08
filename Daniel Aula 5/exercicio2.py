#faca um programa para um lava rapido onde
#lavagem completa $50, lavagem basica $35
#caso o usuario queira adicionar cera nas rodas custara +$5
#retorne o servico + valor dele 

print("Bem vindo ao lava jato Senac!\n")
item1 = "Lavagem completa"
item2 = "Lavagem básica"

escolha=int(input("1 - Lavagem completa $50\n2 - Lavagem basica $35\nDigite aqui: "))
if(escolha==1):
    print(f"\nVocê escolheu a {item1} e custará $50.")
    valortotal = 50
elif(escolha==2):
    print(f"\nVocê escolheu {item2} e custará $35.")
    valortotal = 35
extra = input("\nVocê gostaria de adicionar cera e pretinho por +$5? sim ou não: ").lower()
if extra=="sim":
    valortotal+=5
    print(f"\nO seu servico ficara em ${valortotal}.")
elif extra=="não" or "nao":
        print(f"\nO seu servico ficara em ${valortotal}.")
else:
    print(f"\nO seu serviço ficara em ${valortotal}.")
print("------------Obrigado por escolher nossos serviços, volte sempre!------------\n")
print("\nfim.")
