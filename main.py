import time,configs
from cryptography.fernet import Fernet


configs.checkForSalt()
print("***** Password Generator *****")
print("--- Checking if there is salt ---")

if configs.checkForSalt() == True:
    print("--- Salt Found --- ")
    salt = configs.getSalt()
else:
    print("--- No salt ---")
    if configs.generateSalt() == True:
        pass
    else:
        raise("--- Couldn't create the salt file ---")
    salt = configs.getSalt()

print("--- Checking if there is a key ---")
if configs.checkForKey() == True:
    print("--- Key Found ---")
    key = configs.getKey()
else:
    print("--- No Key ---")
    if configs.createKey() == True:
        print("--- Key Found ---")
    else:
        print("--- Couldn't create the key ---")
    key = configs.getKey()

print("""--- Starting ---""")
print("""   
***** Welcome to the password generator, it's going to ask for 
an input of a phrase, this phrase will be converted into
a password, store this phrase in a password manager. 
Whenever you need the password input it back into the
 generator and it will redefine it *****""")
time.sleep(1)
phrase = input("Enter your phrase: ")

phraseConverted = ""

for i in phrase:
    n = ord(i)
    phraseConverted += str(n)

saltConverted = ""

for i in salt[0]:
    n = ord(i)
    saltConverted += str(n)

print(phraseConverted,saltConverted)
print(len(phraseConverted))
b =int(phraseConverted)//len(phraseConverted)
phrase_encoded = str(b).encode()
salt_encoded = str(salt).encode()
f= Fernet(key[0])
phrase_encrypted = f.encrypt(phrase_encoded)
phrase = str(phrase_encrypted)[(len(phrase_encrypted)-8):(len(phrase_encrypted))]
salt_encrypted = f.encrypt(salt_encoded)
salt = str(salt_encrypted)[(len(salt_encrypted)-8):(len(salt_encrypted))]
password = salt +"1$1" + phrase
print(password)