# 작업자 이름: 김다예
 
from selenium.webdriver.common.by import By

# [HOME] 홈 피드 페이지
# 혼자먹기,같이먹기,회식하기 텍스트 포함된 상위 버튼 선택 
HOME_ALONE_BTN = (By.XPATH, "//p[text()='혼자 먹기']/ancestor::button")
HOME_TOGETHER_BTN = (By.XPATH, "//p[text()='같이 먹기']/ancestor::button")
HOME_TEAM_BTN = (By.XPATH, "//p[text()='회식 하기']/ancestor::button")


# [RECOMMEND] 추천 옵션 선택 페이지
# 🔙 뒤로가기 버튼 
RECOMMEND_BACK_BTN = (By.XPATH, "//span[text()='추천 옵션 선택']/preceding-sibling::*[name()='svg']")

# 🔺 추천 옵션 선택 텍스트
RECOMMEND_OPTION_TITLE_TXT = (By.XPATH, "//span[text()='추천 옵션 선택']")

# 🍽 추천 받고자 하는 음식 카테고리 텍스트
RECOMMEND_CATEGORY_TXT = (By.XPATH, "//span[text()='추천 받고자하는 음식 카테고리']")

# 🔽 음식 카테고리 드롭다운 버튼 (선택)
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

# 🔽 음식 카테고리 드롭다운 버튼 (결과확인)
RECOMMEND_OPTION_KOREAN_RESULT = (By.XPATH, "//button[@role='combobox'][.//span[text()='한식']]")
RECOMMEND_OPTION_CHINESE_RESULT = (By.XPATH, "//button[@role='combobox'][.//span[text()='중식']]")
RECOMMEND_OPTION_WESTERN_RESULT = (By.XPATH, "//button[@role='combobox'][.//span[text()='양식']]")
RECOMMEND_OPTION_JAPANESE_RESULT = (By.XPATH, "//button[@role='combobox'][.//span[text()='중식']]")
RECOMMEND_OPTION_SNACK_RESULT = (By.XPATH, "//button[@role='combobox'][.//span[text()='분식']]")
RECOMMEND_OPTION_ASIAN_RESULT = (By.XPATH, "//button[@role='combobox'][.//span[text()='아시안']]")
RECOMMEND_OPTION_FASTFOOD_RESULT = (By.XPATH, "//button[@role='combobox'][.//span[text()='패스트푸드']]")
RECOMMEND_OPTION_ETC_RESULT = (By.XPATH, "//button[@role='combobox'][.//span[text()='기타']]")

# 🙌 먹는 인원 텍스트
RECOMMEND_MEMBER_TITLE_TXT = (By.XPATH, "//span[text()='먹는 인원']")

# 👤 사용자 이름 - 상단 <span>태그 / 혼자먹기
RECOMMEND_MEMBER_UP = (By.XPATH, "//span[text()='다예']") # 텍스트 값 수정필요

# 👤 사용자 이름 - 하단 <div>태그 / 혼자먹기
RECOMMEND_MEMBER_DOWN = (By.XPATH, "//div[text()='다예']") # 텍스트 값 수정필요

# 👤 부서/팀 정보 텍스트 / 혼자먹기
RECOMMEND_TEAM_TXT = (By.XPATH, "//div[text()='디자인 1팀']") # 텍스트 값 수정필요

# 👤👤 이름 인풋 박스 / 같이먹기
RECOMMEND_SEARCH_NAME = (By.XPATH, "//input[@placeholder='이름을 검색해주세요']")

# 👤👤 이름 인풋 박스(텍스트 입력) / 같이먹기
RECOMMEND_SEARCH_INPUT = (By.CSS_SELECTOR, "ul.flex.flex-col > li")

# 👤👤 이름 인풋 박스(결과 선택 단계) / 같이먹기
RECOMMEND_SEARCH_RESULT = (By. CSS_SELECTOR, "ul > li.cursor-pointer")

