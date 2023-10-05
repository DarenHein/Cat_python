# programa que busca imagenes en directorios y las mueve a un numero direcotrio con el nombre de la fecha 
# esta liminado sollo al directorio descargas  y imagagenes 
# Autor : DH
import os 
from paquete.Modulo_Descargas import descargas
from paquete.Modulo_Imagenes import imagenes
print(os.system("clear"))
print ('''
             ,---,
      ,---, ,--.' |
    ,---.'| |  |  :
    |   | : :  :  :
    |   | | :  |  |,--.
  ,--.__| | |  :  '   |
 /   ,'   | |  |   /' :
.   '  /  | '  :  | | |
'   ; |:  | |  |  ' | :
|   | '/  ' |  :  :_:,'
|   :    :| |  | ,'
 \   \  /   `--''
  `----'


''')
usuario = os.getlogin()
print("Usuario -> " , usuario)
ruta = os.getcwd()
print("Ruta actual donde se ejecuta -> ",ruta)
print("El programa busca imagenes con las extenciones .jpg , .jpeg , .png ")
print("En el los directorios siguientes ")
print("1-. Imagenes")
print("2-. Descargas ")
print("Limitado a sistemas Unix")
print("Cualquier mal uso de este program es bajo su resposabilidad DH se desblinda ")
entrar = input("Presiona enter para empezar -> ")
if entrar != "" : 
    print("Hasta luego")
elif entrar == "dh" :
    pass 
else : 
    os.system("clear")
    print("Bienvenido")
    descargas()
    #imagenes()