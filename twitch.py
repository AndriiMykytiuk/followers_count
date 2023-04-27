from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Twitch:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        chrome_prefs = {}
        options.experimental_options["prefs"] = chrome_prefs
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')
        self.driver = webdriver.Chrome(options=options)

    def get_followers_count(self, username):
        url = f"https://www.twitch.tv/{username}"
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 25)
        try:
            followers = wait.until(EC.presence_of_element_located((By.XPATH, '//p[contains(text(), "followers")]')))
            return followers.text.replace(' followers', '')
        except TimeoutException:
            return False
        finally:
            self.driver.quit()

