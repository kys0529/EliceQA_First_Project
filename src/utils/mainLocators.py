# 작업자 이름: 5조 / 마무리 연수
 
from selenium.webdriver.common.by import By

# 메인 페이지 요소
LOGIN_BTN = (By.XPATH, "//button[text()='로그인하기']")
REGISTER_BTN = (By.XPATH, "//button[text()='회원가입']")

# 메인 -> 로그인하기 / test_register_022, test_register_023, test_register_020, test_register_024
ID_INPUT = (By.ID, "username")
PW_INPUT = (By.ID, "password")
PW_TOGGLE_BTN = (By.XPATH, "//button[@data-action='toggle']") #속성은 @로 찾기

PW_RESET = (By.XPATH, "//a[text()='비밀번호를 잊으셨나요?']")
RESET_GOING_BUTTON = (By.XPATH, "//button[text()='계속']")
PW_FORGET = (By.TAG_NAME, "h1") # 비밀번호를 잊으셨나요 문구

PW_BACK_LOGIN = (By.XPATH, "//button[text()='로그인 화면으로 돌아가기']") # 로그인 화면으로 돌아가기

GOING_BTN = (By.XPATH, "//button[text()='계속하기']") #텍스트는 @생략

# 마스킹 - 토글토글토글 / test_register_005, test_register_025
PW_TOGGLE_BTN = (By.XPATH, "//button[@data-action='toggle']") #속성은 @로 찾기

# 초기 진입 페이지 / test_register_001, test_register_027 
REGISTER_HREF = (By.XPATH, "//a[text()='회원가입']")

# 하이퍼링크 / test_register_002, test_register_020
LOGIN_HREF = (By.XPATH, "//a[text()='로그인']")
REGISTER_HREF = (By.XPATH, "//a[text()='회원가입']")

MAIN_TXT = (By.XPATH, "//p[text()='오늘의 식사 메뉴를 추천해드립니다']")
LOGIN_TXT = (By.XPATH, "//p[text()='맛있는 선택은 당신의 하루를 바꿉니다.']")
REGISTER_TXT = (By.XPATH, "//p[text()='오늘 뭐 먹지? 를 사용하시려면 회원가입을 진행해주세요.']")

# 올바른 입력값 / test_register_003, test_register_026, test_register_029, test_register_030
REGISTER_EMAIL = (By.ID, "email")
REGISTER_PW = (By.ID, "password")

# 유효성 검사 / test_register_004
PW_UNDER_8 = (By.XPATH, "//li[@data-error-code='password-policy-length-at-least']")
PW_VALID_3 = (By.XPATH, "//li[@data-error-code='password-policy-contains-at-least']")
PW_LOWER_LETTERS = (By.XPATH, "//li[@data-error-code='password-policy-lower-case']")
PW_UPPER_LETTERS = (By.XPATH, "//li[@data-error-code='password-policy-upper-case']")
PW_NUMBER = (By.XPATH, "//li[@data-error-code='password-policy-numbers']")
PW_SPECIAL_CHARACTERS = (By.XPATH, "//li[@data-error-code='password-policy-special-characters']")

# 앱 승인 접근 화면 / test_register_003, test_register_006
AUTH_TXT = (By.XPATH, "//h1[text()='Authorize App']")
ACCEPT_BTN = (By.XPATH, "//button[text()='Accept']")
DECLINE_BTN = (By.XPATH, "//button[text()='Decline']")
                 
# 회원가입 승인 / test_register_007
ACCEPT_BTN = (By.XPATH, "//button[text()='Accept']") #중복

# 회원가입 거절 / test_register_008
DECLINE_BTN = (By.XPATH, "//button[text()='Decline']") #중복

# 회원가입 거절 후 다음 페이지 / test_register_009
RETRY_BTN = (By.XPATH, "//button[text()='다시 시도하기']")



# 이메일 주소 (수신함) / test_register_032
RESEND_EMAIL_BTN = (By.XPATH, "//button[text()='Resend email']")
EMAIL_TXT = (By.XPATH, "//p[text()='이메일 주소를 입력하면 비밀번호 재설정 지침을 보내드립니다.']")

# 오늘 뭐 먹지 개인정보 페이지 test_register_011 , test_register_015, test_register_019
# test_register_012
NAME_INPUT = (By.NAME, "name")
SUBMIT_BTN = (By.XPATH, "//button[text()='제출하기']") # @중복
NAME_ERROR = (By.XPATH, "//p[text()='이름을 입력해주세요']")



# 드롭다운 / test_register_014, test_register_019
DROP_DOWN = (By.XPATH, "//button[@role='combobox']")
DROP_OPTION_DEV_1 = (By.XPATH, "//div[normalize-space(text())='개발 1팀']")
DROP_OPTION_DEV_2 = (By.XPATH, "//div[normalize-space(text())='개발 2팀']")
DROP_OPTION_DESIGN_1 = (By.XPATH, "//div[normalize-space(text())='디자인 1팀']")
DROP_OPTION_DESIGN_2 = (By.XPATH, "//div[normalize-space(text())='디자인 2팀']")
SUBMIT_BTN = (By.XPATH, "//button[text()='제출하기']") #@중복
TEAM_SELECT_ERROR = (By.XPATH, "//p[text()='팀을 선택해주세요']")

# 음식성향(슬라이드바) / test_register_016 , test_register_019
SWEET_SLIDERBAR = (By.XPATH, "//span[text()='단 맛']/ancestor::section//span[contains(@class, 'bg-light-gray')]")
SALTY_SLIDERBAR = (By.XPATH, "//span[text()='짠 맛']/ancestor::section//span[contains(@class, 'bg-light-gray')]")
SPICY_SLIDERBAR = (By.XPATH, "//span[text()='매운 맛']/ancestor::section//span[contains(@class, 'bg-light-gray')]")
SUBMIT_BTN = (By.XPATH, "//button[text()='제출하기']") #@중복
BAR_UNDER_1 = (By.XPATH, "//p[text()='맛에 대한 성향은 최소 1 이상 설정해주세요']")

# 음식성향(텍스트) / test_register_017, test_register_018, test_register_019
TEXTAREA_LIKE = (By.NAME, "pros")
TEXTAREA_HATE = (By.NAME, "cons")
SUBMIT_BTN = (By.XPATH, "//button[text()='제출하기']") #@원본
TEXT_UNDER_10 = (By.XPATH, "//p[text()='10자 이상 입력해주세요']") 





