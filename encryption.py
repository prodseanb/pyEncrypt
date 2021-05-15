import base64
import hashlib

#encrypt with base64
def base64():
	text_to_64 = input('Enter the text to be encrypted: ')
	encode = base64.b64encode(bytes(f'{text_to_64}', "utf-8"))
	print(encode.decode('utf-8'))
	exit()

#encrypt with sha256
def sha256():
	text_to_sha = input('Enter the text to be encrypted: ').encode()
	encode = hashlib.sha256(text_to_sha).hexdigest()
	print(encode)
	exit()

#encrypt with caesar cipher
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

#encrypt with md5
def md5():
	text_to_md5 = input('Enter the text to be encrypted: ')
	hash_object = hashlib.md5(text_to_md5.encode())
	md5_hash = hash_object.hexdigest()
	print(md5_hash)
	exit()
##next: user input validation
while True:
	print('Pick an encryption method: md5, base64, caesar, sha256')
	select = input('Select: ')

	if select.lower() == 'md5':
		md5()
	elif select.lower() == 'base64':
		base64()
	elif select.lower() == 'sha256':
		sha256()
	elif select.lower() == 'caesar':
		text_to_binary = input('Enter the text to be encrypted: ')
		s = int(input("Enter shift: "))
		encrypt_text = caesar(text_to_binary, s)
		print("{}".format(encrypt_text))
		exit()
	else:
		print('Invalid input, try again.')
		continue
