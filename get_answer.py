import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys

class Fetcher:
    def __init__(self, url):
        self.driver = webdriver.PhantomJS()
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.url = url
        #
        # browser = webdriver.Chrome('/home/metulburr/chromedriver')
        # browser.get('https://www.myntra.com/watches/fossil/fossil-women-rose-gold-toned-dial-watch-es3352i/759168/buy')
        # t = browser.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "pdp-price", " " ))]')
        # print(t.text)
        #

        # self.lookup()

    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.until(expected_conditions.presence_of_element_located(
                (By.CLASS_NAME, "gsfi")
            ))
        except:
            print("Failed bro!")

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        answer = soup.find_all(class_ = "sPg")

        if not answer:
            answer = soup.find_all(class_ = "_XWk")

        # print(answer.get_text())

        self.driver.quit()
        return answer[0].get_text()