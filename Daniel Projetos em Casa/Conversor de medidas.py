#crie um programa de conversor de medidas

# Conversor de medidas

print("Conversor de medidas.")
valor = float(input("\nDigite uma medida: "))

print("\n1 - km (Kilômetros)\n2 - hm (Hectômetro)\n3 - dam (Decâmetro)\n4 - M (Metro)\n5 - dm (Decímetro)\n6 - cm (Centímetro)\n7 - mm (Milímetro)")
medida = int(input("\nEscolha a unidade da medida inserida: "))

print("\n1 - km (Kilômetros)\n2 - hm (Hectômetro)\n3 - dam (Decâmetro)\n4 - M (Metro)\n5 - dm (Decímetro)\n6 - cm (Centímetro)\n7 - mm (Milímetro)")
conversao = int(input("\nConverter para qual medida: "))

# Fatores de conversão para metros (multiplicação ou divisão com base na entrada)
fatores = {
    1: 1000,   # km para metros
    2: 100,    # hm para metros
    3: 10,     # dam para metros
    4: 1,      # metros
    5: 0.1,    # dm para metros
    6: 0.01,   # cm para metros
    7: 0.001   # mm para metros
}
unidades = {
    1: "km (Kilômetros)",
    2: "hm (Hectômetro)",
    3: "dam (Decâmetro)",
    4: "m (Metro)",
    5: "dm (Decímetro)",
    6: "cm (Centímetro)",
    7: "mm (Milímetro)"
}
# Convertendo o valor inicial para metros
valor_metros = valor * fatores[medida]

# Convertendo de metros para a medida desejada
valor_convertido = valor_metros / fatores[conversao]

# Exibindo o resultado da conversão
print(f"\n{valor} {unidades[medida]} é igual a {valor_convertido} {unidades[conversao]}.")
