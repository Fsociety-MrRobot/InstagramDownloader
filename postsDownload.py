import instaloader

class GetPosts:
	def __init__(self, username, login, password):
		self.loader = instaloader.Instaloader()
		self.target = username
		self.login = login
		self.psswrd = password


	def getPosts(self):
		self.loader.login(self.login, self.psswrd)

		profile = instaloader.Profile.from_username(self.loader.context, self.target)

		posts_sorted = sorted(profile.get_posts(), key=lambda post: post.likes, reverse=True)

		for post in posts_sorted:
			self.loader.download_post(post, self.target)
