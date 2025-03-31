# 작업자 이름: @@@

import json
import os
import time
import random

from faker import Faker
from PIL import Image, ImageChops
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from src.utils import teamFeedLocators
from src.utils.helpers import autoLogin
from src.utils.logger import setupLogger

class teamFeed():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = setupLogger("teamFeed")
        self.action = ActionChains(driver)
        
        with open("credentials.json", "r", encoding="utf-8") as f: # 나중에 auth.json 파일 이름을 credentials.json으로 변경해주기
            self.userInfo = json.load(f)

        autoLogin(self.driver, self.wait, self.userInfo)
        
    def scroll(self, num):
        time.sleep(1)
        self.driver.execute_script(f"window.scrollTo(0, {num});")
        time.sleep(1)
        
            
    def getElement(self, element):
        result = self.wait.until(EC.presence_of_element_located(element))
        return result
    
    def goToPage(self, depth):
        if depth == "팀 피드":
            self.getElement(teamFeedLocators.TEAM_FEED_TAB).click()
            
        elif (depth == "[+] 버튼"):
            self.getElement(teamFeedLocators.TEAM_FEED_TAB).click()
            self.action.send_keys(Keys.PAGE_DOWN).perform()
            self.getElement(teamFeedLocators.TEAM_MENU_PLUS_BTN).click()
        elif (depth == "같은 메뉴 먹기"):
            self.getElement(teamFeedLocators.TEAM_FEED_TAB).click()
            self.action.send_keys(Keys.PAGE_DOWN).perform()
            self.getElement(teamFeedLocators.TEAM_SAME_MENU_BTN).click()
            
    def pageDown(self, depth):
        if depth == "page down":
            self.getElement(teamFeedLocators.TEAM_FEED_TAB).click()
            self.action.send_keys(Keys.PAGE_DOWN).perform()
        
        
    def getElements(self, element):
        return self.wait.until(EC.presence_of_all_elements_located(element))
    
    def getVisibilityElement(self, element):
        return self.wait.until(EC.visibility_of_element_located(element))
    
    def getClickableElement(self, element):
        return self.wait.until(EC.element_to_be_clickable(element))
    
    def scrollElement(self):
        while True:

            self.driver.execute_script("window.scrollBy(0, 500);")  # 500픽셀씩 아래로 스크롤
            time.sleep(1)  # 스크롤 후 대기

            try:
            
                self.getElement(teamFeedLocators.TEAM_BUTTON_DOWN).click()
                break  # 요소를 찾으면 반복 종료
            
            except:
                pass  # 요소가 없으면 스크롤 계속
    

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

    def getRandomMenuName(self):
        menus = ["치킨", "햄버거", "피자", "국밥", "초밥"]
        return random.choice(menus)

    def getRandomCategory(self):
        categories = [
            ("한식", teamFeedLocators.RECOMMEND_OPTION_KOREAN),
            ("중식", teamFeedLocators.RECOMMEND_OPTION_CHINESE),
            ("양식", teamFeedLocators.RECOMMEND_OPTION_WESTERN),
            ("일식", teamFeedLocators.RECOMMEND_OPTION_JAPANESE),
            ("분식", teamFeedLocators.RECOMMEND_OPTION_SNACK),
            ("아시안", teamFeedLocators.RECOMMEND_OPTION_ASIAN),
            ("패스트푸드", teamFeedLocators.RECOMMEND_OPTION_FASTFOOD),
            ("기타", teamFeedLocators.RECOMMEND_OPTION_ETC)
        ]
    
        name, locator = random.choice(categories)
        return name, locator
        
    def getRandomReview(self):
        reviews = [
            "치킨 냠냠 바삭바삭 존맛탱~~",
            "햄버거 냠냠 존맛탱~~",
            "피자 토핑 대박 풍족~~",
            "국밥 국물 대박 얼큰~~",
            "초밥 냠냠 완전 존맛탱~~"
        ]
        return random.choice(reviews)

    def getRandomStar(self):
        stars = [
            ("1", teamFeedLocators.MY_MENU_STAR1),
            ("2", teamFeedLocators.MY_MENU_STAR2),
            ("3", teamFeedLocators.MY_MENU_STAR3),
            ("4", teamFeedLocators.MY_MENU_STAR4),
            ("5", teamFeedLocators.MY_MENU_STAR5)
        ]

        value, locator = random.choice(stars)
        return value, locator

    def getReviewPostCount(self):
        prevCount = -1

        while True:
            currentElements = self.getElements(teamFeedLocators.TEAM_MENU_PLUS_REVIEW_POST)
            currentCount = len(currentElements)

            if currentCount == prevCount:
                break

            prevCount = currentCount
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        return prevCount