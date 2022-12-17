#Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция.
import string

print(string.punctuation + string.ascii_letters)
print(''.join([chr(i) for i in range(1072, 1104)]))
def crypt(text:str, key:int, decrypt:bool  = False):
    key = -key if decrypt else key