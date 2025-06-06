print ("----------------------------------------------------------------------------------------------")
# Imprime una línea decorativa para separar visualmente la salida.
print("Actividad 5:Organizador de Clubes Estudiantiles")
# Muestra el título de la actividad.
print ("----------------------------------------------------------------------------------------------\n")
# Imprime otra línea decorativa y un salto de línea para formatear el output.

club_voley = [("Max", 17), ("Damián", 17), ("Maximiliano", 17), ("Matías", 17)]
# Inicializa una lista llamada 'club_voley' con tuplas, donde cada tupla representa a un miembro (nombre, edad).
club_basquet = [("Max", 17), ("Vicente", 18), ("Maximiliano", 17)]
# Inicializa una lista llamada 'club_basquet' con tuplas de miembros.
club_futbol = [("Matías", 17), ("Max", 17), ("Santos", 17)]
# Inicializa una lista llamada 'club_futbol' con tuplas de miembros.

club_voley_set = set(club_voley)
# Convierte la lista 'club_voley' en un conjunto ('set') llamado 'club_voley_set'. Los conjuntos eliminan elementos duplicados automáticamente.
club_basquet_set = set(club_basquet)
# Convierte la lista 'club_basquet' en un conjunto llamado 'club_basquet_set'.
club_futbol_set = set(club_futbol)
# Convierte la lista 'club_futbol' en un conjunto llamado 'club_futbol_set'.

print("Miembros únicos por club:")
# Imprime un encabezado para la sección de miembros únicos por club.
print(f"Club de Voley: {club_voley_set}")
# Muestra los miembros únicos del club de Voley usando un f-string para formatear la salida.
print(f"Club de Básquet: {club_basquet_set}")
# Muestra los miembros únicos del club de Básquet.
print(f"Club de Fútbol: {club_futbol_set}")
# Muestra los miembros únicos del club de Fútbol.

todos_los_alumnos = club_voley_set.union(club_basquet_set).union(club_futbol_set)
# Crea un conjunto llamado 'todos_los_alumnos' que contiene la unión de todos los miembros de los tres clubes. Los elementos duplicados se eliminan automáticamente por la operación 'union' de conjuntos.

alumnos_en_multiples_clubes = set()
# Inicializa un conjunto vacío llamado 'alumnos_en_multiples_clubes' para almacenar a los alumnos que pertenecen a más de un club.

todos_los_clubes_sets = [club_voley_set, club_basquet_set, club_futbol_set]
# Crea una lista que contiene todos los conjuntos de clubes para facilitar la iteración.

for alumno in todos_los_alumnos:
    # Inicia un bucle que itera sobre cada alumno en el conjunto 'todos_los_alumnos'.
    contador_clubes = 0
    # Inicializa un contador a cero para cada alumno, que registrará en cuántos clubes está.
    for club_set in todos_los_clubes_sets:
        # Inicia un bucle anidado que itera sobre cada conjunto de club en 'todos_los_clubes_sets'.
        if alumno in club_set:
            # Comprueba si el alumno actual se encuentra en el conjunto del club actual.
            contador_clubes += 1
            # Si el alumno está en el club, incrementa el contador de clubes.
    if contador_clubes > 1:
        # Después de revisar todos los clubes para un alumno, verifica si el contador es mayor que 1 (es decir, está en más de un club).
        alumnos_en_multiples_clubes.add(alumno)
        # Si el alumno está en más de un club, lo añade al conjunto 'alumnos_en_multiples_clubes'.

print("Alumnos que están en más de un club:")
# Imprime un encabezado para la sección de alumnos en múltiples clubes.
if alumnos_en_multiples_clubes:
    # Comprueba si el conjunto 'alumnos_en_multiples_clubes' no está vacío.
    for alumno in alumnos_en_multiples_clubes:
        # Si hay alumnos en múltiples clubes, itera sobre ellos.
        print(f"- {alumno[0]} (Edad: {alumno[1]})")
        # Imprime el nombre y la edad de cada alumno en el formato especificado.
else:
    # Si el conjunto 'alumnos_en_multiples_clubes' está vacío.
    print("No hay alumnos que estén en más de un club.")
    # Muestra un mensaje indicando que no hay alumnos en más de un club.