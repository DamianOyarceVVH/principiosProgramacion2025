# Obj: Aplicar librería OS, funciones strip(), rstrip(), lstrip() , para eliminar caracteres específicos del principio y/o al final de una cadena.

# Imprime una línea separadora
print ("\n---------------------------------------------------------------------")
# Imprime el título de la sección actual, indicando que se trata de la función strip con un cuento.
print("Función strip: Cuento")
# Imprime otra línea separadora
print ("---------------------------------------------------------------------\n")

# Importa el módulo 'os' que proporciona funciones para interactuar con el sistema operativo, como la creación de directorios
import os
# Define la ruta de la carpeta donde se creará el archivo del cuento
ruta_carpeta = "C://clase"
# Inicia un bloque try-except para manejar posibles errores durante la creación de la carpeta
try:
    # 'exist_ok=False' asegura que se lance un error si la carpeta ya existe, evitando sobrescribir o ignorar la existencia
    os.makedirs(ruta_carpeta, exist_ok=False)
    # Si la carpeta se crea con éxito, imprime un mensaje de confirmación
    print(f"La carpeta fue creada con éxito en: {ruta_carpeta}")
# Captura una excepción 'PermissionError' si el programa no tiene los permisos necesarios para crear la carpeta.
except PermissionError:
    # Imprime un mensaje indicando que no hay permisos
    print(f"No tiene permiso para crear carpetas en {ruta_carpeta}")
# Captura cualquier otra excepción que pueda ocurrir durante la creación de la carpeta
except Exception as e:
    # Imprime un mensaje de error genérico junto con la descripción del error
    print(f"Ocurrió un error: {e}")

# Define una cadena de texto multilinea que representa el cuento
cuento = """AEn el futuro brillante vivía la familia Supersónico, con su perro Astro y el robot RobotinaU.
ASúper Sónico volaba a su trabajo en un platillo, mientras Ultra Sónico hacía las compras con solo presionar un botónU.
ALucero Sónico soñaba con ser cantante galáctica, y Cometín Sónico inventaba robots para no hacer la tarea.
AUn día, Astro se perdió entre satélites y meteoritosJ.
ATodos lo buscaron con su nave turbo y, al encontrarlo, hicieron una fiesta entre estrellasK.
ADesde entonces, los Supersónicos valoraron más estar juntos que cualquier tecnología8."""

# Define la ruta completa del archivo donde se guardará el cuento
archivo_cuento = "C://clase/cuento.txt"

# Abre el archivo especificado en modo escritura ('w'). Si el archivo no existe, lo crea, y si existe, borra su contenido
with open(archivo_cuento, 'w') as archivo:
    # Escribe el contenido de la variable 'cuento' en el archivo
    archivo.write(cuento)
    
# Abre el mismo archivo en modo lectura ('r')
with open(archivo_cuento, 'r') as archivo:
    # Lee todas las líneas del archivo y las almacena como una lista de cadenas en 'lineas'
    # Cada elemento de la lista incluirá el carácter de nueva línea ('\n')
    lineas = archivo.readlines()
    
# Crea una nueva lista 'lineas_sin_lstrip'
# 'lstrip("A")' elimina todas 'A' del principio de cada cadena.
# 'rstrip' permite que elimine los caracteres 'U', 'J', 'K', '8' al final de cada linea
nuevas_lineas = [linea.lstrip("A").rstrip("UJK8.\n") for linea in lineas]

# Abre el archivo nuevamente en modo escritura ('w') para sobrescribir su contenido
with open(archivo_cuento, 'w') as archivo:
    # Escribe todas las cadenas de la lista 'nuevas_lineas' en el archivo, añadiendo un salto de línea a cada una
    for linea in nuevas_lineas:
        archivo.write(linea + ".\n")
    
# Imprime la lista 'nuevas_lineas' en la consola
print(nuevas_lineas)