print("Obj: Aplicar funciones *args vs **kwargs")

print ("\n---------------------------------------------------------------------")
print("Función: lista de componentes")
print ("---------------------------------------------------------------------\n")

def mostrar_componentes(*componentes):
    print("===  Lista de componentes ===\n")
    for componente in componentes:
        print(f"> {componente}")
mostrar_componentes("Procesador", "R A M", "Placa Madre", "Tarjeta Gráfica")

print ("\n---------------------------------------------------------------------")
print("Función: llevar cosas")
print ("---------------------------------------------------------------------\n")

def detalles_componentes(**detalles):
    for clave, valor in detalles.items():
        print(f"{clave}: {valor}")
detalles_componentes(Nombre="Mely", Edad=17, Ciudad="Santiago")

print ("\n---------------------------------------------------------------------")
print("Función: llevar cosas")
print ("---------------------------------------------------------------------\n")



print ("\n---------------------------------------------------------------------")
print("Función: llevar cosas")
print ("---------------------------------------------------------------------\n")



print ("\n---------------------------------------------------------------------")
print("Función: llevar cosas")
print ("---------------------------------------------------------------------\n")



print ("\n---------------------------------------------------------------------")
print("Función: llevar cosas")
print ("---------------------------------------------------------------------\n")



print ("\n---------------------------------------------------------------------")
print("Función: llevar cosas")
print ("---------------------------------------------------------------------\n")
