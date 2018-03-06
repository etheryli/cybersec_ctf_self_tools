from __future__ import print_function, unicode_literals
from os import urandom
import binascii
import string
import re

def genkey(length, int_seed):
    """Generate key based on repeating character"""
    ch = chr(int_seed)
    key_string = ""
    key_string += ch
    key_string = key_string.ljust(length, ch)
    return key_string.encode()
    

def xor_strings(s, t):
    """xor two strings together"""
    if isinstance(s, str):
        # Text strings contain single characters
        return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
    else:
        # Python 3 bytes objects contain integer values in the range 0-255
        return bytes([a ^ b for a, b in zip(s, t)])
        

filename = "text.txt"
data = ""
with open(filename, 'r') as f:
    content = f.read().splitlines()
    for i in range(0, len(content)):
        temp = content[i]
        for j in range(0, len(content[i]) - 1, 2):
            data+=chr(int(content[i][j:j+2], 16))
            
message = data
#print('message:', message)

key = genkey(len(message), 70)

#print('key:', key)

print("\nKey Length:", len(key), "\nData Length:", len(message))

cipherText = xor_strings(message.encode('utf-8'), key)
re.sub(r'[\x00-\x1f\x7f-\x9f]', '', cipherText)
print ('cipherText:', cipherText)
#print ('decrypted:', xor_strings(cipherText, key).decode('utf8'))

f = open("out.txt", 'w')

for i in range(0, 2):
    key = genkey(len(message), i)
    #for character in cipherText.decode('ascii','replace'):
    s = cipherText.decode('ascii', 'ignore')
    printable = set(string.printable)
    filter(lambda x: x in printable, s)
    re.sub(r'[^\x00-\x7F]+',' ', s)
    
    f.write(s)
#f.write(cipherText.decode(encoding='latin-1', errors="ignore"))
    