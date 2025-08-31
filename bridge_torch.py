# El Puente y la Antorcha

# Programa considerando la solucion matematica optima
# NOTA!!!: Esto solo sirve si A < B < C < D

# Tiempos de cada persona, ordenados de menor a mayor
tiempo_cruce = {'A': 1, 'B': 2, 'C': 5, 'D': 10}
tiempo_cruce = dict(sorted(tiempo_cruce.items(), key=lambda item: item[1]))

# La ecuacion matematica que da la solucion (tiempo minimo) es:
# min( 2A + B + C + D , A + 3B + D )
tiempo_minimo_formula = min(
    2*tiempo_cruce['A'] + tiempo_cruce['B'] + tiempo_cruce['C'] + tiempo_cruce['D'],
    tiempo_cruce['A'] + 3*tiempo_cruce['B'] + tiempo_cruce['D']
)

# Escenarios posibles
escenarios = [
    # Caso 1: B + A + C + A + D  == 2A + B + C + D
    [('A','B'), 'A', ('A','C'), 'A', ('A','D')],

    # Caso 2: B + A + D + B + B  == A + 3B + D
    [('A','B'), 'A', ('C','D'), 'B', ('A','B')],
]

# Calculando el tiempo de cada escenario
def calcular_tiempo(secuencia):
    tiempo_total = 0
    registro_cruces = []
    for paso in secuencia:
        if isinstance(paso, tuple):  # cruzan 2 personas
            t = max(tiempo_cruce[paso[0]], tiempo_cruce[paso[1]])
            registro_cruces.append(f"({tiempo_cruce[paso[0]]},{tiempo_cruce[paso[1]]}) → {t}")
            tiempo_total += t
        else:  # regresa 1 persona
            t = tiempo_cruce[paso]
            registro_cruces.append(f"{t} ← {t}")
            tiempo_total += t
    return tiempo_total, registro_cruces

# Comparando el escenario con la formula, imprimir los pasos de dicho escenario
for secuencia in escenarios:
    tiempo_total, registro_cruces = calcular_tiempo(secuencia)
    if tiempo_total == tiempo_minimo_formula:
        print("; ".join(registro_cruces) + f". Total = {tiempo_total}.")
        break
