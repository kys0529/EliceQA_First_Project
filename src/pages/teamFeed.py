# 작업자 이름: @@@

import json
import time
from faker import Faker
from PIL import Image, ImageChops
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utils import teamFeedLocators
from src.utils.helpers import autoLogin
from src.utils.logger import setupLogger

class teamFeed():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = setupLogger("teamFeed")

        with open("credentials.json", "r", encoding="utf-8") as f: # 나중에 auth.json 파일 이름을 credentials.json으로 변경해주기
            self.userInfo = json.load(f)

        autoLogin(self.driver, self.wait, self.userInfo)
        
    def getElement(self, element):
        result = self.wait.until(EC.presence_of_element_located(element))
        return result
    
    def goToPage(self, depth):
        if depth == "팀 피드":
            self.getElement(teamFeedLocators.TEAM_FEED_TAB).click()
        
        
    