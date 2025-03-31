# 작업자 이름: 윤찬유

from selenium.webdriver.common.by import By

# 히스토리 버튼
HISTORY_BTN = (By.XPATH, '//a[@href="/history"]')
# 뒤로가기 버튼
HISTORY_BACK = (By.XPATH, "//span[text()='추천 히스토리']/preceding-sibling::*[name()='svg']")
# 페이지 들어가서 사이트
HOME_BACK = (By.XPATH, '//span[contains(text(),"오늘 뭐먹지")]')
RECOMEND_HISTORY = (By.XPATH, '//span[text()="추천 히스토리"]')
# 상단 타이틀
RECOMEND_TITLE = (By.XPATH, '//span[contains(text(),"추천 받았던 메뉴들이에요!")]')
# 이미지(첫 번째 추천 이미지)
FIRST_MENU_IMAGE = (By.XPATH, '(//img[contains(@class, "object-cover")])[1]')
# 한식라벨 - 페이지 첫 번째  @ 한식 아니라면 변경!!
LABEL_HANSIK = (By.XPATH, '(//div[text()="한식"])[1]')
# 혼밥라벨 - 페이지 첫 번째 @ 혼밥 아니라면 변경!!
LABEL_HONBAB = (By.XPATH, '(//div[text()="혼밥"])[1]')
LABEL_GROUP = (By.XPATH, '(//div[text()="그룹"])[1]')
LABEL_TEAM = (By.XPATH, '(//div[text()="회식"])[1]')
# 음식명 텍스트 바로 찾기 - @ 타코 아니라면 변경!!
MENU_TACO = (By.XPATH, '//div[text()="타코"]')
MENU_RICECAKESOUP = (By.XPATH, '//div[text()="떡국"]')
MENU_Jjimdak = (By.XPATH, '//div[text()="찜닭"]')
MENU_Dongtae_jjigae = (By.XPATH, '//div[text()="동태찌개"]')
MENU_Nakgopsae = (By.XPATH, '//div[text()="낙곱새"]')
MENU_JAPCHAE = (By.XPATH, '//div[text()="잡채채"]')
MENU_DONGTAETANG = (By.XPATH, '//div[text()="동태탕"]')
MENU_HOE = (By.XPATH, '//div[text()="회"]')
MENU_HAEMUL_PAJEON = (By.XPATH, '//div[text()="해물파전"]')
MENU_MANDUGUK = (By.XPATH, '//div[text()="만둣국"]')
MENU_HAEMULTANG = (By.XPATH, '//div[text()="해물탕"]')
MENU_JANGEO_GUI = (By.XPATH, '//div[text()="장어구이"]')



# AI가 분석한 취향 적합률
AI_COMMAND = (By.XPATH, '(//span[contains(text(),"AI가 분석한 취향 적합률")])[1]')
# 추천후기 등록 하기 버튼 누르기 - 혼밥
RECOMEND_HON_BTN = (By.XPATH,'(//button[text()="추천 후기 등록하기"])[1]')
RECOMEND_GROUP_BTN = (By.XPATH,'(//button[text()="추천 후기 등록하기"])[2]')
RECOMEND_TEAM_BTN = (By.XPATH,'(//button[text()="추천 후기 등록하기"])[3]')

# 히스토리 -> 후기 동록하기 페이지
REVIEW_REGISTER_TITLE = (By.XPATH, '//span[text()="후기 등록하기"]')
# x 버튼 클릭 팝업 닫기
REVIEW_X_BTN = (By.XPATH, "//span[text()='후기 등록하기']/following-sibling::button/*[name()='svg']")
# 혼밥 라디오 버튼 선택 된 부분 확인 / 다른 버튼은 비활성화화
HONBAB_RADIO_SELECTED = (By.XPATH, '//button[@id="혼밥" and @aria-checked="true"]')
GROUP_RADIO_SELECTED = (By.XPATH, '//button[@id="그룹" and @aria-checked="true"]')
TEAM_RADIO_SELECTED = (By.XPATH, '//button[@id="회식" and @aria-checked="true"]')

# 그룹 라디오
HONBAB_RADIO_NO_SELECTED = (By.XPATH, '//button[@id="혼밥" and @aria-checked="false"]')
GROUP_RADIO_NO_SELECTED = (By.XPATH, '//button[@id="그룹" and @aria-checked="false"]')
TEAM_RADIO_NO_SELECTED = (By.XPATH, '//button[@id="회식" and @aria-checked="false"]')


