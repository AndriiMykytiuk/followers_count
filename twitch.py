from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Twitch:
    def __init__(self):
        self.driver = webdriver.Remote(
            command_executor='http://chrome:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

    def get_followers_count(self, username):
        url = f"https://www.twitch.tv/{username}"
        self.driver.get(url)

        wait = WebDriverWait(self.driver, 25)
        followers = wait.until(EC.presence_of_element_located((By.XPATH, '//p[contains(text(), "followers")]')))
        return followers.text.replace(' followers', '')
