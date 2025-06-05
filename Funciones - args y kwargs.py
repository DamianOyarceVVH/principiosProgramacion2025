print("Funciones: args y kwargs")

print ("\n---------------------------------------------------------------------")
print("Función: llevar cosas")
print ("---------------------------------------------------------------------\n")

def llevar(*cosas):
    for cosa in cosas:
        print(f"- Llevo {cosa}")
llevar("Lapiz", "Borrador", "Cartulina", "Celular")

print ("\n---------------------------------------------------------------------")
print("Función: llevar cosas")
print ("---------------------------------------------------------------------\n")

def suma_total(*args):
    return sum(args)
print(">", suma_total(3, 5))
print(">", suma_total(1, 2, 3, 4, 5))

print ("\n---------------------------------------------------------------------")
print("Función: llevar cosas")
print ("---------------------------------------------------------------------\n")

def sumar_todos(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total
print(">", sumar_todos(1, 2, 3))
print(">", sumar_todos(10, 20, 30, 40))
print(">", sumar_todos())

print ("\n---------------------------------------------------------------------")
print("Función: llevar cosas")
print ("---------------------------------------------------------------------\n")

def registrar(**datos):
    for clave, valor in datos.items():
        print(f"- {clave}: {valor}")
registrar(Nombre = "Max", Edad = 17, Ciudad = "Santiago")

print ("\n---------------------------------------------------------------------")
print("Función: llevar cosas")
print ("---------------------------------------------------------------------\n")

def saludar(**kwargs):
    if "nombre" in kwargs:
        print(f"Hola, {kwargs['nombre']}!")
    else: print("Hola, desconocido.")
    if "edad" in kwargs:
        print(f"Tienes {kwargs['edad']} años.")
saludar(nombre = "Martín")
saludar (nombre = "Alonso", edad = 17)

print ("\n---------------------------------------------------------------------")
print("Función: llevar cosas")
print ("---------------------------------------------------------------------\n")

def mostrar(*args,**kwargs):
    print("Posicionales:", args)
    print("Nombrados:" ,kwargs)
mostrar(1, 2, 3, nombre = "Yetzibel", edad = 18)

print ("\n---------------------------------------------------------------------")
print("Función: llevar cosas")
print ("---------------------------------------------------------------------\n")

def mostrar_frutas(*frutas, **detalles):
    print("=== Lista de frutas ===")
    for fruta in frutas:
        print(f"- {fruta}")
        
    print("\n === Detalles adicionales ===")
    for clave, valor in detalles.items():
        print(f"{clave}: {valor}")
    
mostrar_frutas("Manzana", "Plátano", "Naranjo", Color = "Rojo", Cantidad = 3, Estacion = "Verano")