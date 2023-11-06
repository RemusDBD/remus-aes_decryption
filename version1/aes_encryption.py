from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import getpass

print("""
-----------------------------------------------
| Author: Remus L.                            |
| GitHub: https://github.com/RemusDBD/remus-aes_decryption/ |
| Function: This script encrypts a plaintext using AES in ECB mode and outputs a base64-encoded ciphertext. |
-----------------------------------------------
""")

def aes_ecb_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    return base64.b64encode(ciphertext).decode('utf-8')

key = getpass.getpass('Enter your secret key: ').encode()

plaintext = getpass.getpass('Enter your plaintext: ')

ciphertext = aes_ecb_encrypt(plaintext, key)
print(ciphertext)
