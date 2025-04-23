# V1 ---------------------------------------------------------------------------------------------------------------------
"""import os # Se llama a la librería "os", que crea y administra archivos y directorios
ubicacion_carpeta = 'C:/Users/Estudiante4c2025/Documents/VS Code/principiosProgramacion2025/nuevaCarpeta'
try:
    os.makedirs(ubicacion_carpeta, exist_ok=False)
    print(f"La carpeta fue creada con éxito en: {ubicacion_carpeta}")
except PermissionError:
    print(f"No tiene permiso para crear carpetas en {ubicacion_carpeta}")
except Exception as e: # Al suceder un excepción, crea una variable llamada "e" para llamar en el print
    print(f"Ocurrió un error: {e}")
    
# V2 ---------------------------------------------------------------------------------------------------------------------
import os 
nombre_carpeta = input("Ingresa el nombre de la carpeta: ")
ubicacion_carpeta = os.path.join('C:/Users/Estudiante4c2025/Desktop', nombre_carpeta)

try:
    os.makedirs(ubicacion_carpeta, exist_ok=False)
    print(f"La carpeta fue creada con exito en: {ubicacion_carpeta}")
except PermissionError:
    print(f"No tiene permiso para crear carpetas en {ubicacion_carpeta}")
except Exception as e:
    print(f"Ocurrió un error: {e}")

# V2 + archivos ----------------------------------------------------------------------------------------------------------
ubicacion = "/Users/Estudiante4c2025/Documents/VS Code/principiosProgramacion2025/nuevoArchivo.txt"
with open(ubicacion, 'w') as archivo_datos: # La "w" sobrescribe el contenido, la "a" permite agregar texto sin necesidad de borrar lo anterior
    archivo_datos.write("Hola, estos son mis datos almacenados.\n")
    archivo_datos.write("Otra línea de información\n")
print("El mensaje fue impreso con éxito.")"""

# V2 + creación de carpetas ----------------------------------------------------------------------------------------------
ubicacion = "C:/Users/Programacion4c2025/Documents/VS Code/principiosProgramacion2025/nuevoArchivo.txt"
modo = input("¿Quieres sobrescribir el archivo (w) o agregar al archivo (a)? (w/a):\n").lower()

while modo not in ['w', 'a']:
    print("Opción no válida, debe pulsar 'w' o 'a'.")
    modo = input("¿Quieres sobrescribir el archivo (w) o agregar al archivo (a)? (w/a):\n").lower()

if modo == 'w':
    with open(ubicacion, 'w') as archivo_datos:
        archivo_datos.write("Hola, estos son mis datos.\n")
        archivo_datos.write("Otra línea de información\n")
    print("El mensaje fue impreso con éxito (sobrescritura).")
elif modo == 'a':
    with open(ubicacion, 'a') as archivo_datos:
        archivo_datos.write("Hola, estos son mis datos.\n")
        archivo_datos.write("Otra línea de información\n")
    print("El mensaje fue impreso con éxito (agregado).")