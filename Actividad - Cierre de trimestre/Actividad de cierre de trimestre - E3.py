# Imprime una línea decorativa para el encabezado.
print("----------------------------------------------------------------------------------------------")
# Imprime el título de la actividad.
print("Actividad 3: Clasificador de Palabras Únicas y Repetidas")
# Imprime otra línea decorativa y un salto de línea.
print("----------------------------------------------------------------------------------------------\n")

# Define una función llamada 'clasificador_palabras'.
def clasificador_palabras():
    # Inicializa una lista vacía para almacenar todas las palabras ingresadas.
    lista_palabras = []
    # Inicializa un conjunto vacío para almacenar palabras que se consideran únicas.
    palabras_unicas = set()
    # Inicializa un conjunto vacío para almacenar palabras que se han repetido.
    palabras_repetidas = set()

    # Imprime un encabezado para la sección de ingreso de palabras.
    print("--- Clasificador de Palabras Únicas y Repetidas ---")
    # Imprime una instrucción para el usuario sobre cómo terminar el ingreso.
    print("Ingresa palabras. Escribe 'fin' para terminar.")

    # Inicia un bucle infinito para permitir al usuario ingresar múltiples palabras.
    while True:
        # Solicita al usuario que ingrese una palabra, elimina espacios y la convierte a minúsculas.
        palabra = input("Ingresa una palabra: ").strip().lower()
        # Verifica si la palabra ingresada es 'fin'.
        if palabra == 'fin':
            # Si es 'fin', sale del bucle.
            break
        # Agrega la palabra ingresada a la lista 'lista_palabras'.
        lista_palabras.append(palabra)
    
    # Imprime un encabezado para la sección de clasificación.
    print("\n--- Clasificando palabras ---")
    # Itera sobre cada palabra en la 'lista_palabras' ingresada por el usuario.
    for palabra in lista_palabras:
        # Comprueba si la palabra actual ya se encuentra en el conjunto 'palabras_unicas'.
        if palabra in palabras_unicas:
            # Si la palabra ya estaba en 'palabras_unicas', significa que es una repetición, así que se añade a 'palabras_repetidas'.
            palabras_repetidas.add(palabra)
            # Comprueba nuevamente si la palabra está en 'palabras_unicas' (esto es para un caso específico de lógica).
            if palabra in palabras_unicas:
                # Si la palabra está en 'palabras_unicas', se remueve de allí porque ahora es una palabra repetida.
                palabras_unicas.remove(palabra)
        # Si la palabra no está en 'palabras_unicas' y tampoco está en 'palabras_repetidas'.
        elif palabra not in palabras_repetidas:
            # Se agrega la palabra al conjunto 'palabras_unicas', ya que es la primera vez que se ve y aún no se ha repetido.
            palabras_unicas.add(palabra)
            
    # Inicializa un conjunto vacío para almacenar las palabras únicas finales.
    final_unicas = set()
    # Inicializa un conjunto vacío para almacenar las palabras repetidas finales.
    final_repetidas = set()
    
    # Itera de nuevo sobre cada palabra en la 'lista_palabras' para una clasificación más precisa.
    for palabra in lista_palabras:
        # Usa el método 'count()' para verificar si la palabra aparece más de una vez en 'lista_palabras'.
        if lista_palabras.count(palabra) > 1:
            # Si la palabra aparece más de una vez, se agrega al conjunto 'final_repetidas'.
            final_repetidas.add(palabra)
        # Si la palabra aparece solo una vez.
        else:
            # Se agrega la palabra al conjunto 'final_unicas'.
            final_unicas.add(palabra)

    # Imprime un encabezado para mostrar los resultados.
    print("\n--- Resultados ---")
    # Imprime el título para las palabras únicas.
    print("Palabras Únicas:")
    # Comprueba si el conjunto 'final_unicas' no está vacío.
    if final_unicas:
        # Itera sobre cada palabra en 'final_unicas', convirtiéndolo a lista y ordenándolo alfabéticamente para imprimir.
        for palabra in final_unicas:
            # Imprime cada palabra única con un guion.
            print(f"- {palabra}")
    # Si el conjunto 'final_unicas' está vacío.
    else:
        # Imprime un mensaje indicando que no se encontraron palabras únicas.
        print("No se encontraron palabras únicas.")

    # Imprime el título para las palabras repetidas.
    print("\nPalabras Repetidas:")
    # Comprueba si el conjunto 'final_repetidas' no está vacío.
    if final_repetidas:
        # Itera sobre cada palabra en 'final_repetidas', convirtiéndolo a lista y ordenándolo alfabéticamente para imprimir.
        for palabra in final_repetidas:
            # Imprime cada palabra repetida con un guion.
            print(f"- {palabra}")
    # Si el conjunto 'final_repetidas' está vacío.
    else:
        # Imprime un mensaje indicando que no se encontraron palabras repetidas.
        print("No se encontraron palabras repetidas.")

# Llama a la función 'clasificador_palabras' para iniciar el programa.
clasificador_palabras()