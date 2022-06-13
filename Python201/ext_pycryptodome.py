from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

key = get_random_bytes(32)
print(key)
print(len(key))

#salt is used prevent dictionary based attacks
#random 

salt = b':\xfd\x99\xa7;\xdcc\xfe\xb3b\xb8*&e?\x81\x17U\xc9\r\xfe\xecZ?s\xb1\xa4{\x89\xbd\xbd-'
password = "hunter2"
key = PBKDF2(password, salt, dkLen=32)

print(key)
print(len(key))