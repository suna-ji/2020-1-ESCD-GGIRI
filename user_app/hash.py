import crypto
import sys
sys.modules['Crypto'] = crypto
import Crypto.Random
from Crypto.Cipher import AES
import hashlib
import binascii


# salt size in bytes
SALT_SIZE = 16

# number of iterations in the key generation
NUMBER_OF_ITERATIONS = 20

# the size multiple required for AES
AES_MULTIPLE = 16
# # From https://github.com/mitsuhiko/python-pbkdf2
# from pbkdf2 import pbkdf2_bin
def generate_salt():
    return Crypto.Random.get_random_bytes(SALT_SIZE)

def generate_key(password, salt, iterations):
    assert iterations > 0

    key = password + str(salt)
    key = key.encode('utf-8')
    for i in range(iterations):
        key = hashlib.sha256(key).digest()  

    return key

def pad_text(text, multiple):
    extra_bytes = len(text) % multiple

    padding_size = multiple - extra_bytes

    padding = chr(padding_size) * padding_size

    padded_text = text + padding

    return padded_text

def unpad_text(padded_text):
    padding_size = ord(padded_text[-1])

    text = padded_text[:-padding_size]

    return text

def encrypt(device, password, salt):
    # salt = Crypto.Random.get_random_bytes(SALT_SIZE)

    key = generate_key(password, salt, NUMBER_OF_ITERATIONS)

    cipher = AES.new(key, AES.MODE_ECB)

    if device:
        plaintext = device.device_type + device.os + device.version

    padded_plaintext = pad_text(plaintext, AES_MULTIPLE)

    ciphertext = cipher.encrypt(padded_plaintext)

    # ciphertext_with_salt = salt + ciphertext

    return ciphertext


def decrypt(ciphertext, password):
    salt = ciphertext[0:SALT_SIZE]

    ciphertext_sans_salt = ciphertext[SALT_SIZE:]

    key = generate_key(password, salt, NUMBER_OF_ITERATIONS)

    cipher = AES.new(key, AES.MODE_ECB)

    added_plaintext = cipher.decrypt(ciphertext_sans_salt)

    plaintext = unpad_text(str(added_plaintext))
    return plaintext