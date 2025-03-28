# 작업자 이름: 김다예
 
from selenium.webdriver.common.by import By

# [HOME] 홈 피드 페이지
# 혼자먹기,같이먹기,회식하기 텍스트 포함된 상위 버튼 선택 
HOME_ALONE_BTN = (By.XPATH, "//p[text()='혼자 먹기']/ancestor::button")
HOME_ALONE_BTN = (By.XPATH, "//p[text()='같이 먹기']/ancestor::button")
HOME_ALONE_BTN = (By.XPATH, "//p[text()='혼자 먹기']/ancestor::button")


# [RECOMMEND] 추천 옵션 선택 페이지
# 🔙 뒤로가기 버튼 
RECOMMEND_BACK_BTN = (By.XPATH, "//svg[@class='rounded-full cursor-pointer']")

# 🔺 추천 옵션 선택 텍스트
RECOMMEND_TITLE_TXT = (By.XPATH, "//span[text()='추천 옵션 선택']")

# 🍽 추천 받고자 하는 음식 카테고리 텍스트
RECOMMEND_CATEGORY_TXT = (By.XPATH, "//span[text()='추천 받고자하는 음식 카테고리']")

# 🔽 음식 카테고리 드롭다운 버튼
RECOMMEND_CATEGORY_DROPDOWN = (By.XPATH, "//button[@role='combobox']")
RECOMMEND_OPTION_LABEL = (By.XPATH, "//div[text()='카테고리']")
RECOMMEND_OPTION_KOREAN = (By.XPATH, "//div[@role='option'][.//span[text()='한식']]")
RECOMMEND_OPTION_CHINESE = (By.XPATH, "//div[@role='option'][.//span[text()='중식']]")
RECOMMEND_OPTION_WESTERN = (By.XPATH, "//div[@role='option'][.//span[text()='양식']]")
RECOMMEND_OPTION_JAPANESE = (By.XPATH, "//div[@role='option'][.//span[text()='일식']]")
RECOMMEND_OPTION_SNACK = (By.XPATH, "//div[@role='option'][.//span[text()='분식']]")
RECOMMEND_OPTION_ASIAN = (By.XPATH, "//div[@role='option'][.//span[text()='아시안']]")
RECOMMEND_OPTION_FASTFOOD = (By.XPATH, "//div[@role='option'][.//span[text()='패스트푸드']]")
RECOMMEND_OPTION_ETC = (By.XPATH, "//div[@role='option'][.//span[text()='기타']]")


# 👤 사용자 이름 텍스트
RECOMMEND_MEMBER_NAME_TXT = ()

# 🧑‍💼 부서/팀 정보 텍스트
RECOMMEND_MEMBER_TEAM_TXT = ()

# ✅ 선택 완료 버튼
RECOMMEND_SUBMIT_BTN = (By. XPATH, "//button[text()='선택 완료']")


#








