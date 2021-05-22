from base64 import b64encode
import base64 as b64
import hashlib
import random
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import codecs
import binascii

#for ascii-art
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format


#encrypt in rot13
def rot13():
	text_to_rot = input('Enter the text to be encrypted: ')
	encrypted_text = codecs.getencoder("rot-13")
	result = encrypted_text(text_to_rot)[0]
	print('\n', result)

#encrypt in base64
def base64():
	text_to_64 = input('Enter the text to be encrypted: ')
	encode = b64.b64encode(bytes(f'{text_to_64}', "utf-8"))
	print('\n', encode.decode('utf-8'))
	

#encrypt in aes
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



#encrypt in sha256
def sha256():
	text_to_sha = input('Enter the text to be encrypted: ').encode()
	encode = hashlib.sha256(text_to_sha).hexdigest()
	print('\n', encode)
	

#encrypt in caesar cipher
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

#encrypt in md5
def md5():
	text_to_md5 = input('Enter the text to be encrypted: ')
	hash_object = hashlib.md5(text_to_md5.encode())
	md5_hash = hash_object.hexdigest()
	print('\n', md5_hash)
	
#encrypt in hex
def hex():
	text_to_hex = input('Enter the text to be encrypted: ').encode('utf-8')
	encrypted_text = text_to_hex.hex()
	print('\n', encrypted_text)

#ascii-art
cprint(figlet_format('Encryption', font='isometric1'),
	'yellow', attrs=['bold'])
cprint(figlet_format('@author: prodseanb', font='mini'),
	'white', attrs=['bold'])

#user input validation
while True:
	#main block
	print('\n' + 'Pick an encryption method: [aes, md5, base64, caesar, sha256, rot13, hex]')
	print("'x', 'exit', 'q', or 'quit' to exit.")
	select = input('Select: ')

	if select.lower() == 'md5':
		md5()
	elif select.lower() == 'hex':
		hex()
	elif select.lower() == 'rot13':
		rot13()
	elif select.lower() == 'base64':
		base64()
	elif select.lower() == 'sha256' or select.lower() == 'sha':
		sha256()

	elif select.lower() == 'caesar':
		text_to_binary = input('Enter the text to be encrypted: ')
		s = int(input("Enter the shift: ")) #how many shifts to encode in caesar
		encrypt_text = caesar(text_to_binary, s)
		print('\n', "{}".format(encrypt_text))

	elif select.lower() == 'aes':
		password = input('Pick a password: ')
		text_to_aes = input('Enter the text to be encrypted: ')
		encrypted_text = aes(f'{text_to_aes}', password) #encrypt in aes
		print('\n', encrypted_text)

	#allow user to exit
	elif select.lower() in ['x', 'exit', 'quit', 'q']:
		exit()
	else:
		print('Invalid input, try again.')
		continue