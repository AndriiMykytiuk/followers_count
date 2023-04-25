from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Twitch:
    def __init__(self):
        options = ChromeOptions()
        options.add_argument("no-sandbox")
        options.accept_untrusted_certs = True
        options.assume_untrusted_cert_issuer = True
        options.add_argument("--disable-infobars")
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def get_followers_count(self, username):
        url = f"https://www.twitch.tv/{username}"
        self.driver.get(url)

        wait = WebDriverWait(self.driver, 25)
        followers = wait.until(EC.presence_of_element_located((By.XPATH, '//p[contains(text(), "followers")]')))
        return followers.text.replace(' followers', '')



# t = Twitch()
# print(t.get_followers_count('seba'))