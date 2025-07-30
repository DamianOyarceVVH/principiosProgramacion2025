ejemplo = "Cuarto Medio de Programación"
resultado = ejemplo.lower()
print(resultado)

"""

Uso de funcion lower(): Convierte todos los caracteres de una cadena a minúsculas

"""

Palabra1 = "JavaScript"
Palabra2 = "C+"

if Palabra1.lower() == Palabra2.lower():
    print("Las palabras son iguales")
else:
    print("Las palabras son diferentes")

"""

Lista de palabras en minúsculas

"""

frutas = ["PHYSALIS", "kumquat", "LoganBerry"]
frutas_minusculas = [f.lower() for f in frutas]
print(frutas_minusculas)

"""

Uso de función upper(): Convierte todos los caracteres de una cadena a mayúsculas

"""

Palabra1 = "JavaScript"
Palabra2 = "C+"

if Palabra1.upper() == Palabra2.upper():
    print("Las palabras son iguales")
else:
    print("Las palabras son diferentes")

"""

Uso de función capitalize(): Convierte en mayúsculas la primera letra de la cadena y convertir el resto en minúsculas

"""

ejemplo = "Vate Vicente Huidobro"
resultado = ejemplo.capitalize()
print(resultado)

"""

Uso de función title(): Convierte en mayúscula la primera letra de cada palabra
    
"""

ejemplo = "Vaya pedazo de plotwist"
resultado = ejemplo.title()
print(resultado)

"""

Uso de función swapcase(): Invierte las mayúsculas y minúsculas de cada letra
    
"""

ejemplo = "Cuarto Medio de Programación"
resultado = ejemplo.swapcase()
print(resultado)
