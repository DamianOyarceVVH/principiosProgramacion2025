# --------------------------------------------------------------------------------------------------------------------------------
intentos = []
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
print(f'Intentos guardados:\n{intentos}')

# --------------------------------------------------------------------------------------------------------------------------------
club_voley = [("Max", 17), ("Damián", 17), ("Maximiliano", 17), ("Matías", 17)]
club_basquet = [("Max", 17), ("Vicente", 18), ("Maximiliano", 17)]
club_futbol = [("Matías", 17), ("Max", 17), ("Santos", 17)]

# Eliminar duplicados dentro de cada club y convertir a conjunto para facilitar comparaciones
# Convertimos las tuplas (nombre, edad) a tuplas inmutables dentro del conjunto
club_voley_set = set(club_voley)
club_basquet_set = set(club_basquet)
club_futbol_set = set(club_futbol)

print("Miembros únicos por club:")
print(f"Club de Voley: {club_voley_set}")
print(f"Club de Básquet: {club_basquet_set}")
print(f"Club de Fútbol: {club_futbol_set}")

todos_los_alumnos = club_voley_set.union(club_basquet_set).union(club_futbol_set)

alumnos_en_multiples_clubes = set()

todos_los_clubes_sets = [club_voley_set, club_basquet_set, club_futbol_set]

for alumno in todos_los_alumnos:
    contador_clubes = 0
    for club_set in todos_los_clubes_sets:
        if alumno in club_set:
            contador_clubes += 1
    if contador_clubes > 1:
        alumnos_en_multiples_clubes.add(alumno)

print("Alumnos que están en más de un club:")
if alumnos_en_multiples_clubes:
    for alumno in alumnos_en_multiples_clubes:
        print(f"- {alumno[0]} (Edad: {alumno[1]})")
else:
    print("No hay alumnos que estén en más de un club.")