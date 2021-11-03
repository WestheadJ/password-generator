import os,crypt
from cryptography.fernet import Fernet




def checkForSalt():
    if os.path.isfile("./salt.txt"):
        return True
    else:
        return False

def generateSalt():
    print("--- Generating Salt ---")
    salt = crypt.mksalt(crypt.METHOD_SHA512)
    try:
        file = open("salt.txt","w")
        file.write(salt)
        file.close()
        return True
    except:
        return False

def getSalt():
    file = open("salt.txt","r")
    salt = file.readlines()
    file.close()
    return salt

def checkForKey():
    if os.path.isfile("./key.txt"):
        return True
    else:
        return False

def createKey():
    print("--- Creating Key ----")
    try:
        key = Fernet.generate_key()  # store in a secure location
        file = open("key.txt","wb")
        file.write(key)
        file.close()
        return True
    except:
        return False

def getKey():
    file = open("key.txt", "rb")
    key = file.readlines()
    file.close()
    return key