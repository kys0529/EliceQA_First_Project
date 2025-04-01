# 작업자 이름: 채승호

from selenium.webdriver.common.by import By

# 개인 피드 요소
TEAM_FEED_TAB = (By.XPATH, "//a[@href='/my']")
TEAM_FEED_BACK_PAGE = (By.XPATH, "//span[text()='팀 피드']/preceding-sibling::*[name()='svg']")
TEAM_MENU_PLUS_BTN = (By.XPATH, "//span[contains(text(), '팀이 먹은 메뉴')]/following-sibling::button")
TEAM_EAT_SAME_MENU_BTN = (By.XPATH, "//span[contains(text(), '팀이 먹은 메뉴')]/../following-sibling::div//button[text()='같은 메뉴 먹기']") # 제일 상단에 위치한 [같은 메뉴 먹기] 버튼

TEAM_FEED_TXT = (By.XPATH, "//span[text()='팀 피드']")


# 프로필 수정
TEAM_PROFILE_CHANGE_SVG = (By.XPATH, "//*[name()='svg' and @class='cursor-pointer']")
TEAM_PROFILE_CHANGE_CANCEL_SVG = (By.XPATH, "//span[contains(text(), '프로필 정보 수정')]/following-sibling::button")

TEAM_PROFILE_IMG_CHANGE_BTN = (By.XPATH, "//img[@alt='프로필 이미지']/../following-sibling::button") # [프로필 이미지 수정] 버튼 요소 (프로필 이미지 우측에 위치)
TEAM_PROFILE_IMG_INPUT = (By.NAME, "profileImageUrl") # 프로필 이미지 URL 입력 필드 (파일 업로드가 아닌 URL 직접 입력 방식)



TEAM_PROFILE_TEXTAREA_LIKE = (By.NAME, "pros")
TEAM_PROFILE_TEXTAREA_HATE = (By.NAME, "cons")
TEAM_PROFILE_TEXTAREA_ERROR = (By.XPATH, "//p[text()='10자 이상 입력해주세요']")

TEAM_PROFILE_CHANGE_COMPLETE_BTN = (By.XPATH, "//button[text()='프로필 수정 완료']")
TEAM_PROFILE_CHANGE_COMPLETE_TXT = (By.XPATH, "//div[text()='프로필 수정 완료']")

# 내 통계
TEAM_PROFILE_STAT_TXT = (By.XPATH, "//span[text()='📊 내 통계']")
TEAM_PROFILE_STAT_IMG = (By.XPATH, "//canvas[@role='img']")

# 새로운 후기 등록하기
MY_MENU_PLUS_CANCEL_SVG = (By.XPATH, "//span[text()='새로운 후기 등록하기']/following-sibling::button/*[name()='svg']")

# 또 먹은 후기 등록하기 페이지
MY_MENU_EAT_AGAIN_CANCEL_SVG = (By.XPATH, "//span[text()='또 먹은 후기 등록하기']/following-sibling::button/*[name()='svg']")


TEAM_FEED_TAB = (By.CSS_SELECTOR, 'a[href^="/teams/"]')

TEAM_PROFILE_CHANGE = (By.XPATH, "//*[local-name()='svg' and @class='cursor-pointer']")
TEAM_SAME_MENU = (By.XPATH, "//button[text()='같은 메뉴 먹기']")
TEAM_BUTTON_UP = (By.XPATH, "//p[@class='pr-3 text-description']")

TEAM_BUTTON_DOWN = (By.XPATH, "//p[@class='pr-3 text-description line-clamp-1']")

TEXTAREA_LIKE = (By.NAME, "pros")
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
TEAM_PROFILE_SLIDER = (By.XPATH, "//span[contains(text(), '음식 성향')]/following-sibling::div//span[@role='slider']")
TEAM_PROFILE_SLIDER_VALUE = (By.CSS_SELECTOR, "span.w-8.text-right.text-gray-500.text-subbody")
TEAM_PROFILE_SLIDERBAR_ERROR = (By.XPATH, "//p[text()='맛에 대한 성향은 최소 1 이상 설정해주세요']")


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

