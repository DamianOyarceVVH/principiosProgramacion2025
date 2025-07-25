# Damián Oyarce - 4°C
# Importa el módulo 'os', que nos permite interactuar con el sistema operativo,
# por ejemplo, para crear carpetas o verificar archivos.
import os

# Define la ruta de la carpeta donde se guardarán los archivos.
# En este caso, es "C://NORMALIZAR".
ruta_carpeta = "C://NORMALIZAR"

# Inicia un bloque 'try' para intentar ejecutar un código que podría causar errores.
try:
    # Intenta crear la carpeta especificada en 'ruta_carpeta'.
    # 'exist_ok=True' significa que si la carpeta ya existe, no se generará un error,
    # simplemente se asegura de que la carpeta exista. Esto es útil para evitar errores
    # si el script se ejecuta varias veces.
    os.makedirs(ruta_carpeta, exist_ok=True)
    # Si la carpeta se crea con éxito o ya existe, imprime un mensaje de confirmación.
    print(f"La carpeta fue creada o ya existe en: {ruta_carpeta}")
# Si ocurre un error de 'PermissionError' (por ejemplo, no tienes permisos para crear carpetas allí),
# este bloque se ejecuta.
except PermissionError:
    # Imprime un mensaje indicando que no hay permiso para crear la carpeta.
    print(f"No tiene permiso para crear carpetas en {ruta_carpeta}")
# Si ocurre cualquier otro tipo de error inesperado, este bloque se ejecuta.
except Exception as e:
    # Imprime un mensaje general de error, mostrando la descripción del error ('e').
    print(f"Ocurrió un error inesperado al crear la carpeta: {e}")

# Define una cadena de texto larga que contiene el contenido de la historia "El Origen".
el_origen = """eL oRiGeN eS uNa nOveLa dE mIsTeRiO y sUsPeNsO dE dAn bRoWn qUe cUeNtA lA hIsToRiA dE rObErT lAnGdOn, uN sYmBoLoGiStA qUe sE vE eNvUeLtO eN uN cOmPlOt qUe pOdRíA cAmBiAr eL rUmBo dE lA hUmAnIdAd.
EL LIBRO SE DESARROLLA EN ESPAÑA, ESPECÍFICAMENTE EN CIUDADES COMO BILBAO, MADRID Y BARCELONA, Y MEZCLA ELEMENTOS DE ARTE, RELIGIÓN Y TECNOLOGÍA.
en esta historia, langdon asiste a una presentación de su amigo edmond kirsch, un futurista que afirma haber descubierto el origen y el destino de la humanidad.
El OrIgEn dE lA hUmAnIdAd y sU dEsTiNo sOn tEmAs cEnTrAlEs qUe gUiAn lA tRama y lOs dEsAfÍoS qUe lOs pErSoNaJeS dEbEn eNvEnTaR pArA lLeGaR a lA vErDaD.
a tRaVéS dE cOdIgOs, pIsTaS y eNiGmAs, lAnGdOn y aMbRa vIdAl, lA dIrEcToRa dE uN mUsEo, tRaTaN dE eScApAr dE sUs pErSeGuIdOrEs mIeNtRaS rEvElAn eL mEnSaJe dE kIrScH.
uNa mEzClA dE fIcCiÓn, cOnSpIrAcIóN y cIeNcIa hAcE dE eStA nOvElA uNa aTrAyEnTe rEfLeXiÓn sObRe lA fE y lA rAzÓn.
pOr lAs cAlLeS dE bArCeLoNa y dEnTrO dE lA sAgRaDa fAmIlIa, lOs pRoTaGoNiStAs vIvEn uNa cArReRa cOnTrA eL tIeMpO pArA rEvElAr lA vErDaD.
eL oRiGeN iNvItA a lOs lEcToReS a cUeStIoNaRsE sObRe lAs cReEnCiAs rElIgIoSaS y lOs aVaNcEs tEcNoLóGiCoS qUe pOdRíAn rEvOlUcIoNaR eL mUnDo.
a lO lArGo dE sUs cApÍtUlOs, eL lIbRo mAnTiEnE eL sUsPeNsO y sOrPrEnDe cOn gIrOs iNeSpErAdOs qUe cOnViErTeN lA lEcTuRa eN uNa eXpErIeNcIa úNiCa.
eL fInAl dE eL oRiGeN pRoPoNe uNa vIsIÓn sObRe lA eVoLuCiÓn y eL pApEl dE lA iNtElIgEnCiA aRtIfIcIaL eN nUeStRo fUtUrO, dEjAnDo a lOs lEcToReS cOn pReGuNtAs pRoFuNdAs y rEfLeXiOnEs."""

# Define las rutas completas para los tres archivos de texto que se crearán.
archivo_libro = "C://NORMALIZAR/libro.txt"
archivo_libro2 = "C://NORMALIZAR/libro2.txt"
archivo_libro3 = "C://NORMALIZAR/libro3.txt"

