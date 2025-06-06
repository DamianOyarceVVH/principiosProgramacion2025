def registro_alumnos():
    alumnos = []  # Lista de tuplas para almacenar (nombre, numero)
    numeros_registrados = set()  # Conjunto para verificar números únicos

    print("--- Registro de Alumnos ---")
    print("Ingresa 'salir' en el nombre para terminar.")

    while True:
        nombre = input("\nIngresa el nombre del alumno: ").strip()
        if nombre.lower() == 'salir':
            break

        while True:
            try:
                numero = int(input(f"Ingresa el número de lista para {nombre}: "))
                if numero <= 0:
                    print("Error: El número de lista debe ser un entero positivo.")
                elif numero in numeros_registrados:
                    print(f"Error: El número de lista {numero} ya ha sido usado. Intenta con otro.")
                else:
                    alumnos.append((nombre, numero))
                    numeros_registrados.add(numero)
                    print(f"¡{nombre} registrado con el número {numero}!")
                    break  # Sale del bucle de número de lista
            except ValueError:
                print("Error: El número de lista debe ser un número entero válido.")
    
    print("\n--- Alumnos Registrados ---")
    if alumnos:
        for nombre, numero in alumnos:
            print(f"Nombre: {nombre}, Número de Lista: {numero}")
    else:
        print("No se registraron alumnos.")

# Ejecutar la función
registro_alumnos()