import os 
def descargas():
    try : 
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
        
        pass 

    except OSError : 
        print("Error en modulo os ")