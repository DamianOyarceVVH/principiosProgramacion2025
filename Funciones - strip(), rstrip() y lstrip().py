"""
    FUNCION STRIP()
"""

""" ELIMINAR LOS ESPACIOS DE LOS LATERALES
texto = " 4° de programacion "
print(texto)

limpiar = texto.strip()
print(f"{limpiar}")
"""

""" ELIMINAR LOS CARACTERES LATERALES SELECIONADOS EN EL STRIP
texto = "-4° de programacion!"
print(texto)

limpiar = texto.strip("!")
print(f"{limpiar}")

limpiar = texto.strip("-,!")
print(f"{limpiar}")

numeros = "B12345A"
print(numeros)

limpiar_num = numeros.strip("B,A")
print(f"{limpiar_num}")
"""

cuento = """RHabía una vez un pez llamado FLOUNDER que vivia en el
acuario de una casa azul.
RTodos los dias lo alimentaban a las 6:30 de la mañana y luego salio a
pasear por entremedio de las plantas acuaticas.
RUn dias, se encontro con un caracol manzana llamado AGUSTIN y para
el era un misterio."""
           
ruta_archivo = "C:/casa/datos.txt"

with open(ruta_archivo, 'w') as archivo:
    archivo.write(cuento)
   

with open(ruta_archivo, 'r') as archivo:
    lineas = archivo.readlines()
   
nuevas_lineas = [linea.lstrip("R") for linea in lineas]

with open(ruta_archivo, 'w') as archivo:
    archivo.writelines(nuevas_lineas)