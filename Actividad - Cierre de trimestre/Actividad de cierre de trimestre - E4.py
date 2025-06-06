# Imprime una línea decorativa para la sección de la actividad.
print ("----------------------------------------------------------------------------------------------")
# Imprime el título de la actividad.
print("Actividad 4: Juego de Adivina el Número con Historial ")
# Imprime otra línea decorativa seguida de un salto de línea para formatear la salida.
print ("----------------------------------------------------------------------------------------------\n")

# Inicializa una lista vacía llamada 'intentos' que almacenará los intentos del jugador.
intentos = []
# Define el número secreto que el jugador debe adivinar, en este caso, es 7.
numero = int(7)

# Inicia un bucle infinito que continuará ejecutándose hasta que se encuentre una condición para romperlo.
while True:
    # Inicia un bloque 'try' para manejar posibles errores (excepciones) durante la ejecución del código.
    try:
        # Solicita al usuario que adivine un número y convierte su entrada a un entero, almacenándola en 'intento'.
        intento = int(input("Adivine el número del 1 al 20: "))
        # Agrega el número ingresado por el usuario a la lista 'intentos', registrando cada intento.
        intentos.append(intento)
        # Comprueba si el número ingresado por el usuario es mayor que el número secreto.
        if intento > numero:
            # Si el intento es mayor, imprime un mensaje indicando que el número es demasiado alto.
            print("EL número ingresado es mayor al número a adivinar.")
        # De lo contrario, comprueba si el número ingresado es menor que el número secreto.
        elif intento < numero:
            # Si el intento es menor, imprime un mensaje indicando que el número es demasiado bajo.
            print("EL número ingresado es menor al número a adivinar.")
        # Si ninguna de las condiciones anteriores se cumple, significa que el intento es igual al número secreto.
        else:
            # Imprime un mensaje de felicitación porque el usuario adivinó el número.
            print("¡F E L I C I D A D E S, adivinó el número!")
            # Rompe el bucle 'while True', terminando el juego.
            break
    # Captura la excepción 'ValueError' si ocurre, lo que sucede si el usuario no ingresa un número entero.
    except ValueError:
        # Imprime un mensaje de error indicando que la entrada no fue un número válido.
        print("Lo que ingresó no es un número entero.")
# Después de que el bucle termina, imprime un mensaje mostrando todos los intentos que el usuario realizó.
print(f'Intentos guardados:\n{intentos}')