# 👤👤 이름 인풋 박스(결과 추가, "x" 아이콘) / 같이먹기
# RECOMMEND_SEARCH_SELECTED = (By.CSS_SELECTOR, "svg.absolute.top-0.cursor-pointer.-right-2")
RECOMMEND_SEARCH_SELECTED = (By.XPATH, "//span[text()='먹는 인원']/following-sibling::div[1]//svg/path")

# 👤👤 이름 리스트 / 같이먹기
RECOMMEND_MEMBER_LIST = (By.XPATH, "//div[@class='font-semibold' and text()='정준하']")

# 👤👤 부서/팀 리스트 / 같이먹기
RECOMMEND_TEAM_LIST = (By.XPATH, "//div[@class=text-gray-500' and text()='개발 1팀']")

# 👤👤 리스트 체크박스/ 같이먹기
RECOMMEND_CHECKBOX_LIST = (By.XPATH, "//div[@class=cursor-pointer]")

# 👤👤👤 부서/팀 정보 뱃지 / 회식하기
RECOMMEND_TEAM_BADGE = (By.XPATH, "//span[text()='디자인 1팀']") # 텍스트 값 수정필요

# ✅ [선택 완료] 버튼
RECOMMEND_SUBMIT_BTN = (By. XPATH, "//button[text()='선택 완료']")


# [RESULT] 메뉴추천 페이지
# 🔺 메뉴추천 텍스트 (헤더바 안에 있는 "메뉴 추천")
RESULT_HEADER_TITLE = (By.XPATH, "//span[text()='메뉴 추천']")

# 🔺 "오늘 메뉴는 찜닭 어떠세요?" 텍스트
RESULT_MENU_TITLE = (By.XPATH, "//span[contains(text(), '오늘 메뉴는')]")

# 🖼️ 찜닭 이미지
RESULT_MENU_IMAGE = (By.XPATH, "//img[@alt='음식 사진']")

# 🧠 "AI가 분석한 취향 적합률" 텍스트
RESULT_AI_MATCH_TXT = (By.XPATH, "//div[span[contains(text(), 'AI가 분석한')]]")

# 🧠 "AI가 분석한 취향 적합률" 퍼센트
RESULT_AI_MATCH_PERCENT = (By.XPATH, "//div[span[contains(text(), '%')]]")

# 🍽️ "찜닭에 해당하는 맛집 리스트" 텍스트
RESULT_RECOMMENDED_RESTAURANT = (By.XPATH, "//span[contain(text(), '에 해당하는 맛집 리스트')]")

# 🏠 맛집 리스트 전체 (슬라이드/카드 리스트 영역)
RESULT_RESTAURANT_LIST = (By.CSS_SELECTOR, "div.swiper-slide a")

# 🏠 맛집 리스트 (첫 번째 카드)
RESULT_RESTAURANT_FIRST = (By.CSS_SELECTOR, "div.swiper-slide-active a")

# 📱 페이지네이션 (첫 번째 점)
RESULT_RESTAURANT_CAROUSEL_FIRST = (By.CSS_SELECTOR, "span.swiper-pagination-bullet:nth-child(1)")

# 📱 페이지네이션 (두 번째 점)
RESULT_RESTAURANT_CAROUSEL_SECOND = (By.CSS_SELECTOR, "span.swiper-pagination-bullet:nth-child(2)")

# 📱 페이지네이션 (현재 활성화된 점)
RESULT_RESTAURANT_CAROUSEL_ACTIVE = (By.CSS_SELECTOR, "span.swiper-pagination-bullet-active")

# 검색 결과가 없습니다
RESULT_NO_RESTAURANT = (By.XPATH, "//h1[contains(text(), '검색 결과가 없습니다')]")

# 🔁 다시 추천받기 버튼 (초록색)
RESULT_RETRY_BTN = (By.XPATH, "//button[text()='다시 추천 받기']")

# ✅ 추천 수락하기 버튼 (빨간색)
RESULT_ACCEPT_BTN = (By.XPATH, "//button[text()='추천 수락하기']")

# ✅ 추천 수락하기 버튼 결과 페이지 > 히스토리 탭 
RESULT_ACCEPT_BTN_AFTER = (By.XPATH, "//span[contains(text(), '추천 받았던 메뉴들이에요')]")