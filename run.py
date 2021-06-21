
import platform
import subprocess
import sys
import banner as banner
import functions as func

def main(option):
	if option == '--aes':
		banner.head()
		password = input('[*] Pick a password: ')
		text_to_aes = input('[*] Enter the text to be encrypted: ')
		encrypted_text = func.aes(f'{text_to_aes}', password) 
		print('\n[*]', encrypted_text)

	elif option == '--caesar':
		banner.head()
		text_to_binary = input('[*] Enter the text to be encrypted: ')
		while True:
			try:
				s = int(input("[*] Enter the shift: ")) #how many shifts to encode in caesar
				break
			except ValueError:
				print('[!] Please enter a numerical value.')
				continue
		encrypt_text = func.caesar(text_to_binary, s)
		print('\n[*] Encrypted value:', "{}".format(encrypt_text))

	elif option == '--md5':
		func.md5()
	elif option == '--rot13':
		func.rot13()
	elif option == '--base64':
		func.base64()
	elif option == '--sha256':
		func.sha256()
	elif option == '--hex':
		func.hex()
	elif option == '--help' or option =='-h':
		banner.usage()

if __name__ == '__main__':
	options = ['--help', '-h', '--aes', '--caesar', '--md5', '--rot13', '--base64',
				'--sha256', '--hex']
	try:
		option = sys.argv[1]
		if option in options: # handle invalid options
			if platform.system() == 'Windows':
				subprocess.call('cls', shell=True)
			else:
				subprocess.call('clear', shell=True)

			main(option)
		else:
			print('[!] Option not found. Please check out the documentation.')
			raise IndexError
	except IndexError: # short documentation here
		banner.usage()
