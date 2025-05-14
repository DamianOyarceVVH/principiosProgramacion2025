def saludar():
    print("¡Hola! ¿Cómo estás?")
# Llamamos a la función
saludar()

# Ejemplo: Función que saluda con nombre

def saludar(nombre):
    print("Hola, " + nombre + "¿Cómo estás?")
saludar("Lisette")
saludar("Danielle")

def saludar(nombre):
    print(f"¡Hola, {nombre} ¿Cómo estás?)
saludar("Lisette")
saludar("Danielle")

# Imprimir datos concatenando valores Imprimir datos usando “f” strings

# Ejemplo: Función que devuelve un resultado

def sumar(a, b):
    resultado = a + b
    return resultado
Total = sumar (3, 5)
print("El resultado es: ", Total)

def sumar(a, b):
    resultado = a + b
    return resultado
a, b = 3, 5
Total = sumar(a, b)
print(f"El resultado de {a} + {b} es {Total}")

# Ejemplo: Si un número es par o impar

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
print(es_par(4)) # Verdadero
print(es_par(7)) # Falso

def es_par(numero):
    return numero % 2 == 0
print(f"¿Es par 4? {'Sí' if es_par(4) else 'No'}")
print(f"¿Es par 7? {'Sí' if es_par(7) else 'No'}")

# Ejemplo: Usar funciones dentro de otras funciones

def cuadrado(x):
    return x * x
def suma_de_cuadrados (a, b):
    
    return cuadrado(a) + cuadrado (b)
print(suma_de_cuadrados (2, 3))ç

def cuadrado(x):
    return x * x

def suma_de_cuadrados(a, b):
    return cuadrado(a) + cuadrado(b)
resultado = suma_de_cuadrados(2, 3)
print(f"El resultado de la suma de cuadrados es: {resultado}")

# Ejemplo: Uso de función sum

# Sumar elementos de una lista
números = [30, 4, 2025]
resultado = sum(números)
print("El resultado es: ", resultado)
# El resultado es: 2059

# Sumar con un valor inicial
números = [30, 4, 2025]
resultado_anterior = sum(números, 10)
print("El resultado es la suma de los 3 primeros valores + 10 es: ", resultado_anterior)
# El resultado es la suma de los 3 primeros valores + 10 es : 2069

# sum es una función incorporada en Python. Se utiliza para sumar los elementos de un iterable (como una lista, tupla o set).

# Ejemplo: Uso de función range

# Crear un rango de 0 a 4 (entre 0 y 4 hay 5 números)
valores = range(5)
print("Los valores existentes son:", list(valores))
# Los valores existentes son: [0, 1, 2, 3, 4]
# Crear un rango de 2 a 9 (sin incluir 10) con paso de 2
valores = range(2, 10, 2)
print("Los valores que incluye el rango son: ", list(valores))
# Los valores que incluye el rango son: [2, 4, 6, 8]

"""range es una función incorporada en Python. Se utiliza para generar una secuencia de números. Es muy
útil en bucles como for, cuando quieres iterar sobre una serie
de valores sin tener que crear una lista explícita."""

# Crear un rango descendente
valores_descendentes = range(10, 0, -1)
print("Los valores que incluye el rango son: ", list(valores_descendentes))
# Los valores que incluye el rango son: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]