# 작업자 이름: 채승호

from selenium.webdriver.common.by import By


TEAM_FEED_TAB = (By.CSS_SELECTOR, 'a[href^="/teams/"]')
TEAM_PROFILE_CHANGE = (By.XPATH, "//*[local-name()='svg' and @class='cursor-pointer']")
TEAM_MENU_PLUS = (By.CLASS_NAME, "lucide lucide-plus")
TEAM_SAME_MENU = (By.XPATH, "//button[text()='같은 메뉴 먹기']")
TEAM_BUTTON_DAWN = (By.XPATH, "//button[text()='▼']")
TEXTAREA_LIKE = (By.NAME, "pros")
TEXTAREA_MINUS_ERROR = (By.XPATH, "//p[text()='10자 이상 입력해주세요']")
TEXTAREA_PLUS_ERROR = (By.XPATH, "//p[text()='100자 이내로 입력해주세요']")
TEXTAREA_HATE = (By.NAME, "cons")
CLOSE_BUTTON = (By.CLASS_NAME, "text-2xl.cursor-pointer")
PROFILE_CHANGE_BTN = (By.XPATH, "//button[text()='프로필 수정 완료']")

# 드롭다운 / test_register_002, test_register_019
USERINFO_TEAM_DROP_DOWN = (By.XPATH, "//button[@role='combobox']") # 해당 버튼을 누르면 aria-expanded 속성과 data-state 속성이 변동됨
USERINFO_TEAM_DEV_1 = (By.XPATH, '//*[@id="radix-:r0:"]/div/div/div[2]')
USERINFO_TEAM_DEV_2 = (By.XPATH, '//*[@id="radix-:r0:"]/div/div/div[3]')
USERINFO_TEAM_DESIGN_1 = (By.XPATH, '//*[@id="radix-:r0:"]/div/div/div[4]')
USERINFO_TEAM_DESIGN_2 = (By.XPATH, '//*[@id="radix-:r0:"]/div/div/div[5]')
USERINFO_TEAM_NAME = (By.XPATH, "//span[@style='pointer-events: none;']")
USERINFO_TEAM_ERROR = (By.XPATH, "//p[text()='팀을 선택해주세요']")

# 슬라이더
USERINFO_SLIDER = (By.XPATH, "//span[@role='slider']")
USERINFO_SLIDER_VALUE = (By.CSS_SELECTOR, "span.w-8.text-right.text-gray-500.text-subbody")
USERINFO_SLIDERBAR_ERROR = (By.XPATH, "//p[text()='맛에 대한 성향은 최소 1 이상 설정해주세요']")
