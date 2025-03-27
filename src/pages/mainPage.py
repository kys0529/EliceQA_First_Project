# 작업자 이름: 5조 / 마무리 연수

# Page Object 클래스 (UI 요소 및 메서드 정의)

import json
import time
from faker import Faker
from PIL import Image, ImageChops
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utils import mainLocators
from src.utils.logger import setupLogger

class mainPage():
    URL = "https://kdt-pt-1-pj-2-team03.elicecoding.com/signin"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = setupLogger("mainPage")

        with open("credentials.json", "r", encoding="utf-8") as f: # 나중에 auth.json 파일 이름을 credentials.json으로 변경해주기
            self.userInfo = json.load(f)

    def goToPage(self, depth2):
        if (depth2 == "메인 페이지"):
            self.driver.get(self.URL)
        elif (depth2 == "회원가입 페이지"):
            self.driver.get(self.URL)
            self.getElement(mainLocators.REGISTER_BTN).click()
        elif (depth2 == "앱 인증 권한"):
            self.driver.get(self.URL)
            self.getElement(mainLocators.REGISTER_BTN).click()
            email, pw = self.getRandomAccount()
            self.getElement(mainLocators.REGISTER_EMAIL).send_keys(email)
            self.getElement(mainLocators.REGISTER_PW).send_keys(pw)
            self.getElement(mainLocators.RE_GOING_BTN).click()
        elif (depth2 == "로그인 오류 페이지"):
            pass # 이건 나중에
        elif (depth2 == "인적사항 작성 페이지"):
            self.driver.get(self.URL)
            self.getElement(mainLocators.REGISTER_BTN).click()
            email, pw = self.getRandomAccount()
            self.getElement(mainLocators.REGISTER_EMAIL).send_keys(email)
            self.getElement(mainLocators.REGISTER_PW).send_keys(pw)
            self.getElement(mainLocators.RE_GOING_BTN).click()
            self.getElement(mainLocators.ACCEPT_BTN).click()
        elif (depth2 == "로그인 페이지"):
            self.driver.get(self.URL)
            self.getElement(mainLocators.LOGIN_BTN).click()
        elif (depth2 == "비밀번호 재설정 페이지"):
            self.driver.get(self.URL)
            self.getElement(mainLocators.LOGIN_BTN).click()
            self.getElement(mainLocators.PW_RESET).click()

    def getElement(self, element):
        result = self.wait.until(EC.presence_of_element_located(element))
        return result
    
    def getRandomAccount(self):
        faker = Faker()
        return faker.email(), faker.password(length=8)
    
    def screenDiff(self, locator, funcName, imageName, action, msg=""):
        time.sleep(2)
        self.driver.save_screenshot(f"reports/screenshots/{funcName}_{imageName}_before.png")
        
        if (action == "click"):
            self.getElement(locator).click()
        elif (action == "send"):
            self.getElement(locator).send_keys(msg)

        time.sleep(2)
        self.driver.save_screenshot(f"reports/screenshots/{funcName}_{imageName}_after.png")

        isDiff =  ImageChops.difference(Image.open(f"reports/screenshots/{funcName}_{imageName}_before.png"), Image.open(f"reports/screenshots/{funcName}_{imageName}_after.png"))
        return isDiff.getbbox() is not None