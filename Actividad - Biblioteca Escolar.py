# Damian Oyarce - 03/04/2025
# Tipos de variables

# Información de la biblioteca del VVH
nombre_biblioteca = "Bilbioteca Escolar Vate"
capacidad_maxima = 1500
libros_disponibles = 1223

# Creación de un diccionario con los valores del libro destacado del mes
libro_destacado = {
    "título:": "La Conspiración",
    "autor:": "Dan Brown",
    "año:": 2001,
    "género:": "Novela",
    "disponible:": True
    }

# Creación de una lista de categorías de libros
categorias = ["Ficción", "No ficción", "Ciencia", "Historia", "Matemáticas"]

# Creación de una tupla con el horario de atención (hora de apertura, hora de cierre)
horario = (9, 17)

# Creación de un set con conjuntos de rut de estudiantes con préstamos activos
estudiantes_con_prestamos = {12345678, 23456789, 34567890}

# Actividad
# 1 ---------------------------------------------------------------------------
print(nombre_biblioteca)

# 2 ---------------------------------------------------------------------------
print(f"Libros restantes para la capacidad máxima: {capacidad_maxima - libros_disponibles}")

# 3 ---------------------------------------------------------------------------
categorias.append('Programación')

# 4 ---------------------------------------------------------------------------
print(f"Hora de apertura: {horario[0]}\nHora de cierre: {horario[1]}")

# 5 ---------------------------------------------------------------------------
estudiantes_con_prestamos.add("12208919")

# 6 ---------------------------------------------------------------------------
libro_destacado["disponible:"] = False

# 7 ---------------------------------------------------------------------------
print("Libro destacado (Info Actializada):")
for clave, valor in libro_destacado.items():    
    print(clave, valor)