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
        self.faker = Faker()

        with open("credentials.json", "r", encoding="utf-8") as f:
            self.userInfo = json.load(f)

    def goToPage(self, depth2):
        email, pw = self.getRandomAccount()

        if (depth2 == "메인 페이지"):
            self.driver.get(self.URL)
        elif (depth2 == "로그인 페이지"):
            self.driver.get(self.URL)
            self.getElement(mainLocators.MAINP_LOGIN_BTN).click()
        elif (depth2 == "회원가입 페이지"):
            self.driver.get(self.URL)
            self.getElement(mainLocators.MAINP_REGISTER_BTN).click()
        elif (depth2 == "앱 인증 권한"):
            self.driver.get(self.URL)
            self.getElement(mainLocators.MAINP_REGISTER_BTN).click()
            self.getElement(mainLocators.REGP_EMAIL_INPUT).send_keys(email)
            self.getElement(mainLocators.REGP_PW_INPUT).send_keys(pw)
            self.getElement(mainLocators.REGP_GOING_BTN).click()
        elif (depth2 == "인적사항 작성 페이지"):
            self.driver.get(self.URL)
            self.getElement(mainLocators.MAINP_REGISTER_BTN).click()
            self.getElement(mainLocators.REGP_EMAIL_INPUT).send_keys(email)
            self.getElement(mainLocators.REGP_PW_INPUT).send_keys(pw)
            self.getElement(mainLocators.REGP_GOING_BTN).click()
            self.getElement(mainLocators.AUTH_ACCEPT_BTN).click()
        elif (depth2 == "비밀번호 재설정 페이지"):
            self.driver.get(self.URL)
            self.getElement(mainLocators.MAINP_LOGIN_BTN).click()
            self.getElement(mainLocators.LOGINP_PW_RESET_HREF).click()
        elif (depth2 == "메일 확인 안내 페이지"):
            self.driver.get(self.URL)
            self.getElement(mainLocators.MAINP_LOGIN_BTN).click()
            self.getElement(mainLocators.LOGINP_PW_RESET_HREF).click()
            self.getElement(mainLocators.RESET_EMAIL_INPUT).send_keys(email)
            self.getElement(mainLocators.RESET_GOING_BTN).click()
        elif (depth2 == "로그인 오류 페이지"):
            self.driver.get(self.URL)
            self.getElement(mainLocators.MAINP_REGISTER_BTN).click()
            self.getElement(mainLocators.REGP_EMAIL_INPUT).send_keys(email)
            self.getElement(mainLocators.REGP_PW_INPUT).send_keys(pw)
            self.getElement(mainLocators.REGP_GOING_BTN).click()
            self.getElement(mainLocators.AUTH_DECLINE_BTN).click()

    def getElement(self, element):
        return self.wait.until(EC.presence_of_element_located(element))

    def getElements(self, element):
        return self.wait.until(EC.presence_of_all_elements_located(element))
    
    def getRandomAccount(self):
        return self.faker.email(), self.faker.password(length=8)

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