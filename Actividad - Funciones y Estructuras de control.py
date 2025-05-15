# Damián Oyarce 4ºC - 14/05/2025

""" 1 -> Crear una función que reciba un número entero ingresado por el usuario y evalúe, si el valor
ingresado es: mayor, menor o igual a 10, aplique estructuras de control if, else, además try para
controlar las excepciones """

def numero():
    # se define una función llamada 'numero'

    while True:
        # 'while True:' crea un bucle que se repetirá indefinidamente hasta que se encuentre una instrucción 'break'
        try:
            # 'try:' inicia un bloque de código donde podrían ocurrir errores.
            valor = input("Ingrese un número: ")
            # 'input()' muestra el mensaje "Ingrese un número:" y guarda lo que escriba en la variable 'valor'
            entero = int(valor)
            # 'int()' converte el texto guardado a un número entero.

            if entero > 10:
                # 'if' es una estructura de control. Si el valor de 'entero' es mayor que 10, se ejecuta la siguiente línea
                print(f"El número {entero} es mayor que 10")
                # 'print()' muestra un mensaje indicando que el número ingresado es mayor que 10

            elif entero < 10:
                # 'elif' (else if) es otra estructura de control. Si la condición del 'if' anterior no se cumple, se verifica esta condición. Si 'entero' es menor que 10
                print(f"El número {entero} es menor que 10")
                # 'print()' muestra un mensaje indicando que el número ingresado es menor que 10.

            else:
                # 'else' se ejecuta si ninguna de las condiciones anteriores ('if' o 'elif') se cumple. En este caso, significa que 'entero' no es mayor ni menor que 10
                print(f"El número {entero} es igual que 10")
                # 'print()' muestra un mensaje indicando que el número ingresado es igual a 10.
            break
            # 'break' se utiliza para salir del bucle 'while True' una vez que el usuario ingresa un número válido
        except ValueError:
            # 'except ValueError:' captura el error específico que ocurre cuando 'int()' no puede convertir el texto ingresado a un número entero
            print("Lo que usted ingresó no es un número válido.")
            # 'print()' muestra un mensaje de error al usuario, indicando que lo que ingresó no era un número válido. El bucle 'while' continuará pidiendo un número.
numero()
# Esta línea llama a la función 'numero()' para que se ejecute el código dentro de ella.

""" 2 -> Crear una función que reciba un número con decimales ingresado por el usuario y evalúe, si el valor
ingresado es: mayor, menor o igual a 10, aplique estructuras de control if, else, además try para
controlar las excepciones """

def decimal():
    # Define una función llamada 'decimal' para comparar un número decimal con 10

    while True:
        # Bucle infinito para seguir pidiendo un decimal hasta que se ingrese uno válido
        try:
            # Bloque para intentar convertir la entrada del usuario a un número decimal
            valor = input("Ingrese un decimal: ")
            # Pide al usuario que ingrese un número decimal y lo guarda como texto en 'valor'
            dec = float(valor)
            # 'float()' intenta convertir el texto en 'valor' a un número con decimales

            if dec > 10:
                # Si el número decimal es mayor que 10
                print(f"El decimal {dec} es mayor que 10")
                # Muestra un mensaje indicando que el decimal es mayor que 10

            elif dec < 10:
                # Si el número decimal es menor que 10.
                print(f"El decimal {dec} es menor que 10")
                # Muestra un mensaje indicando que el decimal es menor que 10

            else:
                # Si el número decimal no es mayor ni menor que 10 (es igual a 10)
                print(f"El decimal {dec} es igual que 10")
                # Muestra un mensaje indicando que el decimal es igual a 10
            break
            # Sale del bucle una vez que se ingresa un decimal válido
        except ValueError:
            # Si 'float()' no puede convertir la entrada a un decimal
            print("Lo que usted ingresó no es un decimal válido.")
            # Muestra un mensaje de error al usuario
