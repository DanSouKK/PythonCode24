# Inicializa uma lista para armazenar as notas
notas = []

print("Digite a nota do aluno (ou um número negativo para encerrar): ")

while True:
    nota = float(input())
    
    if nota < 0:
        break  # Encerra o loop se o número for negativo
    
    notas.append(nota)  # Adiciona a nota à lista

# Verifica se foram inseridas notas
if notas:  # Verifica se a lista não está vazia
    media = sum(notas) / len(notas)
    nota_maxima = max(notas)
    nota_minima = min(notas)
    
    # Exibe os resultados
    print(f"Número total de notas: {len(notas)}")
    print(f"Média das notas: {media:.2f}")
    print(f"Nota mais alta: {nota_maxima}")
    print(f"Nota mais baixa: {nota_minima}")
else:
    print("Nenhuma nota foi inserida.")