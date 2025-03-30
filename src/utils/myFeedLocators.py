# 작업자 이름: 강연수

from selenium.webdriver.common.by import By

# /.. : 해당 요소의 부모
# /preceding-sibling : 해당 요소의 같은 부모 아래, 앞에 있는 형제
# /following-sibling : 해당 요소의 같은 부모 아래, 뒤에 있는 형제
# <svg>는 HTML이 아니라 SVG 네임스페이스(XML 기반) 이기 때문에, //svg 또는 //preceding-sibling::svg 처럼 사용시 실패 확률 높음
#  ~> *[name()='svg'] 처럼 네임스페이스 무시하고 svg 태그로 정확하게 인식 (네임스페이스: HTML이나 XML에서 같은 이름의 태그가 충돌하지 않도록 구분해주는 것)

# 홈 요소
HOME_TXT = (By.XPATH, "//span[text()='오늘 뭐먹지 ?']")

# 개인 피드 요소
MY_FEED_TAB = (By.XPATH, "//a[@href='/my']")
MY_FEED_BACK_PAGE = (By.XPATH, "//span[text()='내 피드']/preceding-sibling::*[name()='svg']")
MY_MENU_PLUS_BTN = (By.XPATH, "//span[contains(text(), '내가 먹은 메뉴')]/following-sibling::button")
MY_EAT_SAME_MENU_BTN = (By.XPATH, "//span[contains(text(), '내가 먹은 메뉴')]/../following-sibling::div//button[text()='같은 메뉴 먹기']") # 제일 상단에 위치한 [같은 메뉴 먹기] 버튼

MY_FEED_TXT = (By.XPATH, "//span[text()='내 피드']")

# 프로필 수정
MY_PROFILE_CHANGE_SVG = (By.XPATH, "//*[name()='svg' and @class='cursor-pointer']")
MY_PROFILE_CHANGE_CANCEL_SVG = (By.XPATH, "//span[contains(text(), '프로필 정보 수정')]/following-sibling::button")

MY_PROFILE_IMG_CHANGE_BTN = (By.XPATH, "//img[@alt='프로필 이미지']/../following-sibling::button") # [프로필 이미지 수정] 버튼 요소 (프로필 이미지 우측에 위치)
MY_PROFILE_IMG_INPUT = (By.NAME, "profileImageUrl") # 프로필 이미지 URL 입력 필드 (파일 업로드가 아닌 URL 직접 입력 방식)

MY_PROFILE_SLIDER = (By.XPATH, "//span[contains(text(), '음식 성향')]/following-sibling::div//span[@role='slider']")
MY_PROFILE_SLIDER_VALUE = (By.CSS_SELECTOR, "span.w-8.text-right.text-gray-500.text-subbody")
MY_PROFILE_SLIDERBAR_ERROR = (By.XPATH, "//p[text()='맛에 대한 성향은 최소 1 이상 설정해주세요']")

MY_PROFILE_TEXTAREA_LIKE = (By.NAME, "pros")
MY_PROFILE_TEXTAREA_HATE = (By.NAME, "cons")
MY_PROFILE_TEXTAREA_ERROR = (By.XPATH, "//p[text()='10자 이상 입력해주세요']")

MY_PROFILE_CHANGE_COMPLETE_BTN = (By.XPATH, "//button[text()='프로필 수정 완료']")
MY_PROFILE_CHANGE_COMPLETE_TXT = (By.XPATH, "//div[text()='프로필 수정 완료']")

# 내 통계
MY_PROFILE_STAT_TXT = (By.XPATH, "//span[text()='📊 내 통계']")
MY_PROFILE_STAT_IMG = (By.XPATH, "//canvas[@role='img']")

# 새로운 후기 등록하기
MY_MENU_PLUS_CANCEL_BTN = (By.XPATH, "//span[text()='새로운 후기 등록하기']/following-sibling::button/*[name()='svg']")

MY_MENU_PLUS_ALONE_BTN = (By.XPATH, "//button[@value='혼밥']")
MY_MENU_PLUS_GROUP_BTN = (By.XPATH, "//button[@value='그룹']")
MY_MENU_PLUS_TEAM_BTN = (By.XPATH, "//button[@value='회식']")

MY_MENU_PLUS_IMG_CHANGE_BTN = (By.XPATH, "//h1[text()='후기 사진']/following-sibling::div//button")
MY_MENU_PLUS_IMG_INPUT = (By.NAME, "reviewImg")

MY_MENU_PLUS_MENU_NAME_INPUT = (By.XPATH, "//input[@name='menu']")

MY_MENU_PLUS_CATEGORY_BTN = (By.XPATH, "//button[@role='combobox']")
MY_MENU_PLUS_KOREAN_BTN = (By.XPATH, "//div[@role='option'][.//span[text()='한식']]")
MY_MENU_PLUS_CHINESE_BTN = (By.XPATH, "//div[@role='option'][.//span[text()='중식']]")
MY_MENU_PLUS_WESTERN_BTN = (By.XPATH, "//div[@role='option'][.//span[text()='양식']]")
MY_MENU_PLUS_JAPANESE_BTN = (By.XPATH, "//div[@role='option'][.//span[text()='일식']]")
MY_MENU_PLUS_SNACK_BTN = (By.XPATH, "//div[@role='option'][.//span[text()='분식']]")
MY_MENU_PLUS_ASIAN_BTN = (By.XPATH, "//div[@role='option'][.//span[text()='아시안']]")
MY_MENU_PLUS_FASTFOOD_BTN = (By.XPATH, "//div[@role='option'][.//span[text()='패스트푸드']]")
MY_MENU_PLUS_ETC_BTN = (By.XPATH, "//div[@role='option'][.//span[text()='기타']]")
NY_MENU_PLUS_CATEGORY_TXT = (By.XPATH, "//h1[text()='카테고리']/following-sibling::button//span") # 카테고리 변경 검증 (text 값 확인)

MY_MENU_PLUS_REVIEW_TEXTAREA = (By.NAME, "comment")

MY_MENU_STAR1 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[1]')
MY_MENU_STAR2 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[2]')
MY_MENU_STAR3 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[3]')
MY_MENU_STAR4 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[4]')
MY_MENU_STAR5 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[5]')
MY_MENU_STAR_BTN = (By.XPATH, "//input[@name='star']") # 별점 변경 검증 (value 속성값 확인)

MY_MENU_PLUS_COMPLETE_BTN = (By.XPATH, "//button[text()='후기 작성 완료']")

MY_MENU_PLUS_REVIEW_POST = (By.CSS_SELECTOR, "div.flex.w-full.gap-6.p-4.shadow-md.rounded-2xl") # 리뷰 등록 검증 (len으로 개수 파악)

MY_MENU_PLUS_IMG_ERROR = (By.XPATH, "//p[text()='리뷰 이미지는 필수입니다']")
MY_MENU_PLUS_MENU_NAME_ERROR = (By.XPATH, "//p[text()='메뉴명은 필수입니다']")
MY_MENU_PLUS_CATEGORY_ERROR = (By.XPATH, "//p[text()='카테고리는 필수입니다']")
MY_MENU_PLUS_REVIEW_ERROR = (By.XPATH, "//p[text()='후기는 필수입니다']")
MY_MENU_PLUS_STAR_ERROR = (By.XPATH, "//p[text()='별점은 최소 1점 이상이어야 합니다']")