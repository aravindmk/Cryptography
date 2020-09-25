from binascii import hexlify

def repeating_key_xor(key, string):
    i = 0
    arr = []
    for ch in string:
        arr.append(ord(ch) ^ ord(key[i]))
        i += 1
        if (i == len(key)):
            i = 0
    return hexlify(bytearray(arr))

string="Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = 'ICE'

encrypted = repeating_key_xor(key, string)
print(encrypted)
