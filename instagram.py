from instaloader import Instaloader, Profile
from decouple import config


class Instagram:
    def __init__(self):
        USERNAME = "andrii_garden_experience"
        self.instaloader = Instaloader()
        self.instaloader.load_session_from_file(USERNAME, filename='session-andrii_garden_experience')

    def get_followers(self, username):
        try:
            profile = Profile.from_username(self.instaloader.context, username)
            return profile.followers
        except:
            return None


