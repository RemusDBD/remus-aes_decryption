from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256
import base64
import getpass

# Print banner
print("""
-----------------------------------------------
| Author: Remus L.                            |
| GitHub: https://github.com/RemusDBD/remus-aes_decryption/ |
| Function: This script encrypts a plaintext using AES in ECB mode and outputs a base64-encoded ciphertext. (PKCS7)|
| Version : v3 - This is an All-in-one script mixed with de/encrypt_v2 |
-----------------------------------------------
""")

def aes_ecb_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    return base64.b64encode(ciphertext).decode('utf-8')

def aes_ecb_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(base64.b64decode(ciphertext))
    plaintext = unpad(decrypted_data, AES.block_size).decode('utf-8')
    return plaintext

mode = input("Choose mode (Encryption/Decryption): ")

# Verify secret key input
while True:
    key = getpass.getpass('Enter your secret key: ')
    verify_key = getpass.getpass('Re-enter your secret key: ')
    if key == verify_key:
        key = SHA256.new(key.encode()).digest()  # Hash the key to ensure it is 32 bytes (256 bits)
        break
    else:
        print("The secret keys do not match. Please try again.")

if mode.lower() == "encryption":
    # Verify plaintext input
    while True:
        plaintext = getpass.getpass('Enter your plaintext: ')
        verify_plaintext = getpass.getpass('Re-enter your plaintext: ')
        if plaintext == verify_plaintext:
            break
        else:
            print("The plaintexts do not match. Please try again.")
    ciphertext = aes_ecb_encrypt(plaintext, key)
    print(ciphertext)

elif mode.lower() == "decryption":
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

else:
    print("Invalid mode. Please choose either 'Encryption' or 'Decryption'.")
