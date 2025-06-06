print ("----------------------------------------------------------------------------------------------")
print("Actividad 2: Verificador de Votación en Club Escolar")
print ("----------------------------------------------------------------------------------------------\n")

def verificador_votacion():
    # Inicializa una lista vacía llamada 'participantes' para guardar tuplas (nombre, edad) de cada persona.
    participantes = []
    # Inicializa otra lista vacía llamada 'votantes_aptos' para almacenar a quienes cumplan con la edad mínima para votar.
    votantes_aptos = []

    # Imprime un encabezado para el programa en la consola.
    print("--- Verificador de Votación en Club Escolar ---")
    # Imprime instrucciones para el usuario sobre cómo ingresar los datos y cómo terminar.
    print("Ingresa los datos de los participantes. Escribe 'listo' en el nombre para terminar.")

    # Inicia un bucle infinito que permite al usuario ingresar múltiples participantes.
    while True:
        # Pide al usuario que ingrese el nombre del participante
        nombre = input("\nIngresa el nombre del participante: ")
        # Comprueba si el nombre ingresado (convertido a minúsculas) es "listo".
        if nombre.lower() == 'listo':
            # Si es "listo", sale del bucle principal de ingreso de participantes.
            break
        
        # Inicia un bucle interno para asegurar que la edad ingresada sea válida.
        while True:
            try:
                # Intenta convertir la cadena de texto 'edad_str' a un número entero.
                edad = int(input(f"Ingresa la edad de {nombre}: "))
                participantes.append((nombre, edad))
                # Sale del bucle interno de ingreso de edad, porque la edad es válida.
                break
            # Captura la excepción ValueError si la conversión de 'edad_str' a entero falla.
            except ValueError:
                # Imprime un mensaje de error indicando que la edad no es un número válido.
                print("Error: La edad debe ser un número entero válido.")
    
    # Imprime un encabezado indicando que se va a proceder a verificar los votantes.
    print("\n--- Verificando quiénes pueden votar ---")
    # Itera sobre cada tupla (nombre, edad) en la lista 'participantes'.
    for nombre, edad in participantes:
        # Comprueba si la edad del participante es mayor o igual a 14.
        if edad >= 14:
            # Si la edad es 14 o más, agrega la tupla (nombre, edad) a la lista 'votantes_aptos'.
            votantes_aptos.append((nombre, edad))
            # Imprime un mensaje indicando que el participante puede votar.
            print(f"{nombre} (Edad: {edad}) puede votar.")
        # Si la edad es menor de 14.
        else:
            # Imprime un mensaje indicando que el participante no puede votar y la razón.
            print(f"{nombre} (Edad: {edad}) no puede votar por ser menor de 14 años.")

verificador_votacion()