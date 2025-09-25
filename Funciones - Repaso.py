# Damián Oyarce - 4°C - 25/09/2025

def estudiantes(*estudiantes, **detalles):
    print("=== Detalles ===")
    for clave, valor in detalles.items():
        print(f"- {clave}: {valor}")
    
    print("\n=== Estudiantes ===")
    for estudiante in estudiantes:
        strip = estudiante.strip()
        print(f"Nombre original: {estudiante}")
        print(f"> lower: {strip.lower()}")
        print(f"> upper: {strip.upper()}")
        print(f"> capitalize: {strip.capitalize()}")
        print(f"> title: {strip.title()}")
        print(f"> swapcase: {strip.swapcase()}\n")

estudiantes("  ana pérez morales  ",
            "JUAN soto melo",
            "cARLos loPEz RodriGuez",
            Curso="4°C", 
            Año=2025,)

print("Damián Oyarce Benavides")