MEAL_TYPE_TITLE = (By.XPATH, '//h1[text()="식사 유형"]')
PHOTO_TITLE = (By.XPATH, '//h1[text()="후기 사진"]')
PHOTO_UPLOAD_BTN = (By.XPATH, '//button[@type="button" and contains(@class, "bg-main-color")]')
REVIEW_IMG_CHANGE_BTN = (By.XPATH, "//h1[text()='후기 사진']/following-sibling::div//button")
REVIEW_IMG_INPUT = (By.NAME, "reviewImg")
MENU_NAME_TITLE = (By.XPATH, '//h1[text()="메뉴 명"]')
# 떡국으로 고정되고 비활성화 확인
MENU_NAME_INPUT_HON = (By.XPATH, '//input[@name="menu" and @value="잡채" and @disabled]')
# 동태탕으로 고정되고 비활성화 확인
MENU_NAME_INPUT_GROUP = (By.XPATH, '//input[@name="menu" and @value="동태탕" and @disabled]')
MENU_NAME_INPUT_TEAM = (By.XPATH, '//input[@name="menu" and @value="회" and @disabled]')

CATEGORY_TITLE = (By.XPATH, '//h1[text()="카테고리"]')

# 한식 고정 /비활성화 확인인
CATEGORY_DROPDOWN = (By.XPATH, '//button[@role="combobox"]//span[text()="한식"]')
CATEGORY_SELECT_DISABLED = (By.XPATH, '//select[@disabled]')


REVIEW_CONTENT_TITLE = (By.XPATH, '//h1[text()="후기"]')

#테스트칸
REVIEW_TEXTAREA = (By.XPATH, '//textarea[@name="comment"]')
RATING_TITLE = (By.XPATH, '//h1[text()="별점"]')
STAR1 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[1]')
STAR2 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[2]')
STAR3 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[3]')
STAR4 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[4]')
STAR5 = (By.XPATH, '(//div[contains(@class, "cursor-pointer") and text()="★"])[5]')
STAR_MENU_BTN = (By.XPATH, "//input[@name='star']")

SUBMIT_REVIEW_BTN = (By.XPATH, '//button[@type="submit" and text()="후기 작성 완료"]')

# 빈칸 후기 작성 완료 눌렀을때 
REVIEW_IMAGE_REQUIRED = (By.XPATH, '//p[text()="리뷰 이미지는 필수입니다"]')
REVIEW_TEXT_REQUIRED = (By.XPATH, '//p[text()="후기는 필수입니다"]')
STAR_REQUIRED = (By.XPATH, '//p[text()="별점은 최소 1점 이상이어야 합니다"]')

REVIEW_SUBMIT_DONE_BTN = (By.XPATH, '//button[text()="후기 등록 완료" and @disabled]')


####같이 먹기
GROUP_EAT = (By.XPATH, '//h1[text()="같이 먹은 사람 등록"]')
GROUP_EAT_PEOPLE = (By.XPATH, '//div[@class="flex items-center gap-4 overflow-x-auto whitespace-nowrap"]/div')

# 추천 카드 - 메뉴명 텍스트
MENU_NAME_TEXT = (By.XPATH, '(//div[contains(@class,"text-base")])[1]')

# 추천 카드 - 식사유형 라벨 (혼밥, 그룹, 회식)
MEAL_TYPE_LABEL = (By.XPATH, '(//div[@class="rounded-full bg-sub text-white px-2 py-1 text-xs font-bold"])[1]')

# 추천 카드 - 카테고리 라벨 (한식, 양식 등)
CATEGORY_LABEL = (By.XPATH, '(//div[@class="rounded-full bg-main text-white px-2 py-1 text-xs font-bold"])[1]')


# 식사유형 라디오 버튼 동적
MEAL_TYPE_RADIO_SELECTED = '//button[@id="{}" and @aria-checked="true"]'

# 메뉴명 input 동적
MENU_NAME_INPUT = '//input[@name="menu" and @value="{}" and @disabled]'

# 카테고리 드롭다운 선택 값 동적
CATEGORY_SELECTED = '//button[@role="combobox"]//span[text()="{}"]'