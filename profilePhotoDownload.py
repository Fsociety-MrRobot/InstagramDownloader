import instaloader

class GetProfilePhoto:
	def __init__(self, username, login, password):
		self.loader = instaloader.Instaloader()
		self.target = username
		self.login = login
		self.psswrd = password


	def getProfilePhoto(self):
		self.loader.login(self.login, self.psswrd)
		self.loader.download_profile(self.target, profile_pic_only=True)
