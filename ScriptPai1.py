import hashlib,  os
from datetime import datetime
#Ver todos los archivos de una carpeta y los convierte a hash en otro fichero


with open("Config.config") as configfile:
    directorio=configfile.readline().rstrip()
print(directorio)

lista=[]
directorio_ejemplo = directorio.replace("directorio=","")
print(directorio_ejemplo)
#fecha_actual=datetime.now()
#hora_reiniciar=fecha_actual.strftime("%H")

def main():
    directorio_listado=os.listdir(directorio_ejemplo)
    for archivo in directorio_listado:
        hash_value=hashlib.sha256(archivo.encode('utf-8')).hexdigest()
        lista.append(hash_value)
    
    with open("Fichero_conHashes.txt","w") as opfile:
        opfile.write("\n".join(lista))

if __name__ == '__main__':
    #if hora_reiniciar == 13:
    main()
    #else:
        #print("no es la hora")