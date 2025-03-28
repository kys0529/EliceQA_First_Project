# 작업자 이름: 5조 / 마무리 연수
 
from selenium.webdriver.common.by import By

# 메인 페이지 요소
MAINP_LOGIN_BTN = (By.XPATH, "//button[text()='로그인하기']")
MAINP_REGISTER_BTN = (By.XPATH, "//button[text()='회원가입']")

MAINP_TXT = (By.XPATH, "//p[text()='오늘의 식사 메뉴를 추천해드립니다']")

# 로그인 페이지 요소 (메인 페이지 -> [로그인하기] 버튼 클릭)
# 메인 페이지에서 [로그인하기] 버튼 클릭 / test_register_022, test_register_023, test_register_020, test_register_024
LOGINP_EMAIL_INPUT = (By.ID, "username")
LOGINP_PW_INPUT = (By.ID, "password")
LOGINP_PW_TOGGLE_BTN = (By.XPATH, "//button[@data-action='toggle']") # 해당 버튼을 누르면 LOGINP_PW_INPUT type 속성이 변동됨
LOGINP_PW_RESET_HREF = (By.XPATH, "//a[text()='비밀번호를 잊으셨나요?']")
LOGINP_GOING_BTN = (By.XPATH, "//button[text()='계속하기']")
LOGINP_REGISTER_HREF = (By.XPATH, "//a[text()='회원가입']")

LOGINP_LOGIN_ERROR_TXT = (By.ID, "error-element-password")
LOGINP_TXT = (By.XPATH, "//p[text()='맛있는 선택은 당신의 하루를 바꿉니다.']")

# 회원가입 페이지 요소 (메인 페이지 -> [회원가입] 버튼 클릭)
REGP_EMAIL_INPUT = (By.ID, "email")
REGP_PW_INPUT = (By.ID, "password")
REGP_PW_TOGGLE_BTN = (By.XPATH, "//button[@data-action='toggle']") # 해당 버튼을 누르면 REGP_PW_INPUT type 속성이 변동됨
REGP_GOING_BTN = (By.XPATH, "//button[text()='계속하기']")
REGP_LOGIN_HREF = (By.XPATH, "//a[text()='로그인']")

REGP_PW_LEAST_8 = (By.XPATH, "//li[@data-error-code='password-policy-length-at-least']")
REGP_PW_VALID_3 = (By.XPATH, "//li[@data-error-code='password-policy-contains-at-least']")
REGP_PW_LOWER_LETTERS = (By.XPATH, "//li[@data-error-code='password-policy-lower-case']")
REGP_PW_UPPER_LETTERS = (By.XPATH, "//li[@data-error-code='password-policy-upper-case']")
REGP_PW_NUMBER = (By.XPATH, "//li[@data-error-code='password-policy-numbers']")
REGP_PW_SPECIAL_CHARACTERS = (By.XPATH, "//li[@data-error-code='password-policy-special-characters']")

REGP_EMAIL_ERROR_TXT = (By.ID, "error-element-email")
REGP_TXT = (By.XPATH, "//p[text()='오늘 뭐 먹지? 를 사용하시려면 회원가입을 진행해주세요.']")

# 비밀번호 재설정 페이지 (로그인 페이지 -> "비밀번호를 잊으셨나요?" 하이퍼링크 클릭)
RESET_EMAIL_INPUT = (By.ID, "email")
RESET_GOING_BTN = (By.XPATH, "//button[text()='계속']")
RESET_BACK_LOGIN_BTN = (By.XPATH, "//button[text()='로그인 화면으로 돌아가기']") # 로그인 화면으로 돌아가기

RESET_TXT = (By.XPATH, "//p[text()='이메일 주소를 입력하면 비밀번호 재설정 지침을 보내드립니다.']")

# 메일 확인 안내 페이지 (비밀번호 재설정 페이지 -> '이메일 주소' 필드 입력 후 [계속] 버튼 클릭)
MAIL_RESEND_EMAIL_BTN = (By.XPATH, "//button[text()='Resend email']") # 해당 버튼을 누르면 비밀번호 재설정 페이지로 돌아감 

MAIL_TXT = (By.XPATH, "//h1[text()='Check Your Email']")

# 앱 인증권한 페이지
AUTH_ACCEPT_BTN = (By.XPATH, "//button[text()='Accept']")
AUTH_DECLINE_BTN = (By.XPATH, "//button[text()='Decline']")

AUTH_TXT = (By.XPATH, "//h1[text()='Authorize App']")

# 로그인 오류페이지 (앱 인증권한 페이지 -> [Decline] 버튼 클릭)
ERROR_RETRY = (By.XPATH, "//button[text()='다시 시도하기']") # 해당 버튼을 누르면 메인 페이지로 돌아감

ERROR_TXT = (By.XPATH, "//h2[text()='로그인 오류']")

# 인적사항 작성 페이지
USERINFO_NAME_INPUT = (By.XPATH, "//input[@placeholder='이름을 입력해주세요']")
USERINFO_NAME_ERROR = (By.XPATH, "//p[text()='이름을 입력해주세요']")

USERINFO_TEAM_DROP_DOWN = (By.XPATH, "//button[@role='combobox']") # 해당 버튼을 누르면 aria-expanded 속성과 data-state 속성이 다름 
USERINFO_TEAM_DEV_1 = (By.XPATH, "//div[normalize-space(text())='개발 1팀']")
USERINFO_TEAM_DEV_2 = (By.XPATH, "//div[normalize-space(text())='개발 2팀']")
USERINFO_TEAM_DESIGN_1 = (By.XPATH, "//div[normalize-space(text())='디자인 1팀']")
USERINFO_TEAM_DESIGN_2 = (By.XPATH, "//div[normalize-space(text())='디자인 2팀']")
USERINFO_TEAM_ERROR = (By.XPATH, "//p[text()='팀을 선택해주세요']")

# # 음식성향(슬라이드바) / test_register_016 , test_register_019
# SWEET_SLIDERBAR = (By.XPATH, "//span[text()='단 맛']/ancestor::section//span[contains(@class, 'bg-light-gray')]")
# SALTY_SLIDERBAR = (By.XPATH, "//span[text()='짠 맛']/ancestor::section//span[contains(@class, 'bg-light-gray')]")
# SPICY_SLIDERBAR = (By.XPATH, "//span[text()='매운 맛']/ancestor::section//span[contains(@class, 'bg-light-gray')]")
# BAR_UNDER_1 = (By.XPATH, "//p[text()='맛에 대한 성향은 최소 1 이상 설정해주세요']")

# # 음식성향(텍스트) / test_register_017, test_register_018, test_register_019
# TEXTAREA_LIKE = (By.NAME, "pros")
# TEXTAREA_HATE = (By.NAME, "cons")
# SUBMIT_BTN = (By.XPATH, "//button[text()='제출하기']") #@원본
# TEXT_UNDER_10 = (By.XPATH, "//p[text()='10자 이상 입력해주세요']")

USERINFO_SUBMIT_BTN = (By.XPATH, "//button[text()='제출하기']")

USERINFO_TXT = (By.XPATH, "//span[text()='🔥 서비스 이용을 위해 인적사항을 작성해주세요']")