horas_dia = 24

sono = float(input("Horas de sono: "))
outras = float(input("Horas de outras atividades: "))

tempo_estudo = horas_dia - sono - outras

print("Tempo total para estudar:", tempo_estudo, "horas")

materia1 = input("Nome da matéria 1: ")
peso1 = float(input("Peso da matéria: "))
dif1 = float(input("Dificuldade da matéria: "))

materia2 = input("Nome da matéria 2: ")
peso2 = float(input("Peso da matéria: "))
dif2 = float(input("Dificuldade da matéria: "))

prioridade1 = peso1 * dif1
prioridade2 = peso2 * dif2

total = prioridade1 + prioridade2

tempo1 = (prioridade1 / total) * tempo_estudo
tempo2 = (prioridade2 / total) * tempo_estudo

print("Estudar", materia1, "por", tempo1, "horas")
print("Estudar", materia2, "por", tempo2, "horas")
