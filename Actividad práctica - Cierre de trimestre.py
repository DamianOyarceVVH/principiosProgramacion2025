"""intentos = []
numero = int(7)

while True:
    try:
        intento = int(input("Adivine el número del 1 al 20: "))
        intentos.append(intento)
        if intento > numero:
            print("EL número ingresado es mayor al número a adivinar.")
        elif intento < numero:
            print("EL número ingresado es menor al número a adivinar.")
        else:
            print("¡F E L I C I D A D E S, adivinó el número!")
            break
    except ValueError:
        print("Lo que ingresó no es un número entero.")
print(f'Intentos guardados:\n{intentos}')"""

# Definición de los clubes con listas de tuplas (nombre, edad)
club_literatura = [("Alice", 16), ("Bob", 17), ("Charlie", 16), ("Alice", 16)]
club_ciencia = [("Bob", 17), ("David", 15), ("Eve", 16)]
club_arte = [("Charlie", 16), ("Alice", 16), ("Frank", 18)]

# ---

## Procesamiento de los clubes

# Eliminar duplicados dentro de cada club y convertir a conjunto para facilitar comparaciones
# Convertimos las tuplas (nombre, edad) a tuplas inmutables dentro del conjunto
club_literatura_set = set(club_literatura)
club_ciencia_set = set(club_ciencia)
club_arte_set = set(club_arte)

print("---")
print("Miembros únicos por club:")
print(f"Club de Literatura: {club_literatura_set}")
print(f"Club de Ciencia: {club_ciencia_set}")
print(f"Club de Arte: {club_arte_set}")

# ---

## Encontrar alumnos en más de un club

# Unir todos los alumnos en un solo conjunto para encontrar duplicados
todos_los_alumnos = club_literatura_set.union(club_ciencia_set).union(club_arte_set)

# Conjunto para almacenar los alumnos que están en más de un club
alumnos_en_multiples_clubes = set()

# Lista de todos los clubes en formato conjunto
todos_los_clubes_sets = [club_literatura_set, club_ciencia_set, club_arte_set]

# Iterar sobre cada alumno y verificar en cuántos clubes está
for alumno in todos_los_alumnos:
    contador_clubes = 0
    for club_set in todos_los_clubes_sets:
        if alumno in club_set:
            contador_clubes += 1
    if contador_clubes > 1:
        alumnos_en_multiples_clubes.add(alumno)

print("---")
print("Alumnos que están en más de un club:")
if alumnos_en_multiples_clubes:
    for alumno in alumnos_en_multiples_clubes:
        print(f"- {alumno[0]} (Edad: {alumno[1]})")
else:
    print("No hay alumnos que estén en más de un club.")
print("---")