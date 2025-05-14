# Creación de carpetas V1 -------------------------------------------------------------------------------------------------
"""import os # Se llama a la librería "os", que crea y administra archivos y directorios
ubicacion_carpeta = 'C:/Users/Estudiante4c2025/Documents/VS Code/principiosProgramacion2025/nuevaCarpeta'
try:
    os.makedirs(ubicacion_carpeta, exist_ok=False)
    print(f"La carpeta fue creada con éxito en: {ubicacion_carpeta}")
except PermissionError:
    print(f"No tiene permiso para crear carpetas en {ubicacion_carpeta}")
except Exception as e: # Al suceder un excepción, crea una variable llamada "e" para llamar en el print
    print(f"Ocurrió un error: {e}")
    
# Creación de carpetas V2 -------------------------------------------------------------------------------------------------
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

# Creación de carpetas + archivos V1 --------------------------------------------------------------------------------------
ubicacion = "/Users/Estudiante4c2025/Documents/VS Code/principiosProgramacion2025/nuevoArchivo.txt"
with open(ubicacion, 'w') as archivo_datos: # La "w" sobrescribe el contenido, la "a" permite agregar texto sin necesidad de borrar lo anterior
    archivo_datos.write("Hola, estos son mis datos almacenados.\n")
    archivo_datos.write("Otra línea de información\n")
print("El mensaje fue impreso con éxito.")

# Creación de carpetas + archivos V2 --------------------------------------------------------------------------------------
ubicacion = "C:/Users/Estudiante4c2025/Documents/VS Code/principiosProgramacion2025/nuevoArchivo.txt"
modo = input("¿Quieres sobrescribir el archivo (w) o agregar al archivo (a)? (w/a):\n")
while modo not in ['w', 'a']:
    print("Opción no valida, debe pulsar 'w' o 'a'.")
    modo = input("¿Quieres sobrescribir el archivo (w) o agregar al archivo (a)? (w/a):\n")
    
with open(ubicacion, 'w') as archivo_datos:
    archivo_datos.write("Hola, estos son mis datos.\n")
    archivo_datos.write("Otra línea de información\n")
print("El mensaje fue impreso con éxito.")

# Creación de carpetas + archivos V3 --------------------------------------------------------------------------------------
ubicacion = "C:/Users/Estudiante4c2025/Documents/VS Code/principiosProgramacion2025/nuevoArchivo.txt"
# Solicitar datos al usuario
linea_1 = input("Por favor, ingrese la primera línea de datos: ")
linea_2 = input("Por favor, ingrese la segunda línea de datos: ")

# Escribir los datos ingresados al archivo
with open(ubicacion, 'w') as archivo:
    archivo.write(linea_1 + "\n")
    archivo.write(linea_2 + "\n")
print("Los datos han sido almacenados exitosamente en el archivo.")

# Creación de carpetas + archivos V4 --------------------------------------------------------------------------------------
ubicacion = "C:/Users/Estudiante4c2025/Documents/VS Code/principiosProgramacion2025/nuevoArchivo.txt"
with open(ubicacion, 'w') as archivo:
# Solicitar cuántas líneas desea ingresar el usuario
    num_lineas = int(input("¿Cuántas líneas desea redactar?: "))

    for i in range(num_lineas):
# Solicitar al usuario una línea de datos
        linea = input(f"Por favor, ingrese la línea {i+1}: ")
        archivo.write(linea + "\n")
print("Los datos han sido almacenados exitosamente en el archivo.")