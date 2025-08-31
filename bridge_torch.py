# El Puente y la Antorcha

# Programa considerando la solucion matematica optima
# NOTA!!!: Esto solo sirve si A < B < C < D

# Tiempos de cada persona, ordenados de menor a mayor
tiempo_cruce = {'A': 1, 'B': 2, 'C': 5, 'D': 10}
tiempo_cruce = dict(sorted(tiempo_cruce.items(), key=lambda item: item[1]))

# La ecuacion matematica que da la solucion (tiempo minimo) es:
# min( min(B + A + C + A + D, B + A + D + B + B),
#      min(2A + B + C + D, A + 3B + D) )
# la cual, traducido a codigo, es la siguiente:
tiempo_minimo_formula = min(
    min(
        tiempo_cruce['B'] + tiempo_cruce['A'] + tiempo_cruce['C'] + tiempo_cruce['A'] + tiempo_cruce['D'],
        tiempo_cruce['B'] + tiempo_cruce['A'] + tiempo_cruce['D'] + tiempo_cruce['B'] + tiempo_cruce['B']
    ),
    min(
        2*tiempo_cruce['A'] + tiempo_cruce['B'] + tiempo_cruce['C'] + tiempo_cruce['D'],
        tiempo_cruce['A'] + 3*tiempo_cruce['B'] + tiempo_cruce['D']
    )
)

# Escenarios posibles de la ecuacion con su secuencia de cruces
escenarios = [
    [('A','B'), 'A', ('C','D'), 'B', ('A','B')],
    [('A','B'), 'A', ('A','D'), 'B', ('B','C')],
    [('A','B'), 'A', ('A','C'), 'A', ('A','D')],
    [('A','B'), 'B', ('B','C'), 'B', ('B','D')]
]

# Calcular tiempo de cada escenario para imprimir el mejor
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

# Comparamos el tiempo de cada escenario e imprimimos el mejor
tiempo_minimo = None
registro_optimo = []

for secuencia in escenarios:
    tiempo_total, registro_cruces = calcular_tiempo(secuencia)
    if tiempo_minimo is None or tiempo_total < tiempo_minimo:
        tiempo_minimo = tiempo_total
        registro_optimo = registro_cruces

print("; ".join(registro_optimo) + f". Total = {tiempo_minimo}.")
