from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Hash import SHA256
import base64
import getpass

# Print banner
print("""
-----------------------------------------------
| Author: Remus L.                            |
| GitHub: https://github.com/RemusDBD/remus-aes_decryption/ |
| Function: This script decrypts a base64-encoded ciphertext using AES in ECB mode and outputs the plaintext. (PKCS7) |
| Version : v2 - Your ciphertext should be hashed using Base64, which should be able to use upside down with the aes_encryption_v2 |
-----------------------------------------------
""")

def aes_ecb_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(base64.b64decode(ciphertext))
    plaintext = unpad(decrypted_data, AES.block_size).decode('utf-8')
    return plaintext

# Verify secret key input
while True:
    key = getpass.getpass('Enter your secret key: ')
    verify_key = getpass.getpass('Re-enter your secret key: ')
    if key == verify_key:
        key = SHA256.new(key.encode()).digest()  # Hash the key to ensure it is 32 bytes (256 bits)
        break
    else:
        print("The secret keys do not match. Please try again.")

# Verify ciphertext input
while True:
    ciphertext = getpass.getpass('Enter your ciphertext: ')
    verify_ciphertext = getpass.getpass('Re-enter your ciphertext: ')
    if ciphertext == verify_ciphertext:
        break
    else:
        print("The ciphertexts do not match. Please try again.")

plaintext = aes_ecb_decrypt(ciphertext, key)
print(plaintext)
