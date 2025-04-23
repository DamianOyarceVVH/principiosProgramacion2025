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
    print(f"Ocurrió un error: {e}")"""

# V2 + archivos ----------------------------------------------------------------------------------------------------------
ubicacion = "/Users/Estudiante4c2025/Documents/VS Code/principiosProgramacion2025/nuevoArchivo.txt"
with open(ubicacion, 'w') as archivo_datos:
    archivo_datos.write("Hola, estos son mis datos almacenados.\n")
    archivo_datos.write("Otra línea de información\n")
# La "w" sobrescribe el contenido, la "a" permite agregar texto sin necesidad de borrar lo anterior