TEAM_MENU_ALONE_BTN = (By.XPATH, "//button[@value='혼밥']")
TEAM_MENU_GROUP_BTN = (By.XPATH, "//button[@value='그룹']")
TEAM_MENU_TEAM_BTN = (By.XPATH, "//button[@value='회식']")

TEAM_MENU_IMG_CHANGE_BTN = (By.XPATH, "//h1[text()='후기 사진']/following-sibling::div//button")
TEAM_MENU_IMG_INPUT = (By.NAME, "reviewImg")

TEAM_MENU_PERSON_NAME_INPUT = (By.XPATH, "//input[@placeholder='이름을 검색해주세요']") # 그룹 전용: 같이 먹는 사람 검색창 (이름 입력 필드)
TEAM_MENU_PERSON_NAME_SEARCH_RESULT = (By.CSS_SELECTOR, "ul > li.cursor-pointer") # 그룹 전용: 검색 결과 리스트 중 첫 번째 항목 (자동완성)
TEAM_MENU_PERSON_REMOVE_SVG = (By.XPATH, "//h1[text()='같이 먹은 사람 등록']/following-sibling::div[2]//*[name()='svg']") # 등록된 사람 삭제 버튼 (× 아이콘, svg)

MY_MENU_MENU_NAME_INPUT = (By.NAME, "menu")

TEAM_MENU_CATEGORY_BTN = (By.XPATH, "//button[@role='combobox']")
TEAM_MENU_KOREAN_BTN = (By.XPATH, "//div[@role='option'][.//span[text()='한식']]")
TEAM_MENU_CHINESE_BTN = (By.XPATH, "//div[@role='option'][.//span[text()='중식']]")
TEAM_MENU_WESTERN_BTN = (By.XPATH, "//div[@role='option'][.//span[text()='양식']]")
TEAM_MENU_JAPANESE_BTN = (By.XPATH, "//div[@role='option'][.//span[text()='일식']]")
TEAM_MENU_SNACK_BTN = (By.XPATH, "//div[@role='option'][.//span[text()='분식']]")
TEAM_MENU_ASIAN_BTN = (By.XPATH, "//div[@role='option'][.//span[text()='아시안']]")
TEAM_MENU_FASTFOOD_BTN = (By.XPATH, "//div[@role='option'][.//span[text()='패스트푸드']]")
TEAM_MENU_ETC_BTN = (By.XPATH, "//div[@role='option'][.//span[text()='기타']]")
TEAM_MENU_CATEGORY_TXT = (By.XPATH, "//h1[text()='카테고리']/following-sibling::button//span") # 카테고리 변경 검증 (text 값 확인)

TEAM_MENU_REVIEW_TEXTAREA = (By.XPATH, "//textarea[@placeholder='후기를 등록 입력해주세요.']")

TEAM_MENU_STAR1 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[1]')
TEAM_MENU_STAR2 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[2]')
TEAM_MENU_STAR3 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[3]')
TEAM_MENU_STAR4 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[4]')
TEAM_MENU_STAR5 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[5]')
TEAM_MENU_STAR_BTN = (By.XPATH, "//input[@name='star']") # 별점 변경 검증 (value 속성값 확인)

TEAM_MENU_COMPLETE_BTN = (By.XPATH, "//button[text()='후기 작성 완료']")

TEAM_MENU_REVIEW_POST = (By.CSS_SELECTOR, "div.flex.w-full.gap-6.p-4.shadow-md.rounded-2xl") # 리뷰 등록 검증 (len으로 개수 파악)


#에러 메시지
TEAM_MENU_IMG_ERROR = (By.XPATH, "//p[text()='리뷰 이미지는 필수입니다']")
TEAM_MENU_MENU_NAME_ERROR = (By.XPATH, "//p[text()='메뉴명은 필수입니다']")
TEAM_MENU_CATEGORY_ERROR = (By.XPATH, "//p[text()='카테고리는 필수입니다']")
TEAM_MENU_REVIEW_ERROR = (By.XPATH, "//p[text()='후기는 필수입니다']")
TEAM_MENU_STAR_ERROR = (By.XPATH, "//p[text()='별점은 최소 1점 이상이어야 합니다']")




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
