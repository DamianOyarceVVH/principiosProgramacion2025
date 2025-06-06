# Obj: Aplicar funciones *args vs **kwargs

# ---
# Encabezado para la sección que explica *args en una función.
print ("\n---------------------------------------------------------------------")
print("Función args: lista de componentes")
print ("---------------------------------------------------------------------\n")

# Define una función llamada 'mostrar_componentes'.
# El * adelante de 'componentes' significa que esta función puede recibir
# cualquier cantidad de elementos (componentes) y los agrupará en una 'tupla'.
def mostrar_componentes(*componentes):
    # Imprime un título para esta sección.
    print("===  Lista de componentes ===")
    # Recorre cada 'componente' dentro de la 'tupla' que se recibió.
    for componente in componentes:
        # Imprime cada componente, precedido por un '>'.
        print(f"> {componente}")

# Llama a la función 'mostrar_componentes' pasándole varios nombres de componentes.
# Estos nombres serán recolectados por '*componentes' dentro de la función.
mostrar_componentes("Procesador", "R A M", "Placa Madre", "Tarjeta Gráfica")

# ---
# Encabezado para la sección que explica **kwargs en una función.
print ("\n---------------------------------------------------------------------")
print("Función kwargs: detalles de los componentes")
print ("---------------------------------------------------------------------\n")

# Define una función llamada 'detalles_componentes'.
# Recibe el 'componente' principal y luego, '**detalles'.
# El '**' antes de 'detalles' significa que puede recibir cualquier cantidad de
# argumentos con nombre (como 'Marca=Kingston'), y los agrupará en un 'diccionario'.
def detalles_componentes(componente, **detalles):
    # Imprime un título que incluye el nombre del componente.
    print(f"=== Detalles del componente: {componente} ===")
    # Recorre cada par de 'clave' y 'valor' (característica y descripción)
    # dentro del diccionario 'detalles'.
    for caracteristica, descripcion in detalles.items():
        # Imprime la característica y su descripción.
        print(f"{caracteristica}: {descripcion}")

# Llama a la función 'detalles_componentes' para la RAM.
# "R A M" se asigna a 'componente', y el resto de argumentos con nombre
# ('Marca', 'Capacidad', 'Velocidad') se agrupan en el diccionario 'detalles'.
detalles_componentes("R A M", Marca="Kingston", Capacidad="16GB", Velocidad="3200MHz")

# ---
# Encabezado para la sección que combina *args y **kwargs.
print ("\n---------------------------------------------------------------------")
print("Función args y kwargs: ensamblar computadora")
print ("---------------------------------------------------------------------\n")

# Define una función llamada 'ensamblar_computadora' que usa ambos:
# '*args' para una lista variable de componentes sin nombre fijo.
# '**kwargs' para detalles adicionales como si fueran un diccionario.
def ensamblar_computadora(*args, **kwargs):
    # Imprime un título general para la función de ensamblaje.
    print("=== Ensamblar una computadora ===")
    # Imprime un subtítulo para la lista de componentes.
    print("=== Componentes ===")
    # Inicializa una variable 'i' en 0 para contar los componentes.
    i = 0
    # Recorre cada 'nombre' (componente) en la tupla 'args'.
    for nombre in args:
        # Incrementa 'i' en 1 en cada iteración para numerar los componentes.
        i += 1
        # Imprime el número y el nombre del componente.
        print(f"{i}. {nombre}")
    
    # Imprime un subtítulo para los detalles de ensamblaje.
    print("\n=== Detalles ===") # Agregué un salto de línea para mejor visualización
    # Recorre cada 'clave' y 'valor' (como "Tecnico": "Carlos Sánchez")
    # dentro del diccionario 'kwargs'.
    for clave, valor in kwargs.items():
        # Imprime la clave y su valor.
        print(f"{clave}: {valor}")
        
# Llama a la función 'ensamblar_computadora'.
# Las primeras líneas son los *args (los nombres de los componentes).
# Las líneas que siguen son los **kwargs (los detalles con nombre).
ensamblar_computadora(
    "Procesador AMD Ryzen 5 7600X",
    "Placa Base MSI B650 Tomahawk WiFi",
    "16GB RAM DDR5",
    "SSD Western Digital SN770 1TB",
    "Fuente de Poder Corsair RM750e",
    Tecnico="Carlos Sánchez", # Este es un kwarg
    Fecha="2025-06-05",       # Este es otro kwarg
    Gabinete="Mid Tower"      # Y otro kwarg
  )