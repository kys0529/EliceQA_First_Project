# 작업자 이름: 윤찬유

from selenium.webdriver.common.by import By

# 히스토리 버튼
HISTORY_BTN = (By.XPATH, '//a[@href="/history"]')
# 뒤로가기 버튼
HISTORY_BACK = (By.XPATH, '//svg[contains(@class = "cursor-pointer")]')
# 페이지 들어가서 사이트
RECOMEND_HISTORY = (By.XPATH, '//span[text()="추천 히스토리"]')
# 상단 타이틀
RECOMEND_TITLE = (By.XPATH, '//span[text()="추천 받았던 메뉴들이예요!"]')
# 이미지(첫 번째 추천 이미지)
FIRST_MENU_IMAGE = (By.XPATH, '(//img[contains(@class, "object-cover")])[1]')
# 한식라벨 - 페이지 첫 번째  @ 한식 아니라면 변경!!
LABEL_HANSIK = (By.XPATH, '(//div[text()="한식"])[1]')
# 혼밥라벨 - 페이지 첫 번째 @ 혼밥 아니라면 변경!!
LABEL_HONBAB = (By.XPATH, '(//div[text()="혼밥"])[1]')
# 음식명 텍스트 바로 찾기 - @ 타코 아니라면 변경!!
MENU_TACO = (By.XPATH, '//div[text()="타코"]')
# AI가 분석한 취향 적합률
AI_COMMAND = (By.XPATH, '(//span[text()="AI가 분석한 취향 적합률"])[1]')
# 추천후기 등록 하기 버튼 누르기
RECOMEND_BTN = (By.XPATH,'(//button[text()="추천 후기 등록하기"])[1]')


# 히스토리 -> 후기 동록하기 페이지
review_register_title = (By.XPATH, '//span[text()="후기 등록하기"]')
# 혼밥 라디오 버튼 선택 된 부분 확인 / 다른 버튼은 비활성화화
HONBAB_RADIO_SELECTED = (By.XPATH, '//button[@id="혼밥" and @aria-checked="true"]')
GROUP_RADIO_NO_SELECTED = (By.XPATH, '//button[@id="그룹" and @aria-checked="false"]')
GROUP_RADIO_NO_SELECTED = (By.XPATH, '//button[@id="회식" and @aria-checked="false"]')'

