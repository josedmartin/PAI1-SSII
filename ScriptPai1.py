import hashlib,  os
from datetime import datetime
#Ver todos los archivos de una carpeta y los convierte a hash en otro fichero

with open("Config.config") as configfile:
    directorio=configfile.readline().rstrip()
    sha=configfile.readlines()[0].rstrip()

lista=[]
directorio_elegido = directorio.replace("directorio=","")
sha_elegido=sha.replace("hash=","")

#fecha_actual=datetime.now()
#hora_reiniciar=fecha_actual.strftime("%H")

def main():
    directorio_listado=os.listdir(directorio_elegido)
    for archivo in directorio_listado:
        dic={"sha224":hashlib.sha224(archivo.encode('utf-8')).hexdigest(),
        "sha256":hashlib.sha256(archivo.encode('utf-8')).hexdigest(),
        "sha384":hashlib.sha384(archivo.encode('utf-8')).hexdigest()}
        print(dic)
        hash_value=dic[sha_elegido]
        lista.append(hash_value)
    
    with open("Fichero_conHashes.txt","w") as opfile:
        opfile.write("\n".join(lista))

if __name__ == '__main__':
    #if hora_reiniciar == 13:
    main()
    #else:
        #print("no es la hora")