import hashlib,  os
from datetime import datetime
#Ver todos los archivos de una carpeta y los convierte a hash en otro fichero

with open("Config.config") as configfile:
    directorio=configfile.readline().rstrip()
    sha=configfile.readlines()[0].rstrip()
    hora=configfile.readlines()[1].rstrip()

lista=[]
directorio_elegido = directorio.replace("directorio=","")
sha_elegido=sha.replace("hash=","")
hora_establecida=hora.replace("hora_comprobacion=","")


def main():
    directorio_listado=os.listdir(directorio_elegido)
    for archivo in directorio_listado:

        dic_def={}
        dic_def[archivo] = [hashlib.sha224(archivo.encode('utf-8')).hexdigest(),
        hashlib.sha256(archivo.encode('utf-8')).hexdigest(),
        hashlib.sha384(archivo.encode('utf-8')).hexdigest(),
        hashlib.sha512(archivo.encode('utf-8')).hexdigest()]

        if sha_elegido== 'sha224':
            lista.extend([archivo,dic_def[archivo][0]])
        elif sha_elegido== 'sha256':
            lista.extend([archivo,dic_def[archivo][1]])
        elif sha_elegido== 'sha384':
            lista.extend([archivo,dic_def[archivo][2]])
        elif sha_elegido== 'sha512':
            lista.extend([archivo,dic_def[archivo][3]])
        else: 
            print("hash mal escrito")
    
    with open("Fichero_conHashes.txt","w") as opfile:
        opfile.write("\n".join(lista))

if __name__ == '__main__':
    while True:
        if datetime.now().strftime('%X') == hora_establecida:
            main()
            