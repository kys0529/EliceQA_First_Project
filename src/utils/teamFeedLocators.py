# 작업자 이름: 채승호

from selenium.webdriver.common.by import By


TEAM_FEED_TAB = (By.XPATH, "//a[@href='/teams/1']")
TEAM_PROFILE_CHANGE = (By.XPATH, "//*[local-name()='svg' and @class='cursor-pointer']")
TEAM_MENU_PLUS = (By.CLASS_NAME, "lucide lucide-plus")
TEAM_SAME_MENU = (By.XPATH, "//button[text()='같은 메뉴 먹기']")
TEAM_BUTTON_DAWN = (By.XPATH, "//button[text()='▼']")
TEXTAREA_LIKE = (By.NAME, "pros")
TEXTAREA_HATE = (By.NAME, "cons")
CLOSE_BUTTON = (By.CLASS_NAME, "text-2xl.cursor-pointer")
PROFILE_CHANGE_BTN = (By.XPATH, "//button[text()='프로필 수정 완료']")

# 드롭다운 / test_register_002, test_register_019
DROP_DOWN = (By.XPATH, "//button[@role='combobox']")
DROP_OPTION_DEV_1 = (By.XPATH, "//div[normalize-space(text())='개발 1팀']")
DROP_OPTION_DEV_2 = (By.XPATH, "//div[normalize-space(text())='개발 2팀']")
DROP_OPTION_DESIGN_1 = (By.XPATH, "//div[normalize-space(text())='디자인 1팀']")
DROP_OPTION_DESIGN_2 = (By.XPATH, "//div[normalize-space(text())='디자인 2팀']")
