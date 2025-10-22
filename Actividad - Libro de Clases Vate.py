# -*- coding: utf-8 -*-
"""
Fecha: 22-10-2025

Damián Oyarce - 4°C
"""

# LIBRO DE CLASES VATE

# Define una función llamada 'estandarizar' que recibe un texto como parámetro
def estandarizar(texto):
    # Convierte la primera letra de cada palabra en mayúscula y el resto en minúscula
    return texto.title()

# Crea un diccionario vacío llamado 'libro_clases' donde se guardará toda la información
libro_clases = {}

# Agrega un estudiante predefinido con sus asignaturas, notas y promedios
libro_clases["Juan Pérez Soto"] = {
    # Diccionario con las asignaturas del estudiante
    "Asignaturas": {
        # Cada asignatura tiene una lista de notas y su promedio calculado
        "Matemáticas": {"Notas": [6.5, 5.8, 7.0, 6.2], "Promedio": (6.5 + 5.8 + 7.0 + 6.2) / 4},
        "Lenguaje": {"Notas": [5.0, 6.0, 5.8, 6.5], "Promedio": (5.0 + 6.0 + 5.8 + 6.5) / 4},
        "Historia": {"Notas": [6.0, 6.2, 6.5, 7.0], "Promedio": (6.0 + 6.2 + 6.5 + 7.0) / 4}
    },
    # Calcula el promedio general del estudiante como el promedio de los tres promedios anteriores
    "Promedio General": (
        ((6.5 + 5.8 + 7.0 + 6.2) / 4) +
        ((5.0 + 6.0 + 5.8 + 6.5) / 4) +
        ((6.0 + 6.2 + 6.5 + 7.0) / 4)
    ) / 3
}

# Inicia un ciclo para permitir ingresar más estudiantes manualmente
while True:
    # Solicita el nombre del estudiante y lo estandariza
    nombre_estudiante = estandarizar(input("Ingrese nombre y apellidos del estudiante:\n"))
    # Crea un diccionario vacío para guardar las asignaturas de este estudiante
    asignaturas = {}

    # Inicia un ciclo para ingresar varias asignaturas
    while True:
        # Solicita el nombre de la asignatura y lo estandariza
        nombre_asignatura = estandarizar(input("Ingrese nombre de la asignatura:\n"))
        # Crea una lista vacía para almacenar las notas de esa asignatura
        notas = []

        # Inicia un ciclo para ingresar las notas
        while True:
            # Pide una nota y la convierte a tipo float
            nota = float(input("Ingrese una nota (use punto decimal):\n"))
            # Agrega la nota a la lista
            notas.append(nota)
            # Pregunta si se desea ingresar otra nota
            otra_nota = input("¿Desea ingresar otra nota para esta asignatura? (s/n):\n").lower()
            # Si la respuesta no es 's', sale del ciclo de notas
            if otra_nota != 's':
                break

        # Calcula el promedio de las notas de la asignatura
        promedio_asig = sum(notas) / len(notas)
        # Guarda la asignatura con sus notas y promedio en el diccionario
        asignaturas[nombre_asignatura] = {"Notas": notas, "Promedio": promedio_asig}

        # Pregunta si desea ingresar otra asignatura
        otra_asig = input("¿Desea ingresar otra asignatura? (s/n):\n").lower()
        # Si no, sale del ciclo de asignaturas
        if otra_asig != 's':
            break

    # Calcula el promedio general del estudiante como el promedio de los promedios de sus asignaturas
    promedio_general = sum([a["Promedio"] for a in asignaturas.values()]) / len(asignaturas)
    # Guarda los datos del estudiante en el diccionario principal
    libro_clases[nombre_estudiante] = {"Asignaturas": asignaturas, "Promedio General": promedio_general}

    # Pregunta si desea ingresar otro estudiante
    otro_estudiante = input("¿Desea ingresar otro estudiante? (s/n):\n").lower()
    # Si no, rompe el ciclo principal
    if otro_estudiante != 's':
        break

# Imprime un título para el informe final
print("\n===== LIBRO DE CLASES VATE =====\n")

# Recorre todos los estudiantes del diccionario
for estudiante, datos in libro_clases.items():
    # Muestra el nombre del estudiante
    print(f"Estudiante: {estudiante}")
    # Recorre las asignaturas del estudiante
    for asig, info in datos["Asignaturas"].items():
        # Muestra el promedio de cada asignatura con dos decimales
        print(f"  {asig}: Promedio {info['Promedio']:.2f}")
    # Muestra el promedio general del estudiante
    print(f"Promedio general: {datos['Promedio General']:.2f}\n")

# Imprime los datos finales del autor del programa
print("====================================")
print("Desarrollado por: Damian Esteban Oyarce Benavides")
print("Curso: 4°C")
print("Fecha: 22-10-2025")
print("====================================")

