import os 
import time 
from tqdm import tqdm 
import threading
import shutil 
import arrow


def funcion(a):
    barra = tqdm(total=a,unit="Elemento")
    for i in range(a):
        time.sleep(0.5)
        barra.update(1)
    barra.close()


def imagenes():
    print("Hola mundo desde el modulo imagenes")
    try : 
        usuario = os.getlogin()
        ruta = os.getcwd()
        print("Usuario : " , usuario)
        print("Ruta actual : " , ruta)
        ruta2 = "/home/usuario/Imágenes/"
        ruta3= ruta2.replace("usuario",usuario)
        print("Ruta la cual se escaneara -> ",ruta3)
        existe = os.path.exists(ruta3)
        a = []
        if existe :
            for elementos in os.listdir(ruta3):
                a.append(elementos)
            a = len(a)
            print("Trabajando en ello .... ")
            hilo = threading.Thread(target=funcion,args=(a, ))
            hilo.start()
            print("Elementos encontrados en el direcotrio -> ")
            b = []
            for elementos in os.listdir(ruta3):
                imagenes = str(elementos)
                if imagenes.endswith(".jpg") or imagenes.endswith(".png") or imagenes.endswith(".jpeg"): 
                    b.append(imagenes)
            c = []
            for elementos in b : 
                cadena = str(elementos)
                c.append(os.path.abspath(cadena))
            for elemntos in c : 
                print(elemntos)
    except OSError : 
        print("Error en el modulo os ")