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
# 음식명 텍스트 바로 찾기 - @ 타코 아니라면 변경!!
MENU_TACO = (By.XPATH, '//div[text()="타코"]')
MENU_RICECAKESOUP = (By.XPATH, '//div[text()="떡국"]')
# AI가 분석한 취향 적합률
AI_COMMAND = (By.XPATH, '(//span[contains(text(),"AI가 분석한 취향 적합률")])[1]')
# 추천후기 등록 하기 버튼 누르기 - 혼밥
RECOMEND_HON_BTN = (By.XPATH,'(//button[text()="추천 후기 등록하기"])[1]')


# 히스토리 -> 후기 동록하기 페이지
REVIEW_REGISTER_TITLE = (By.XPATH, '//span[text()="후기 등록하기"]')
# x 버튼 클릭 팝업 닫기
REVIEW_X_BTN = (By.XPATH, "//span[text()='후기 등록하기']/following-sibling::button/*[name()='svg']")
# 혼밥 라디오 버튼 선택 된 부분 확인 / 다른 버튼은 비활성화화
HONBAB_RADIO_SELECTED = (By.XPATH, '//button[@id="혼밥" and @aria-checked="true"]')
GROUP_RADIO_NO_SELECTED = (By.XPATH, '//button[@id="그룹" and @aria-checked="false"]')
TEAM_RADIO_NO_SELECTED = (By.XPATH, '//button[@id="회식" and @aria-checked="false"]')

MEAL_TYPE_TITLE = (By.XPATH, '//h1[text()="식사 유형"]')
PHOTO_TITLE = (By.XPATH, '//h1[text()="후기 사진"]')
PHOTO_UPLOAD_BTN = (By.XPATH, '//button[@type="button" and contains(@class, "bg-main-color")]')
REVIEW_IMG_CHANGE_BTN = (By.XPATH, "//h1[text()='후기 사진']/following-sibling::div//button")
REVIEW_IMG_INPUT = (By.NAME, "reviewImg")
MENU_NAME_TITLE = (By.XPATH, '//h1[text()="메뉴 명"]')
# 떡국으로 고정되고 비활성화 확인
MENU_NAME_INPUT = (By.XPATH, '//input[@name="menu" and @value="떡국" and @disabled]')
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



