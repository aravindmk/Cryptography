#Hex to Basee64 convert

from binascii import b2a_base64,unhexlify
a='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
b=b2a_base64(unhexlify(a)) #Decoding hex and encoding it to base64
print(b[0:len(b)-1])   #Indexing the string to remove escape sequence
