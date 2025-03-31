# 작업자 이름: 채승호

from selenium.webdriver.common.by import By


TEAM_FEED_TAB = (By.CSS_SELECTOR, 'a[href^="/teams/"]')
TEAM_FEED_BACK_BTN = (By.XPATH, "//*[local-name()='svg' and @class='rounded-full cursor-pointer']")
TEAM_PROFILE_CHANGE = (By.XPATH, "//*[local-name()='svg' and @class='cursor-pointer']")
TEAM_SAME_MENU = (By.XPATH, "//button[text()='같은 메뉴 먹기']")
TEAM_BUTTON_UP = (By.XPATH, "//p[@class='pr-3 text-description']")

TEAM_BUTTON_DOWN = (By.XPATH, "//p[@class='pr-3 text-description line-clamp-1']")

TEXTAREA_LIKE = (By.NAME, "pros")
TEAM_FEED_TXT = (By.XPATH, "//p[text()='다른 팀은 어떤 메뉴를 먹었을까요?']")
TEXTAREA_MINUS_ERROR = (By.XPATH, "//p[text()='10자 이상 입력해주세요']")
TEXTAREA_PLUS_ERROR = (By.XPATH, "//p[text()='100자 이내로 입력해주세요']")
TEXTAREA_HATE = (By.NAME, "cons")
CLOSE_BUTTON = (By.CLASS_NAME, "text-2xl.cursor-pointer")
PROFILE_CHANGE_BTN = (By.XPATH, "//button[text()='프로필 수정 완료']")
TEAM_MENU_PLUS_BTN = (By.XPATH, "//span[contains(text(), '팀이 먹은 메뉴')]/following-sibling::button")
TEAM_SAME_MENU_BTN = (By.XPATH, "//span[contains(text(), '팀이 먹은 메뉴')]/../following-sibling::div//button[text()='같은 메뉴 먹기']") # 제일 상단에 위치한 [같은 메뉴 먹기] 버튼

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


# 🔽 음식 카테고리 드롭다운 버튼 (선택)
RECOMMEND_CATEGORY_DROPDOWN = (By.XPATH, "//h1[text()='카테고리']/following::button[1]")
RECOMMEND_OPTION_LABEL = (By.XPATH, "//h1[text()='카테고리']/following-sibling::button//span")
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


# 새로운 후기 등록하기
TEAM_PLUS_CANCEL_BTN = (By.XPATH, "//span[text()='새로운 후기 등록하기']/following-sibling::button/*[name()='svg']")
TEAM_PLUS_ALONE_BTN = (By.XPATH, "//button[@value='혼밥']")
TEAM_PLUS_GROUP_BTN = (By.XPATH, "//button[@value='그룹']")
TEAM_PLUS_TEAM_BTN = (By.XPATH, "//button[@value='회식']")
TEAM_MENU_NAME = (By.NAME, "menu")
TEAM_STAR_BTN = (By.XPATH, "//input[@name='star']") # value 속성값 바꾸면 별점 변경도 되려나?
TEAM_PLUS_COMPLETE_BTN = (By.XPATH, "//button[text()='후기 작성 완료']")
TEAM_PLUS_IMG_ERROR = (By.XPATH, "//p[text()='리뷰 이미지는 필수입니다']")
TEAM_PLUS_MENU_NAME_ERROR = (By.XPATH, "//p[text()='메뉴명은 필수입니다']")
TEAM_PLUS_CATEGORY_ERROR = (By.XPATH, "//p[text()='카테고리는 필수입니다']")
TEAM_PLUS_REVIEW_ERROR = (By.XPATH, "//p[text()='후기는 필수입니다']")
TEAM_PLUS_STAR_ERROR = (By.XPATH, "//p[text()='별점은 최소 1점 이상이어야 합니다']")
TEAM_MENU_PLUS_IMG_CHANGE_BTN = (By.XPATH, "//h1[text()='후기 사진']/following-sibling::div//button")
TEAM_MENU_PLUS_IMG_INPUT = (By.NAME, "reviewImg")
TEAM_MENU_PLUS_REVIEW_POST = (By.CSS_SELECTOR, "div.flex.w-full.gap-6.p-4.shadow-md.rounded-2xl") # 리뷰 등록 검증 (len으로 개수 파악)




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
RECOMMEND_SEARCH_SELECTED = (By.CSS_SELECTOR, "svg.absolute.top-0.cursor-pointer.-right-2")

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

MY_MENU_PLUS_REVIEW_TEXTAREA = (By.NAME, "comment")

MY_MENU_STAR1 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[1]')
MY_MENU_STAR2 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[2]')
MY_MENU_STAR3 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[3]')
MY_MENU_STAR4 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[4]')
MY_MENU_STAR5 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[5]')
MY_MENU_STAR_BTN = (By.XPATH, "//input[@name='star']") # 별점 변경 검증 (value 속성값 확인)