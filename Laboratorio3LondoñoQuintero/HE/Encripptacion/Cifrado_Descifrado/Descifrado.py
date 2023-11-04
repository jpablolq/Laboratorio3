# -*- coding: utf-8 -*-

###########################################
# DescifradoRansomwareJuanPabloLondo�oQuintero
###########################################

from cryptography.fernet import Fernet
import os

###########################################

# Extensi�n de los archivos secuestrados
extension = 'IUEHackeoEtico202302'

# Cargar la clave de cifrado
def cargar_key():
    return open('key.key', 'rb').read()

# Descifrar y restaurar archivos
def descifrar(items, key):
    f = Fernet(key)
    for item in items:
        # Verificar si el archivo tiene la extensi�n adecuada para descifrar
        if item.endswith('.' + extension):
            # Leer el archivo cifrado
            with open(item, 'rb') as file:
                encrypted_data = file.read()

            # Descifrar el archivo
            decrypted_data = f.decrypt(encrypted_data)

            # Restaurar el archivo original
            original_name = os.path.splitext(item)[0]
            with open(original_name, 'wb') as file:
                file.write(decrypted_data)

            # Eliminar el archivo cifrado
            os.remove(item)

if __name__ == '__main__':
    path_to_decrypt = 'C:/Users/JuanPablo/Documents/HE/prueba'
    items = os.listdir(path_to_decrypt)
    full_path = [os.path.join(path_to_decrypt, item) for item in items]

    key = cargar_key()
    descifrar(full_path, key)