# Abre el archivo 'libro.txt' en modo escritura ('w').
# 'with open(...) as ...:' asegura que el archivo se cierre automáticamente después de usarlo.
try:
    with open(archivo_libro, 'w') as libro:
        # Escribe el contenido de la variable 'el_origen' en 'libro.txt'.
        libro.write(el_origen)
    print("Libro creado y con la historia copiada.")

    # Abre el archivo 'libro2.txt' en modo escritura ('w').
    with open(archivo_libro2, 'w') as libro2:
        # Escribe el contenido de 'el_origen' en 'libro2.txt'.
        libro2.write(el_origen)
    print("Libro 2 creado y con la historia copiada.")

    # Abre el archivo 'libro3.txt' en modo escritura ('w').
    with open(archivo_libro3, 'w') as libro3:
        # Escribe el contenido de 'el_origen' en 'libro3.txt'.
        libro3.write(el_origen)
    print("Libro 3 creado y con la historia copiada.")

except Exception as e:
    print(f"Error al crear o escribir en los archivos: {e}")

# Normalización para 'libro.txt': Párrafos inician con mayúscula, el resto en minúscula. (Punto 5)
try:
    with open(archivo_libro, 'r') as f:
        contenido = f.read()

    # Divide el contenido en párrafos usando doble salto de línea como separador.
    # Esto asume que los párrafos están separados por una línea en blanco.
    parrafos = contenido.split('\n\n')
    
    # Procesa cada párrafo: capitaliza la primera letra y pone el resto en minúsculas.
    # Luego, une los párrafos de nuevo con doble salto de línea.
    normalizado_libro = '\n\n'.join([p.capitalize() for p in parrafos])

    with open(archivo_libro, 'w') as f:
        f.write(normalizado_libro)
    print(f"'{os.path.basename(archivo_libro)}' normalizado (primera letra de párrafo en mayúscula, resto en minúscula).")

except Exception as e:
    print(f"Error al normalizar: {e}")

# Normalización para 'libro2.txt': Todos los párrafos en mayúscula. (Punto 6)
# Primero, abrimos en modo escritura para añadir el nombre. (Punto 8)
try:
    with open(archivo_libro2, 'w') as nombre:
        # Escribe el nombre en la primera línea, seguido de un salto de línea.
        nombre.write("Damián Oyarce\n")
        # Luego, escribe el contenido original de 'el_origen' en mayúsculas.
        # Esto sobrescribe el contenido anterior de libro2.txt y añade el nombre al principio.
        nombre.write(el_origen.upper())
    print(f"'{os.path.basename(archivo_libro2)}' actualizado con el nombre y todo en mayúsculas.")

    # Conversores que no se utilizan (aún asi es una demostración)
    print("\n--- Demostración de otras funciones de cadena ---")
    print(f"Ejemplo de .title() (cada palabra inicia con mayúscula):")
    print(el_origen.split('\n')[0].title()) # Muestra la primera línea con title()
    print(f"Ejemplo de .swapcase() (invierte mayúsculas y minúsculas):")
    print(el_origen.split('\n')[0].swapcase()) # Muestra la primera línea con swapcase()
    print("------------------------------------------------------------------\n")

except Exception as e:
    print(f"Error al normalizar: {e}")

# Normalización para 'libro3.txt': Todos los párrafos en minúsculas. (Punto 7)
try:
    with open(archivo_libro3, 'w') as f:
        # Escribe el contenido original de 'el_origen' todo en minúsculas.
        # Esto sobrescribe el contenido anterior de libro3.txt.
        f.write(el_origen.lower())
    print(f"'{os.path.basename(archivo_libro3)}' normalizado (todo en minúsculas).")

except IOError as e:
    print(f"Error al normalizar: {e}")

# --- Comparación de Archivos ---

# Inicializa variables para almacenar el contenido de los archivos.
contenido_libro = ""
contenido_libro2 = ""

try:
    # Abre 'libro.txt' en modo lectura y lee todo su contenido.
    with open(archivo_libro, 'r') as f:
        contenido_libro = f.read()
    
    # Abre 'libro2.txt' en modo lectura y lee todo su contenido.
    with open(archivo_libro2, 'r') as f:
        contenido_libro2 = f.read()

    # Compara el contenido de ambos archivos.
    if contenido_libro == contenido_libro2:
        print(f"El contenido de '{os.path.basename(archivo_libro)}' y '{os.path.basename(archivo_libro2)}' es idéntico.")
    else:
        print(f"El contenido de '{os.path.basename(archivo_libro)}' y '{os.path.basename(archivo_libro2)}' es diferente.")

except FileNotFoundError:
    print("Uno o ambos archivos no fueron encontrados para la comparación.")
except IOError as e:
    print(f"Error al leer archivos para la comparación: {e}")

