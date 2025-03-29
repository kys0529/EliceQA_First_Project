# 작업자 이름: 김다예

import json
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utils.helpers import autoLogin
from src.utils.logger import setupLogger
from src.utils import homeLocators

class home():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = setupLogger("home")

        with open("credentials.json", "r", encoding="utf-8") as f: # 나중에 auth.json 파일 이름을 credentials.json으로 변경해주기
            self.userInfo = json.load(f)

        autoLogin(self.driver, self.wait, self.userInfo)

    def goToPage(self, depth2):
        if (depth2 == "혼자 먹기"):
            self.getElement(homeLocators.HOME_ALONE_BTN).click()
        elif (depth2 == "같이 먹기"):
            self.getElement(homeLocators.HOME_TOGETHER_BTN).click()
        elif (depth2 == "회식 하기"):
            self.getElement(homeLocators.HOME_TEAM_BTN).click()            
   
    # 단일 요소를 기다릴 때
    def getElement(self, element):
        return self.wait.until(EC.presence_of_element_located(element))
  
    # 여러 요소를 기다릴 때
    def getElements(self, element):
        return self.wait.until(EC.presence_of_all_elements_located(element))
    
            