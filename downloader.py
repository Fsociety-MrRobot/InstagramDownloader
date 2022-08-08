import sys
from colorama import Fore
from postsDownload import GetPosts
from profilePhotoDownload import GetProfilePhoto 


class Downloader:
	def __init__(self, command):
		self.command = command

	def check_command(self):
		if self.command >=1 and self.command <=2 and self.command != 0:

			if self.command == 1:
				login = input(Fore.GREEN + "\nEnter your login : ")
				psswrd = input(Fore.GREEN + "Enter your password : ")
				print("")
				target = input(Fore.RED + "Enter target's username : ")

				_ex = GetProfilePhoto(username=target, login=login, password=psswrd)
				_ex.getProfilePhoto()

				sys.exit()

			elif self.command == 2: 
				login = input(Fore.GREEN + "\nEnter your login : ")
				psswrd = input(Fore.GREEN + "Enter your password : ")
				print("")
				target = input(Fore.RED + "Enter target's username : ")

				_ex = GetPosts(username=target, login=login, password=psswrd)
				_ex.getPosts()

				sys.exit()

		else:
			print(Fore.YELLOW + "Warning! Command list out of range")

			sys.exit()

def main():
	print(Fore.CYAN + "1. Download Profile Photo\n2. Download All Posts\n ")

	cmmnd = int(input("Enter command number : "))

	_ex = Downloader(cmmnd)
	_ex.check_command()

if __name__ == '__main__':
	main()
