# Función simple que saluda
def saludar(nombre):
    print(f"¡Hola!, {nombre} ¿Cómo estás?")
# Llamamos a la función
saludar("Maximiliano")
saludar("Benjamín")

# Función que suma dos números
def sumar(a, b):
    resultado = a + b
    return resultado
a = int(input("Ingrese un número: "))
b = int(input("Ingrese un número: "))
total = sumar(a, b)
print(f"El resultado de {a} + {b} es {total}")

#
def par(numero):
    return numero % 2 == 0

print(f"¿Es par 4? {'Si' if par(4) else 'No'}")
print(f"¿Es par 7? {'Si' if par(7) else 'No'}")