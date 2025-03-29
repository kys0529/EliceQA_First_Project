# 작업자 이름: 강연수

from selenium.webdriver.common.by import By

# /.. : 해당 요소의 부모
# /preceding-sibling : 해당 요소의 같은 부모 아래, 앞에 있는 형제
# /following-sibling : 해당 요소의 같은 부모 아래, 뒤에 있는 형제

# 홈 요소
HOME_TXT = (By.XPATH, "//span[text()='오늘 뭐먹지 ?']")

# 개인 피드 요소
MY_FEED_TAB = (By.XPATH, "//a[@href='/my']")
MY_FEED_BACK_PAGE = (By.XPATH, "//span[text()='내 피드']/preceding-sibling::*[name()='svg']")

MY_PROFILE_CHANGE_SVG = (By.XPATH, "//*[name()='svg' and @class='cursor-pointer']")
MY_PROFILE_CHANGE_CANCEL_SVG = (By.XPATH, "//span[contains(text(), '프로필 정보 수정')]/following-sibling::button")

MY_MENU_PLUS_BTN = (By.XPATH, "//span[contains(text(), '내가 먹은 메뉴')]/following-sibling::button")
MY_EAT_SAME_MENU_BTN = (By.XPATH, "//span[contains(text(), '내가 먹은 메뉴')]/../following-sibling::div//button[text()='같은 메뉴 먹기']") # 제일 상단에 위치한 [같은 메뉴 먹기] 버튼

MY_FEED_TXT = (By.XPATH, "//span[text()='내 피드']")