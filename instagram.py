from instaloader import Instaloader, Profile


class Instagram:
    def __init__(self):
        USERNAME = "PUT YOUR USERNAME HERE"
        self.instaloader = Instaloader()
        self.instaloader.load_session_from_file(USERNAME, filename='<filename>')

    def get_followers(self, username):
        try:
            profile = Profile.from_username(self.instaloader.context, username)
            return profile.followers
        except:
            return None