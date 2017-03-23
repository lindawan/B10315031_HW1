# Test the Encrypt and Decrypt method
from EncryptAndDecrypt import *

# Plaintext
p = 'sentfrommyiphone'

# Caesar Cipher, key:3
print("\n--Encrypt Caesar Cipher--")
print("Plaintext: " + p)
c = Caesar_Encrypt(p, 3)
print("\n--Decrypt Caesar Cipher--")
print("Cipher: " + c)
Caesar_Decrypt(c, 3)

""" Monoalphabetic cipher
 key:
 abcdefghijklmnopqrstuvwxyz
 QWERTYUIOPASDFGHJKLZXCVBNM """
print("\n--Encrypt Monoalphabetic Cipher--")
print("Plaintext: " + p)
c = Mono_Encrypt(p, 'QWERTYUIOPASDFGHJKLZXCVBNM')
print("\n--Decrypt Monoalphabetic Cipher--")
print("Cipher: " + c)
Mono_Decrypt(c, 'QWERTYUIOPASDFGHJKLZXCVBNM')

# Playfair Cipher, key:DPP
print("\n--Encrypt Playfair Cipher--")
print("Plaintext: " + p)
c = Playfair_Encrypt(p, 'DPP')
print("\n--Decrypt Playfair Cipher--")
print("Cipher: " + c)
Playfair_Decrypt(c, 'DPP')

# Vernam proposed the autokey system, key: KMT
print("\n--Encrypt Autokey Cipher--")
print("Plaintext: " + p)
c = Autokey_Encrypt(p, 'KMT')
print("\n--Decrypt Autokey Cipher--")
print("Cipher: " + c)
Autokey_Decrypt(c, "KMT")

# Row transposition, key: 52834671
print("\n--Encrypt Row transposition Cipher--")
print("Plaintext: " + p)
c = Rowtrans_Encrypt(p, '52834671')
print("\n--Decrypt Row transposition Cipher--")
print("Cipher: " + c)
Rowtrans_Decrypt(c, '52834671')

# Product Cipher
"""
	  01 02 03 04 05 06 07 08
	  09 10 11 12 13 14 15 16
key:
	  15 11 02 10 16 03 07 14
	  04 12 09 06 01 05 08 13 
"""
print("\n--Encrypt Product Cipher--")
print("Plaintext: " + p)
c = Product_Encrypt(p, [15, 11, 2, 10, 16, 3, 7, 14,4, 12, 9, 6, 1, 5, 8, 13])
print("\n--Decrypt Product Cipher--")
print("Cipher: " + c)
Product_Decrypt(c, [15, 11, 2, 10, 16, 3, 7, 14,4, 12, 9, 6, 1, 5, 8, 13])