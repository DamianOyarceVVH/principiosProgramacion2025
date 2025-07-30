# Importa el módulo 'os', que nos permite interactuar con el sistema operativo,
# por ejemplo, para crear carpetas o verificar archivos.
import os

# Define la ruta de la carpeta donde se guardarán los archivos.
# En este caso, es "C://NORMALIZAR".
ruta_carpeta = "C://NORMALIZAR"

# Inicia un bloque 'try' para intentar ejecutar un código que podría causar errores.
try:
    # Intenta crear la carpeta especificada en 'ruta_carpeta'.
    # 'exist_ok=False' significa que si la carpeta ya existe, se generará un error
    # para evitar sobrescribir o crearla de nuevo innecesariamente.
    os.makedirs(ruta_carpeta, exist_ok=False)
    # Si la carpeta se crea con éxito, imprime un mensaje de confirmación.
    print(f"La carpeta fue creada con éxito en: {ruta_carpeta}")
# Si ocurre un error de 'PermissionError' (por ejemplo, no tienes permisos para crear carpetas allí),
# este bloque se ejecuta.
except PermissionError:
    # Imprime un mensaje indicando que no hay permiso para crear la carpeta.
    print(f"No tiene permiso para crear carpetas en {ruta_carpeta}")
# Si ocurre cualquier otro tipo de error inesperado, este bloque se ejecuta.
except Exception as e:
    # Imprime un mensaje general de error, mostrando la descripción del error ('e').
    print(f"Ocurrió un error: {e}")

# Define una cadena de texto larga que contiene el contenido de un "cuento".
# Esta cadena tiene una mezcla de mayúsculas y minúsculas.
el_origen = """eL oRiGeN eS uNa nOveLa dE mIsTeRiO y sUsPeNsO dE dAn bRoWn qUe cUeNtA lA hIsToRiA dE rObErT lAnGdOn, uN sYmBoLoGiStA qUe sE vE eNvUeLtO eN uN cOmPlOt qUe pOdRíA cAmBiAr eL rUmBo dE lA hUmAnIdAd.
EL LIBRO SE DESARROLLA EN ESPAÑA, ESPECÍFICAMENTE EN CIUDADES COMO BILBAO, MADRID Y BARCELONA, Y MEZCLA ELEMENTOS DE ARTE, RELIGIÓN Y TECNOLOGÍA.
en esta historia, langdon asiste a una presentación de su amigo edmond kirsch, un futurista que afirma haber descubierto el origen y el destino de la humanidad.
El OrIgEn dE lA hUmAnIdAd y sU dEsTiNo sOn tEmAs cEnTrAlEs qUe gUiAn lA tRama y lOs dEsAfÍoS qUe lOs pErSoNaJeS dEbEn eNvEnTaR pArA lLeGaR a lA vErDaD.
a tRaVéS dE cOdIgOs, pIsTaS y eNiGmAs, lAnGdOn y aMbRa vIdAl, lA dIrEcToRa dE uN mUsEo, tRaTaN dE eScApAr dE sUs pErSeGuIdOrEs mIeNtRaS rEvElAn eL mEnSaJe dE kIrScH.
uNa mEzClA dE fIcCiÓn, cOnSpIrAcIóN y cIeNcIa hAcE dE eStA nOvElA uNa aTrAyEnTe rEfLeXiÓn sObRe lA fE y lA rAzÓn.
pOr lAs cAlLeS dE bArCeLoNa y dEnTrO dE lA sAgRaDa fAmIlIa, lOs pRoTaGoNiStAs vIvEn uNa cArReRa cOnTrA eL tIeMpO pArA rEvElAr lA vErDaD.
eL oRiGeN iNvItA a lOs lEcToReS a cUeStIoNaRsE sObRe lAs cReEnCiAs rElIgIoSaS y lOs aVaNcEs tEcNoLóGiCoS qUe pOdRíAn rEvOlUcIoNaR eL mUnDo.
a lO lArGo dE sUs cApÍtUlOs, eL lIbRo mAnTiEnE eL sUsPeNsO y sOrPrEnDe cOn gIrOs iNeSpErAdOs qUe cOnViErTeN lA lEcTuRa eN uNa eXpErIeNcIa úNiCa.
eL fInAl dE eL oRiGeN pRoPoNe uNa vIsIóN sObRe lA eVoLuCiÓn y eL pApEl dE lA iNtElIgEnCiA aRtIfIcIaL eN nUeStRo fUtUrO, dEjAnDo a lOs lEcToReS cOn pReGuNtAs pRoFuNdAs y rEfLeXiOnEs."""

