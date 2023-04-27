from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Twitch:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.binary_location = "/opt/headless-chromium"
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1280x1696")
        options.add_argument("--single-process")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome("/opt/chromedriver",
                                  options=options)

    def get_followers_count(self, username):
        url = f"https://www.twitch.tv/{username}"
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 25)
        followers = wait.until(EC.presence_of_element_located((By.XPATH, '//p[contains(text(), "followers")]')))
        return followers.text.replace(' followers', '')