decimal()
# Llama a la función 'decimal()' para que se ejecute

""" 3 -> Crear una función que reciba un número entero ingresado por el usuario y calcule el área de un
triángulo (base * altura / 2) """

def area_triangulo():
    # Define una función llamada 'area_triangulo' para calcular el área de un triángulo
    while True:
        # Bucle infinito para asegurar que se ingresen valores válidos para la base y la altura
        try:
            # Bloque para intentar obtener la base y la altura como números enteros
            base = int(input("Ingrese la base del triángulo: "))
            # Pide al usuario que ingrese la base del triángulo y la convierte a un entero
            altura = int(input("Ingrese la altura del triángulo: "))
            # Pide al usuario que ingrese la altura del triángulo y la convierte a un entero
            area = base * (altura / 2)
            # Calcula el área del triángulo utilizando la fórmula: base * altura / 2
            print(f"El área del triángulo con base {base} y altura {altura} es: {area}")
            # Muestra el resultado del cálculo del área, incluyendo los valores de la base y la altura
            break
            # Sale del bucle una vez que se ingresan la base y la altura correctamente
        except ValueError:
            # Si 'int()' no puede convertir la entrada de la base o la altura a un entero
            print("Lo que usted ingresó no son datos válidos.")
            # Muestra un mensaje de error si el usuario no ingresa números enteros.
area_triangulo()
# Llama a la función 'area_triangulo()' para ejecutarla

""" 4 -> Crear una función que reciba un nombre y una edad, y luego imprima el siguiente mensaje: "Hola,
nombre. Me alegra que tengas edad años """

def felicidades():
    # Define una función llamada 'felicidades' para saludar al usuario
    while True:
        # Bucle infinito para asegurarse de que se ingresen datos válidos
        try:
            # Bloque para intentar obtener el nombre y la edad
            nombre = str(input("Ingrese su nombre: "))
            # Pide al usuario que ingrese su nombre y lo guarda como texto en la variable 'nombre'
            edad = int(input("Ingrese su edad: "))
            # Pide al usuario que ingrese su edad

            print(f"Hola, {nombre}. Me alegra que tengas {edad} años.")
            # Muestra un mensaje de saludo personalizado con el nombre y la edad ingresados
            break
            # Sale del bucle una vez que se ingresan el nombre y la edad correctamente
        except ValueError:
            # Si 'int()' no puede convertir la entrada de la edad a un entero
            print("Lo que usted ingresó no son datos válidos.")
            # Muestra un mensaje de error si la edad no es un número entero
felicidades()
# Llama a la función 'felicidades()' para que se ejecute

""" 5 -> Crear una función que reciba una cantidad de números definidos por el usuario y devuelva la suma de
los valores ingresados, aplique sum, range y for """

def sum_num():
    # Define una función llamada 'sum_num' para sumar números ingresados por el usuario
    cantidad = int(input("Ingresa la cantidad de números a sumar: "))
    # Pide al usuario que ingrese cuántos números quiere sumar y lo guarda como un entero en 'cantidad'
    numeros = []
    # Crea una lista vacía llamada 'numeros' donde se guardarán los números que ingrese el usuario

    for i in range(cantidad):
        # 'for' inicia un bucle que se repetirá 'cantidad' veces
        numero = int(input(f"Ingresa el numero {i + 1}: "))
        # En cada iteración, se pide al usuario que ingrese un número. 'i + 1' se usa para mostrar al usuario el número de entrada actual
        numeros.append(numero)
        # '.append()' añade el valor de 'numero' al final de la lista 'numeros'
        total = sum(numeros)
        # 'sum()' calcula la suma de todos los elementos dentro de la lista 'numeros'. El resultado se guarda en la variable 'total'
    print("El total es: ", total)
    # Después de que el bucle 'for' termina, esta línea muestra el valor de la suma total.

sum_num()
# Llama a la función 'sum_num()' para que se ejecute.