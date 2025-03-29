# 작업자 이름: 강연수

import os
import json
import time
from PIL import Image, ImageChops
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from src.utils import myFeedLocators
from src.utils.helpers import autoLogin
from src.utils.logger import setupLogger

class myFeed():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = setupLogger("myFeed")
        self.action = ActionChains(driver)

        with open("credentials.json", "r", encoding="utf-8") as f: # 나중에 auth.json 파일 이름을 credentials.json으로 변경해주기
            self.userInfo = json.load(f)

        autoLogin(self.driver, self.wait, self.userInfo)

    def goToPage(self, depth2):
        if (depth2 == "개인 피드"):
            self.getElement(myFeedLocators.MY_FEED_TAB).click()
        elif (depth2 == "프로필 수정"):
            self.getElement(myFeedLocators.MY_FEED_TAB).click()
            self.getElement(myFeedLocators.MY_PROFILE_CHANGE_SVG).click()
        elif (depth2 == "[+] 버튼"):
            self.getElement(myFeedLocators.MY_FEED_TAB).click()
            self.scroll(500)
            self.getElement(myFeedLocators.MY_MENU_PLUS_BTN).click()
        elif (depth2 == "같은 메뉴 먹기"):
            self.getElement(myFeedLocators.MY_FEED_TAB).click()
            self.scroll(500)
            self.getElement(myFeedLocators.MY_EAT_SAME_MENU_BTN).click()

    def getElement(self, element):
        return self.wait.until(EC.presence_of_element_located(element))

    def getElements(self, element):
        return self.wait.until(EC.presence_of_all_elements_located(element))
    
    def getVisibilityElement(self, element):
        return self.wait.until(EC.visibility_of_element_located(element))
    
    def scroll(self, num):
        time.sleep(1)
        self.driver.execute_script(f"window.scrollTo(0, {num});")
        time.sleep(1)

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