# Define las rutas completas para tres archivos de texto que se crearán.
archivo_cuento = "C://normalizar/libro.txt"
archivo_cuento2 = "C://normalizar/libro2.txt"
archivo_cuento3 = "C://normalizar/libro3.txt"

# Abre el archivo 'libro.txt' en modo escritura ('w').
# 'with open(...) as ...:' asegura que el archivo se cierre automáticamente después de usarlo.
with open(archivo_cuento, 'w') as libro:
    # Escribe el contenido de la variable 'el_origen' en 'libro.txt'.
    libro.write(el_origen)

# Abre el archivo 'libro2.txt' en modo escritura ('w').
with open(archivo_cuento2, 'w') as libro2:
    # Escribe el contenido de 'el_origen' en 'libro2.txt'.
    libro2.write(el_origen)

# Abre el archivo 'libro3.txt' en modo escritura ('w').
with open(archivo_cuento3, 'w') as libro3:
    # Escribe el contenido de 'el_origen' en 'libro3.txt'.
    libro3.write(el_origen)

# Imprime un mensaje confirmando que los cuentos han sido guardados en los tres archivos.
print("El cuento ha sido guardado en libro.txt, libro2.txt y libro3.txt")

# Abre 'libro.txt' en modo lectura ('r').
with open(archivo_cuento, 'r') as archivo:
    # Lee todas las líneas del archivo y las guarda en una lista llamada 'lineas'.
    lineas = archivo.readlines()
    
# Abre 'libro.txt' de nuevo en modo escritura ('w').
# Esto sobrescribirá el contenido existente del archivo.
with open(archivo_cuento, 'w') as archivo:
    # Itera sobre cada línea en la lista 'lineas'.
    for linea in lineas:
        # Escribe la línea en el archivo, pero con la primera letra de cada frase en mayúscula
        # y el resto en minúscula (usando .capitalize()).
        archivo.write(linea.capitalize())

# Abre 'libro2.txt' en modo escritura ('w').
# Esto borrará el contenido anterior de 'libro2.txt'.
with open(archivo_cuento2, 'w') as archivo:
    # Escribe la cadena "Damián Oyarce \n" en el archivo.
    archivo.write("Damián Oyarce \n")

# Abre 'libro2.txt' en modo lectura ('r').
with open(archivo_cuento2, 'r') as archivo:
    # Lee todas las líneas del archivo (que ahora solo contiene "Damián Oyarce").
    lineas = archivo.readlines()
    
# Abre 'libro2.txt' en modo adjuntar ('a').
# Esto significa que el nuevo contenido se añadirá al final del archivo sin borrar lo existente.
with open(archivo_cuento2, 'a') as archivo:
    # Escribe el contenido de 'el_origen' en el archivo, pero todo en mayúsculas (usando .upper()).
    archivo.write(el_origen.upper())
        
# Abre 'libro3.txt' en modo lectura ('r').
with open(archivo_cuento3, 'r') as archivo:
    # Lee todas las líneas de 'libro3.txt'.
    lineas = archivo.readlines()
    
# Abre 'libro3.txt' de nuevo en modo escritura ('w').
# Esto sobrescribirá su contenido.
with open(archivo_cuento3, 'w') as archivo:
    # Itera sobre cada línea que se leyó de 'libro3.txt'.
    for linea in lineas:
        # Escribe la línea en el archivo, pero todo en minúsculas (usando .lower()).
        archivo.write(linea.lower())
        
# Compara si las rutas de los archivos 'archivo_cuento' y 'archivo_cuento2' son idénticas.
# Esta comparación solo verifica si las *rutas* son las mismas, no el *contenido* de los archivos.
if archivo_cuento == archivo_cuento2:
    # Si las rutas son las mismas, imprime que los archivos son iguales.
    print("Los archivos son iguales")
else:
    # Si las rutas son diferentes, imprime que los archivos son diferentes.
    print("Los archivos son diferentes")