# Damián Oyarce - 4°C - 25/09/2025

def estudiantes(*estudiantes, **detalles):  # Función que recibe varios estudiantes y detalles adicionales
    print("=== Detalles ===")  # Encabezado para la sección de detalles
    for clave, valor in detalles.items():  # Recorre los detalles entregados como diccionario
        print(f"- {clave}: {valor}")  # Muestra cada detalle en formato clave: valor
    
    print("\n=== Estudiantes ===")  # Encabezado para la sección de estudiantes
    for estudiante in estudiantes:  # Recorre cada estudiante recibido
        strip = estudiante.strip()  # Elimina espacios al inicio y al final del nombre
        print(f"Nombre original ({estudiante})")  # Imprime el nombre tal como fue ingresado
        print(f"> lstrip ({estudiante.lstrip()})") # Elimina espacios al inicio del nombre
        print(f"> rstrip ({estudiante.rstrip()})") # Elimina espacios al inicio del nombre
        print(f"> lower ({strip.lower()})")  # Convierte todo el nombre a minúsculas
        print(f"> upper ({strip.upper()})")  # Convierte todo el nombre a mayúsculas
        print(f"> capitalize ({strip.capitalize()})")  # Primera letra mayúscula, el resto minúsculas
        print(f"> title ({strip.title()})")  # Pone mayúscula en cada palabra
        print(f"> swapcase ({strip.swapcase()})\n")  # Invierte mayúsculas y minúsculas

estudiantes("  ana pérez morales  ",
            "JUAN soto melo",
            "cARLos loPEz RodriGuez",
            Curso="4°C", 
            Año=2025,)  # Llamada a la función pasando estudiantes y detalles adicionales

print("=== Damián Oyarce Benavides ===") # Mi nombre