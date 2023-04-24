from instaloader import Instaloader, Profile
from decouple import config


class Instagram:
    def __init__(self):
        self.instaloader = Instaloader()
        self.instaloader.login(config('INSTAGRAM_LOGIN'), config('INSTAGRAM_PASS'))

    def get_followers(self, username):
        try:
            profile = Profile.from_username(self.instaloader.context, username)
            return profile.followers
        except:
            return None


