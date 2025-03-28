# 작업자 이름: 채승호

from selenium.webdriver.common.by import By


TEAM_FEED_TAB = (By.XPATH, "//a[@href='/teams/1']")
TEAM_PROFILE_CHANGE = (By.XPATH, "//div[@class='cursor-pointer']")
TEAM_MENU_PLUS = (By.CLASS_NAME, "lucide lucide-plus")
TEAM_SAME_MENU = (By.XPATH, "//button[text()='같은 메뉴 먹기']")
TEAM_BUTTON_DAWN = (By.XPATH, "//button[text()='▼']")

# 드롭다운 / test_register_002, test_register_019
DROP_DOWN = (By.XPATH, "//button[@role='combobox']")
DROP_OPTION_DEV_1 = (By.XPATH, "//div[normalize-space(text())='개발 1팀']")
DROP_OPTION_DEV_2 = (By.XPATH, "//div[normalize-space(text())='개발 2팀']")
DROP_OPTION_DESIGN_1 = (By.XPATH, "//div[normalize-space(text())='디자인 1팀']")
DROP_OPTION_DESIGN_2 = (By.XPATH, "//div[normalize-space(text())='디자인 2팀']")
