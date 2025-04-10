# Creación de una lista
estudiantes = [
    {"nombre": "Martin", "nota": 50},
    {"nombre": "Carlos", "nota": 62},
    {"nombre": "Juan", "nota": 70},
    {"nombre": "Roberto", "nota": 38},
    {"nombre": "David", "nota": 40}
    ]

# 1 & 2 -----------------------------------------------------------------------
# Agregar un nuevo estudiante usando append
estudiantes.append({"nombre": "Ana", "nota": 65})
estudiantes.append({"nombre": "Martin", "nota": 40})

# Modificar la nota de un estudiante existente
estudiantes[2]["nota"] = 68
print("Lista de estudiantes y calificaciones actualizada")

# 6 ---------------------------------------------------------------------------
# Ingreso de notas manualmente
print("Ingresa nuevos estudiantes (escribe 'fin' para terminar)")

while True:
    nombre = input("Nombre del estudiante: ")
    if nombre == 'fin':
        break  # Sale del bucle si el usuario escribe 'fin'
    try:
        nota = int(input(f"Nota de {nombre}: "))
        estudiantes.append({"nombre": nombre, "nota": nota})
    except ValueError:
        print("Por favor, ingresa una nota válida (número).")
        
# 7 ---------------------------------------------------------------------------
# Leer datos desde el archivo de texto
try:
    with open("C:/Users/4cProgramacion2025.DESKTOP-GSQNTJN/Documents/principiosProgramacion2025/estudiantes.txt", "r") as archivo:
        for linea in archivo:
            nombre, nota = linea.strip().split(",")
            estudiantes.append({"nombre": nombre, "nota": int(nota)})
except FileNotFoundError:
    print("Error: No se encontró el archivo 'estudiantes.txt'")
    exit()
except ValueError:
    print("Error: Formato incorrecto en el archivo. Asegúrate de que cada línea tenga 'nombre,nota'")
    exit()

# Variables para definir al mejor estudiante y la mejor nota
suma_notas = 0
mejor_estudiante = ""
mejor_nota = 0

# 5* --------------------------------------------------------------------------
peor_estudiante = ""
peor_nota = 70

for estudiante in estudiantes:
    nombre = estudiante["nombre"]
    nota = estudiante["nota"]
    
    suma_notas += nota 
    
    if nota > mejor_nota:
        mejor_nota = nota
        mejor_estudiante = nombre
        
    if nota < peor_nota:
        peor_nota = nota
        peor_estudiante = nombre
        
promedio = suma_notas / len(estudiantes)

# 3 & 4 -----------------------------------------------------------------------
print(f"El promedio de notas es: {promedio:.2f}")
print(f"Los estudiantes en los dos extremos de calificaciones son:\n{mejor_estudiante} con un {mejor_nota} y {peor_estudiante} con un {peor_nota}")

# 5** -------------------------------------------------------------------------
# Contar estudiantes por debajo del promedio 
cantidad_encima_promedio = 0
estudiantes_encima_promedio = []
print("\nEstudiantes por encima del promedio:")
for estudiante in estudiantes:
    if estudiante["nota"] > promedio:
        print(f"--> {estudiante['nombre']} - {estudiante['nota']}")
        cantidad_encima_promedio += 1  # Incrementar el contador
        estudiantes_encima_promedio.append(estudiante)
print(f"\nCantidad de estudiantes por encima del promedio: {cantidad_encima_promedio}")
       
# Contar estudiantes por debajo del promedio 
cantidad_debajo_promedio = 0
estudiantes_debajo_promedio = []
print("\nEstudiantes por debajo del promedio:")
for estudiante in estudiantes:
    if estudiante["nota"] < promedio:
        print(f"--> {estudiante['nombre']} - {estudiante['nota']}")
        cantidad_debajo_promedio += 1 # Incrementar el contador
        estudiantes_debajo_promedio.append(estudiante)
print(f"\nCantidad de estudiantes por debajo del promedio: {cantidad_debajo_promedio}")

