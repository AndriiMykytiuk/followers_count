import requests
from bs4 import BeautifulSoup


class TikTok:
    def get_followers_count(self, username):
        url = f"https://www.tiktok.com/@{username}"
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0"
        }

        soup = BeautifulSoup(requests.get(url, headers=headers).content, "html.parser")
        try:
            return soup.select_one('[title="Followers"]').text
        except AttributeError:
            return False
