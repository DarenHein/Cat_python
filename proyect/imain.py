# programa que busca imagenes en directorios y las mueve a un numero direcotrio con el nombre de la fecha 
# esta liminado sollo al directorio descargas  y imagenes
# Autor : DH
import os 
from paquete.Modulo_Descargas import descargas
from paquete.Modulo_Imagenes import imagenes
print(os.system("clear"))
print ('''
       
.dP"Y8 88b 88    db    88""Yb .dP"Y8  dP"Yb  88""Yb 888888
`Ybo." 88Yb88   dPYb   88__dP `Ybo." dP   Yb 88__dP   88
o.`Y8b 88 Y88  dP__Yb  88"""  o.`Y8b Yb   dP 88"Yb    88
8bodP' 88  Y8 dP""""Yb 88     8bodP'  YbodP  88  Yb   88

''')
usuario = os.getlogin()
print("Usuario -> " , usuario)
ruta = os.getcwd()
print("Ruta actual donde se ejecuta -> ",ruta)

print("El programa busca imagenes con las extenciones .jpg , .jpeg ")
print("En el los directorios siguientes ")
print("1-. Imagenes")
print("2-. Descargas ")
print("Limitado a sistemas Unix")
print("Cualquier mal uso de este program es bajo su resposabilidad DH se desblinda ")
print("Al presionar enter se creara una carpeta en el directorio Imagenes donde se almacenara todo ")
entrar = input("Presiona enter para empezar -> ")
if entrar != "" : 
    #todo lo dejo para agregar funnciones de root 
    print("Hasta luego")
elif entrar == "dh" :
    pass 
else : 
    os.system("clear")
    print("Trabajando en ello ....")
    #descargas()
    imagenes()