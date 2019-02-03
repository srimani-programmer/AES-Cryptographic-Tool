# A Symmetric Cryptographic Encryption and Decryption in Python
# done b @Sri_Programmer
# Python v3.7.2

# imports 

import os
import sys
from tqdm import tqdm
from termcolor import colored,cprint

class Encryption:

	def __init__(self,filename):	# Constructor
		self.filename = filename

	def encryption(self): # Allows us to perfrom file operation

		try:
			original_information = open(self.filename,'rb')

		except (IOError, FileNotFoundError):
			cprint('File with name {} is not found.'.format(self.filename), color='red',attrs=['bold','blink'])
			sys.exit(0)

		try:

			encrypted_file_name = 'cipher_' + self.filename
			encrypted_file_object = open(encrypted_file_name,'wb')

			content = original_information.read()
			content = bytearray(content)


			key = 192
			cprint('Encryption Process is in progress...!',color='green',attrs=['bold'])
			for i,val in tqdm(enumerate(content)):
				content[i] = val ^ key
			
			encrypted_file_object.write(content)
			

		except Exception:
			cprint('Something went wrong with {}'.format(self.filename),color='red',attrs=['bold','blink'])
		finally:
			encrypted_file_object.close()
			original_information.close()

class Decryption:

	def __init__(self,filename):
		self.filename = filename

	def decryption(self):	# produces the original result
		
		try:
			encrypted_file_object = open(self.filename,'rb')

		except (FileNotFoundError,IOError):
			cprint('File with name {} is not found'.format(self.filename),color='red',attrs=['bold','blink'])
			sys.exit(0)

		try:

			decrypted_file = input('Enter the filename for the Decryption file with extension:') # Decrypted file as output

			decrypted_file_object = open(decrypted_file,'wb')

			cipher_text = encrypted_file_object.read()

			key = 192

			cipher_text = bytearray(cipher_text)

			cprint('Decryption Process is in progress...!',color='green',attrs=['bold'])

			for i,val in tqdm(enumerate(cipher_text)):
				cipher_text[i] = val^key
		
			decrypted_file_object.write(cipher_text)
			

		except Exception:
				cprint('Some problem with Ciphertext unable to handle.',color='red',attrs=['bold','blink'])

		finally:
			encrypted_file_object.close()
			decrypted_file_object.close()

space_count = 30 * ' '
cprint('{} File Encryption And Decryption Tool. {}'.format(space_count,space_count), 'red')
cprint('{} {}'.format(space_count + 3 * ' ','Programmed by Sri Manikanta.'),'green')
while True:
		cprint('1. Encryption',color='magenta')
		cprint('2. Decryption',color='magenta')
		cprint('3. Exit', color='red')
		# cprint('Enter your choice:',color='cyan',attrs=["bold"])
		cprint('~Python3:',end=' ', color='green')
		choice = int(input())

		if choice == 1:
			logo = '''  ___                       _   _          
 | __|_ _  __ _ _ _  _ _ __| |_(_)___ _ _  
 | _|| ' \/ _| '_| || | '_ \  _| / _ \ ' \ 
 |___|_||_\__|_|  \_, | .__/\__|_\___/_||_|
                  |__/|_|                  '''
			cprint(logo,color='red',attrs=['bold'])
			cprint('Enter the filename for Encryption with proper extension:',end=' ',color='yellow',attrs=['bold'])
			file = input()
			E1 = Encryption(file)
			E1.encryption()
			cprint('{} Encryption is done Sucessfully...!'.format(file), color='green',attrs=['bold'])
			cprint('Do you want to do it again (y/n):',end = ' ', color='red',attrs=['bold','blink'])
			again_choice  = input()
			if (again_choice.lower() == 'y'):
				continue
			else:
				break

		elif choice == 2:
			logo = '''  ___                       _   _          
 |   \ ___ __ _ _ _  _ _ __| |_(_)___ _ _  
 | |) / -_) _| '_| || | '_ \  _| / _ \ ' \ 
 |___/\___\__|_|  \_, | .__/\__|_\___/_||_|
                  |__/|_|                  '''
			cprint(logo,color='red',attrs=['bold'])
			cprint('Enter the Encrypted filename with proper extension:',end=' ',color='yellow',attrs=['bold'])
			file = input()
			D1 = Decryption(file)
			D1.decryption()
			cprint('{} Decryption is done Sucessfully...!'.format(file),color='green',attrs=['bold'])
			cprint('Do you want to do it again (y/n):',end = ' ', color='red',attrs=['bold','blink'])
			again_choice  = input()
			if (again_choice.lower() == 'y'):
				continue
			else:
				break
		elif choice == 3:
			sys.exit(0)
		else:
			print('Your choice of selection is not available. Sorry to see you again.')





		