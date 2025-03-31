# 작업자 이름: 윤찬유
import os
import json
import time
import random
from PIL import Image, ImageChops
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from src.utils import historyLocators
from src.utils.helpers import autoLogin
from src.utils.logger import setupLogger

class history():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = setupLogger("history")

        with open("credentials.json", "r", encoding="utf-8") as f: # 나중에 auth.json 파일 이름을 credentials.json으로 변경해주기
            self.userInfo = json.load(f)

        autoLogin(self.driver, self.wait, self.userInfo)
        
    def goToPage(self, depth2):
        if (depth2 == "히스토리"):
            self.getElement(historyLocators.HISTORY_BTN).click()
        elif (depth2 == "후기등록혼밥"):
            self.getElement(historyLocators.HISTORY_BTN).click()
            self.getElement(historyLocators.RECOMEND_HON_BTN).click()
        
    # 단일 요소를 기다릴 때
    def getElement(self, element):
        return self.wait.until(EC.presence_of_element_located(element))
  
    # 여러 요소를 기다릴 때
    def getElements(self, element):
        return self.wait.until(EC.presence_of_all_elements_located(element))
    
    def screenDiff(self, locator, funcName, imageName, action, msg=""):
        time.sleep(2)
        self.driver.save_screenshot(f"reports/screenshots/{funcName}_{imageName}_before.png")
        
        if (action == "click"):
            self.getElement(locator).click()
        elif (action == "send"):
            self.getElement(locator).send_keys(msg)
        elif (action == "image"):
            imagePath = os.path.abspath(os.path.join("src/resources/assets", msg))
            self.getElement(locator).send_keys(imagePath)

        time.sleep(2)
        self.driver.save_screenshot(f"reports/screenshots/{funcName}_{imageName}_after.png")

        isDiff =  ImageChops.difference(Image.open(f"reports/screenshots/{funcName}_{imageName}_before.png"), Image.open(f"reports/screenshots/{funcName}_{imageName}_after.png"))
        return isDiff.getbbox() is not None
    
    def getRandomImage(self):
        images = ["chicken.jpeg", "hamburger.jpeg", "pizza.jpeg", "ricesoup.jpg", "sushi.jpeg"]
        return random.choice(images)
    
    def getRandomReview(self):
        reviews = [
            "비비큐 페리카나 교촌 또래오래 비에이치씨씨",
            "롯데리아 맥도날드 맘스터치 케이에프씨씨",
            "도미노피자 번쩍피자피자피자 얼굴피자",
            "국밥은 콩나물국밥 순대국밥 감자탕 난다조아",
            "초밥은 오마카세가 진리지이요오오오오오오~~"
        ]
        return random.choice(reviews)
    
    def getRandomStar(self):
        stars = [
            ("1", historyLocators.STAR1),
            ("2", historyLocators.STAR2),
            ("3", historyLocators.STAR3),
            ("4", historyLocators.STAR4),
            ("5", historyLocators.STAR5)
        ]

        value, locator = random.choice(stars)
        return value, locator
    
    