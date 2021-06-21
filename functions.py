from base64 import b64encode
import base64 as b64
import hashlib
import random
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import codecs
import binascii
import banner as banner

## encrypt in aes
def aes(text_to_aes, password):
	#generate random salt
	salt = get_random_bytes(AES.block_size)
	#use Scrypt KDF to get private key from password
	private_key = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
	#create cipher 
	cipher_config = AES.new(private_key, AES.MODE_GCM)

	#return a dictionary with encrypted text
	cipher_text, tag = cipher_config.encrypt_and_digest(bytes(text_to_aes, 'utf-8'))
	return {
		'Cipher_text': b64encode(cipher_text).decode('utf-8'),
		'Salt': b64encode(salt).decode('utf-8'),
		'Nonce': b64encode(cipher_config.nonce).decode('utf-8'),
		'Tag': b64encode(tag).decode('utf-8')
	}

#md5 hash
def md5():
	banner.head()
	text_to_md5 = input('[*] Enter the text to be hashed: ')
	hash_object = hashlib.md5(text_to_md5.encode())
	md5_hash = hash_object.hexdigest()
	print('\n[*] Hashed value:', md5_hash)

# encrypt in rot13
def rot13():
    banner.head()
    text_to_rot = input('[*] Enter the text to be encrypted: ')
    encrypted_text = codecs.getencoder("rot-13")
    result = encrypted_text(text_to_rot)[0]
    print('\n[*] Encrypted value:', result)

# encode in base64
def base64():
    banner.head()
    text_to_64 = input('[*] Enter the text to be encoded: ')
    encode = b64.b64encode(bytes(f'{text_to_64}', "utf-8"))
    print('\n[*] Encoded value:', encode.decode('utf-8'))

# sha256 hash
def sha256():
    banner.head()
    text_to_sha = input('[*] Enter the text to be hashed: ').encode()
    encode = hashlib.sha256(text_to_sha).hexdigest()
    print('\n[*] Hashed value:', encode)

# encrypt in caesar cipher
def caesar(text_to_binary, s):
    encrypted_text = ''
    for i in range(len(text_to_binary)):
        if text_to_binary[i] == ' ':
            encrypted_text = encrypted_text + text_to_binary[i]
        elif text_to_binary[i].isupper():
            encrypted_text = encrypted_text + chr((ord(text_to_binary[i])+s-65)%26+65)
        else:
            encrypted_text = encrypted_text + chr((ord(text_to_binary[i])+s-97)%26+97)
    return encrypted_text

# encode in hex
def hex():
    banner.head()
    text_to_hex = input('[*] Enter the text to be encoded: ').encode('utf-8')
    encrypted_text = text_to_hex.hex()
    print('\n[*] Encoded value:', encrypted_text)