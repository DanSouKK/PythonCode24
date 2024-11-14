#Pedreira mir4
#programa para calcular quantidade de aço negro minerado por hora

def calcular_producao_aco_negro(tempo_ciclo_segundos, quantidade_aco_por_ciclo, horas_mineracao):
    # Converter horas de mineração para segundos
    tempo_total_segundos = horas_mineracao * 3600
    
    # Calcular quantos ciclos completos de mineração ocorrem no tempo total
    ciclos = tempo_total_segundos // tempo_ciclo_segundos
    
    # Calcular a produção total de aço negro
    producao_total = ciclos * quantidade_aco_por_ciclo
    
    return producao_total

# Exemplo de uso
tempo_ciclo = int(input("Insira qual seu tempo medio de mineração: "))  # segundos
quantidade_aco = int(input("Insira quantidade media de aço negro minerado por ciclo: "))  # aço negro minerado por ciclo
horas_mineracao = int(input("Insira por quantidade de horas minerando: "))  # horas

producao_final = calcular_producao_aco_negro(tempo_ciclo, quantidade_aco, horas_mineracao)
print(f"A produção final de aço negro será(média): {producao_final}")
