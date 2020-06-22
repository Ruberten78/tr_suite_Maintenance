from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os


class WEBDRIVER:
    # +++ TEST CHROME WINDOWS +++
    # https://sites.google.com/a/chromium.org/chromedriver/downloads
    # http://chromedriver.storage.googleapis.com/index.html?path=2.21/

    def __init__(self):

        path_directory = os.path.dirname(__file__)
        print(path_directory)

        self.pathchrome  = path_directory + "/chromedriver.exe"
        self.pathfirefox = path_directory + "/geckodriver.exe"

    def driverchrome(self):
        """ """

        driver = webdriver.Chrome(executable_path=self.pathchrome)
        # driver.fullscreen_window()

        #driver.implicitly_wait(10)
        print('driver chrome connect')

        return driver

    def driverchrome_headless(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")

        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=self.pathchrome)
        # driver.fullscreen_window()

        driver.implicitly_wait(10)
        print('driver chrome connect')

        return driver

    def firefox(self):
        """ """
        print(self.pathfirefox)

        binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        options = Options()
        options.set_headless(headless=False)
        options.binary = binary
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True  # optional
        driver = webdriver.Firefox(firefox_options=options, capabilities=cap,
                                   executable_path=self.pathfirefox)

        return driver

    def webdriver_close(self, driver):

        driver.close()


if __name__ == "__main__":

    test = WEBDRIVER()
    url = 'http://www.google.it'

    driver = test.firefox()
    driver.get(url)
    test.webdriver_close(driver)

    driver = test.driverchrome()
    driver.get(url)
    test.webdriver_close(driver)
