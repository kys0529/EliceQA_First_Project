# 작업자 이름: 강연수

from selenium.webdriver.common.by import By

MY_FEED_TAB = (By.XPATH, "//a[@href='/my']")

MY_PROFILE_CHANGE_SVG = (By.XPATH, "//*[name()='svg' and @class='cursor-pointer']")
MY_MENU_PLUS_BTN = (By.XPATH, "//span[contains(text(), '내가 먹은 메뉴')]/following-sibling::button")
MY_EAT_SAME_MENU_BTN = (By.XPATH, "//span[contains(text(), '내가 먹은 메뉴')]/../following-sibling::div//button[text()='같은 메뉴 먹기']") # 제일 상단에 위치한 [같은 메뉴 먹기] 버튼

MY_FEED_TXT = (By.XPATH, "//span[text()='내 피드']")