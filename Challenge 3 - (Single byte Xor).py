#Single-Byte XOR

from binascii import unhexlify
hx = unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
for key in range(256):
    decoded = ''.join(chr(b ^ key) for b in hx) #Doin xor on each byte of the decoded bytes
    if decoded.isprintable():
        print(key, decoded)
