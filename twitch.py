from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Twitch:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.binary_location = "/opt/headless-chromium"
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1280x1696")
        options.add_argument("--single-process")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def get_followers_count(self, username):
        url = f"https://www.twitch.tv/{username}"
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 25)
        try:
            followers = wait.until(EC.presence_of_element_located((By.XPATH, '//p[contains(text(), "followers")]')))
            return followers.text.replace(' followers', '')
        except TimeoutException:
            return False


