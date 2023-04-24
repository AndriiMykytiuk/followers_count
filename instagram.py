from instaloader import Instaloader, Profile
import os


class Instagram:
    def __init__(self):
        self.instaloader = Instaloader()
        self.instaloader.login(os.getenv('INSTAGRAM_LOGIN'), os.getenv('INSTAGRAM_PASS'))

    def get_followers(self, username):
        try:
            profile = Profile.from_username(self.instaloader.context, username)
            return profile.followers
        except:
            return None


