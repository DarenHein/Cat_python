import os 
def descargas():
    try : 
        lista = []
        usuario = os.getlogin()
        ruta = "/home"
        nueva_ruta = os.path.join(ruta,usuario)
        existe = os.path.exists(nueva_ruta)
        if existe : 
            for directorios in os.listdir(nueva_ruta): 
                if directorios == "Descargas" : 
                    ruta_final = os.path.join(nueva_ruta,directorios)
        print("ruta actual -> " , ruta_final)
        #todo ahora vamos a listar todo lo que tenga el directorios
        for elementos in os.listdir(ruta_final):
            archivo = str(elementos)
            if archivo.endswith(".jpeg"):
                archivo = os.path.abspath(archivo)
                lista.append(archivo)
        for elementos in lista : 
            print(elementos)
        pass 

    except OSError : 
        print("Error en modulo os ")