#define starting string
import string

test1 = 0x42696c6c792c20646f6e27
test2 = 0x742062652061206865726f


str1 = "42696c6c792c20646f6e27"
str2 = "742062652061206865726f"
str3 = "1111111111111111111111"
#define strings as hex
#h=int(str1 , 16)
#n=int(str2 , 16)
result = ""
for i in range(0, len(str1) - 1, 2):
    ah = int(str1[i:i+2], 16)
    ch = int(str2[i:i+2], 16)
    dh = int(str3[i:i+2], 16)
    result += chr( dh ^ ch ^ ah)

print(result)

def genkey(length, int_seed):
    """Gerate key based on repeating char"""
    print ("seed", int_seed)
    ch = chr(int_seed)
    print("char: " + ch)
    key_string = str(ch)
    key_string = key_string.ljust(100, ch)
    return key_string

print(genkey(1000, 55))