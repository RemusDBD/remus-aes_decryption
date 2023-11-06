from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import getpass

print("""
-----------------------------------------------
| Author: Remus L.                            |
| GitHub: https://github.com/RemusDBD/remus-aes_decryption/ |
| Function: This script decrypts a base64-encoded ciphertext using AES in ECB (128-bit) mode. |
-----------------------------------------------
""")

def aes_ecb_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode('utf-8')

key = getpass.getpass('Enter your secret key: ').encode()

ciphertext = base64.b64decode(getpass.getpass('Enter your base64-encoded ciphertext: '))

plaintext = aes_ecb_decrypt(ciphertext, key)
print(plaintext)

