import os
import shutil
import arrow
from tqdm import tqdm
import time 

def descargas():
    try:
        lista = []
        usuario = os.getlogin()
        ruta = "/home"
        nueva_ruta = os.path.join(ruta, usuario)
        existe = os.path.exists(nueva_ruta)
        if existe:
            for directorios in os.listdir(nueva_ruta):
                if directorios == "Descargas":
                    ruta_final = os.path.join(nueva_ruta, directorios)

        for directorios, sub, files in os.walk(ruta_final):
            for archivo in files:
                ruta_absoluta = os.path.abspath(os.path.join(directorios, archivo))
                lista.append(ruta_absoluta)

        nueva_lista = []
        for elementos in lista:
            archivo = str(elementos)
            if archivo.endswith(".jpeg") or archivo.endswith(".jpg"):
                nueva_lista.append(archivo)
            else : 
                print("No encontre archivos con esa extencion ")

        directorio_final = "/home/usuario/Imágenes/"
        nuevo_directorio = directorio_final.replace("usuario", usuario)
        existe = os.path.exists(nuevo_directorio)

        if existe:
            fecha_actual = str(arrow.now())
            juntar = os.path.join(nuevo_directorio, fecha_actual)
            os.mkdir(juntar)

            # Inicializa la barra de progreso
            barra_progreso = tqdm(total=len(nueva_lista))

            for elementos in nueva_lista:
                shutil.move(elementos, juntar)
                # Actualiza la barra de progreso
                barra_progreso.update(1)
                time.sleep(2)

            # Cierra la barra de progreso
            barra_progreso.close()

    except OSError:
        print("Error en módulo os")


