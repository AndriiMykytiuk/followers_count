from instaloader import Instaloader, Profile
import os


class Instagram:
    def __init__(self):
        self.instaloader = Instaloader()
        self.instaloader.login('andrii_garden_experience', 'baxVOtU33z4$')

    def get_followers(self, username):
        try:
            profile = Profile.from_username(self.instaloader.context, username)
            return profile.followers
        except:
            return None


