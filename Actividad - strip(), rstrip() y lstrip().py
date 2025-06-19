# Obj: Aplicar librería OS, funciones strip(), rstrip(), lstrip() , para eliminar caracteres específicos del principio y/o al final de una cadena.

print ("\n---------------------------------------------------------------------")
print("Función strip: Cuento")
print ("---------------------------------------------------------------------\n")

import os
ruta_carpeta = "C://clase"
try:
    os.makedirs(ruta_carpeta, exist_ok=False)
    print(f"La carpeta fue creada con éxito en: {ruta_carpeta}")
except PermissionError:
    print(f"No tiene permiso para crear carpetas en {ruta_carpeta}")
except Exception as e:
    print(f"Ocurrió un error: {e}")

cuento = """AEn el futuro brillante vivía la familia Supersónico, con su perro Astro y el robot
RobotinaU.
ASúper Sónico volaba a su trabajo en un platillo, mientras Ultra Sónico hacía las compras con solo presionar un botónU.
ALucero Sónico soñaba con ser cantante galáctica, y Cometín Sónico inventaba robots para no hacer la tarea.
AUn día, Astro se perdió entre satélites y meteoritosJ.
ATodos lo buscaron con su nave turbo y, al encontrarlo, hicieron una fiesta entre estrellasK.
ADesde entonces, los Supersónicos valoraron más estar juntos que cualquier tecnología8."""

archivo_cuento = "C://clase/cuento.txt"

with open(archivo_cuento, 'w') as archivo:
    archivo.write(cuento)
    

with open(archivo_cuento, 'r') as archivo:
    lineas = archivo.readlines()
    
lineas_sin_lstrip = [linea.lstrip("A") for linea in lineas]

nuevas_lineas = [linea.rstrip("UJK8\n") for linea in lineas_sin_lstrip]

with open(archivo_cuento, 'w') as archivo:
    archivo.writelines(nuevas_lineas)