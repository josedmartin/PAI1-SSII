import hashlib, datetime, os

#Ver todos los archivos de una carpeta y los convierte a hash en otro fichero

directorio_ejemplo = '/Users/Pablo/Desktop/UNIVERSIDAD/PAI/PAI1/Carpeta_Para_Hashear'
lista=[]
def main():
    directorio_listado=os.listdir(directorio_ejemplo)
    for archivo in directorio_listado:
        hash_value=hashlib.sha256(archivo.encode('utf-8')).hexdigest()
        lista.append(hash_value)
    
    with open("Fichero_conHashes.txt","w") as opfile:
        opfile.write("\n".join(lista))

if __name__ == '__main__':
    main()