# 작업자 이름: 윤찬유

import pytest
import inspect
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from src.pages.history import history
from src.utils import historyLocators

def test_history_001(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("히스토리")
        
        myHistory.getElement(historyLocators.HISTORY_BACK).click()
        
        assert myHistory.getElement(historyLocators.HOME_BACK)
        
        myHistory.logger.info(f"▶️ history001 -'홈' 페이지 이동 확인")
        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗{inspect.currentframe().f_code.co_name} : {e}")
        raise
    
def test_history_002(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("히스토리")
        assert myHistory.getElement(historyLocators.RECOMEND_HISTORY)
        myHistory.logger.info(f"▶️ history002 - 추천 히스토리(페이지 정상 노출)")
        
        assert myHistory.getElement(historyLocators.RECOMEND_TITLE)
        myHistory.logger.info(f"▶️ history003 - 추천 받았던 메뉴들 이예요!(문구 확인)")
        assert myHistory.getElement(historyLocators.MENU_IMAGE1)
        assert myHistory.getElement(historyLocators.LABEL_HANSIK) 
        assert myHistory.getElement(historyLocators.LABEL_HONBAB) 
        assert myHistory.getElement(historyLocators.MENU_JAPCHAE) # @변경 필요
        assert myHistory.getElement(historyLocators.AI_COMMAND)
        assert myHistory.getElement(historyLocators.RECOMEND_BTN)
        
        myHistory.logger.info(f"▶️ history004 - '혼밥' 음식딱지 노출 확인!")
    
        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

def test_history_003(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록페이지")

        assert myHistory.getElement(historyLocators.REVIEW_REGISTER_TITLE)

        myHistory.logger.info(f"▶️ history005 - '혼밥' 후기 등록하기 페이지 이동 확인")
        
        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗{inspect.currentframe().f_code.co_name} : {e}")
        raise

def test_history_004(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록페이지")

        myHistory.getElement(historyLocators.REVIEW_X_BTN).click()

        assert myHistory.getElement(historyLocators.RECOMEND_HISTORY)
        myHistory.logger.info(f"▶️ history006 - '혼밥' 팝업 취소 후 히스토리 창으로 이동")
        
        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

def test_history_005(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록페이지")

        assert myHistory.getElement(historyLocators.REVIEW_REGISTER_TITLE)
        myHistory.logger.info(f"▶️ history007 - '혼밥 - 후기 등록하기' 타이틀 문구 확인")
        
        assert myHistory.getElement(historyLocators.MEAL_TYPE_TITLE)
        myHistory.logger.info(f"▶️ history008 - '혼밥 - 식사 유형' 문구 확인")
    
        assert myHistory.getElement(historyLocators.HONBAB_RADIO_SELECTED)
        assert myHistory.getElement(historyLocators.GROUP_RADIO_NO_SELECTED)
        assert myHistory.getElement(historyLocators.TEAM_RADIO_NO_SELECTED)
        myHistory.logger.info(f"▶️ history008 - '혼밥'버튼만 활성화 확인")

        assert myHistory.getElement(historyLocators.PHOTO_TITLE)
        myHistory.logger.info(f"▶️ history009 - '혼밥 - 사진 / 사진 영역' 확인")
        
        assert myHistory.getElement(historyLocators.MENU_NAME_TITLE)
        assert myHistory.getElement(historyLocators.MENU_JAPCHAE_INPUT) # @ 변경 필요
        myHistory.logger.info(f"▶️ history010 - '혼밥 - 메뉴/ 비활성화 된 메뉴 이름)' 확인")
        
        assert myHistory.getElement(historyLocators.CATEGORY_TITLE)
        assert myHistory.getElement(historyLocators.CATEGORY_DROPDOWN)
        assert myHistory.getElement(historyLocators.CATEGORY_SELECT_DISABLED)
        myHistory.logger.info(f"▶️ history011 - '혼밥 - 카테고리/ 비활성화 된 카테고리 이름' 확인")
        
        assert myHistory.getElement(historyLocators.REVIEW_CONTENT_TITLE)
        assert myHistory.getElement(historyLocators.REVIEW_TEXTAREA)
        myHistory.logger.info(f"▶️ history012 - '혼밥 - 후기/ 후기 입력칸' 확인")
        
        assert myHistory.getElement(historyLocators.RATING_TITLE)
        assert myHistory.getElement(historyLocators.STAR1)
        assert myHistory.getElement(historyLocators.STAR2)
        assert myHistory.getElement(historyLocators.STAR3)
        assert myHistory.getElement(historyLocators.STAR4)
        assert myHistory.getElement(historyLocators.STAR5)
        myHistory.logger.info(f"▶️ history013 - '혼밥 - 별점/ 별점 칸' 확인")
        
        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise


def test_history_006(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록페이지")

        myHistory.getElement(historyLocators.SUBMIT_REVIEW_BTN).click()

        assert myHistory.getElement(historyLocators.REVIEW_IMAGE_REQUIRED)
        assert myHistory.getElement(historyLocators.REVIEW_TEXT_REQUIRED)
        assert myHistory.getElement(historyLocators.STAR_REQUIRED)
        myHistory.logger.info(f"▶️ history014 - '혼밥' 사진,후기,별점 에러 메세지 확인")
        
        
        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise
    
def test_history_007(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록페이지")
        
        assert myHistory.screenDiff(historyLocators.REVIEW_IMG_INPUT, inspect.currentframe().f_code.co_name, "reviewImg", "image", myHistory.getRandomImage())
        myHistory.logger.info(f"▶️ history015 - '혼밥' 사진 등록 확인")
        
        randomReview = myHistory.getRandomReview()
        myHistory.getElement(historyLocators.REVIEW_TEXTAREA).send_keys(randomReview)
        
        assert myHistory.getElement(historyLocators.REVIEW_TEXTAREA).get_attribute("value") == randomReview
        myHistory.logger.info(f"▶️ history016 - '혼밥' 작성한 후기 노출 확인")
        
        randomValue, randomStar = myHistory.getRandomStar()
        myHistory.getElement(randomStar).click()
        
        assert myHistory.getElement(historyLocators.STAR_MENU_BTN).get_attribute("value") == randomValue
        myHistory.logger.info(f"▶️ history017 - '혼밥' 별점 체크 확인")

        myHistory.getElement(historyLocators.SUBMIT_REVIEW_BTN).click()

        assert myHistory.getElement(historyLocators.REVIEW_SUBMIT_DONE_BTN)
        myHistory.logger.info(f"▶️ history018 - '혼밥' 후기등록 완료 및 버튼 비활성화 확인")

        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

def test_history_008(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("히스토리")
        
        assert myHistory.getElement(historyLocators.MENU_IMAGE2)
        assert myHistory.getElement(historyLocators.LABEL_HANSIK2)
        assert myHistory.getElement(historyLocators.LABEL_GROUP) 
        assert myHistory.getElement(historyLocators.MENU_HAEMUL_PAJEON) # @ 변경 필요
        assert myHistory.getElement(historyLocators.AI_COMMAND2)
        assert myHistory.getElement(historyLocators.RECOMEND_BTN)
        
        myHistory.logger.info("▶️ history019 - '그룹' 음식 딱지 노출 확인!")
    
        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f" ❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise
    
def test_history_009(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록페이지")
        
        assert myHistory.getElement(historyLocators.REVIEW_REGISTER_TITLE)
        
        myHistory.logger.info("▶️ history020 - '그룹' 후기 등록하기 페이지 이동 확인")
        
        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

def test_history_010(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록페이지")
        
        myHistory.getElement(historyLocators.REVIEW_X_BTN).click()
        
        assert myHistory.getElement(historyLocators.RECOMEND_HISTORY)
        myHistory.logger.info("▶️ history021 - '그룹' 팝업 취소 후 히스토리 창으로 이동")
        
        
        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗{inspect.currentframe().f_code.co_name} : {e}")
        raise

def test_history_011(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록페이지")
        
        assert myHistory.getElement(historyLocators.REVIEW_REGISTER_TITLE)
        myHistory.logger.info(f"▶️ history022 - '그룹 - 후기 등록하기' 타이틀 문구 확인")
        
        assert myHistory.getElement(historyLocators.MEAL_TYPE_TITLE)
        myHistory.logger.info(f"▶️ history023 - '그룹 - 식사 유형' 문구 확인")
        
        assert myHistory.getElement(historyLocators.HONBAB_RADIO_NO_SELECTED) 
        assert myHistory.getElement(historyLocators.GROUP_RADIO_SELECTED) 
        assert myHistory.getElement(historyLocators.TEAM_RADIO_NO_SELECTED) 
        myHistory.logger.info(f"▶️ history023 - '그룹 - 버튼만 활성화 확인")
        
        assert myHistory.getElement(historyLocators.PHOTO_TITLE)
        myHistory.logger.info(f"▶️ history024 - '그룹 - 사진 / 사진 영역' 확인")        
        
        assert myHistory.getElement(historyLocators.GROUP_EAT)
        people_list = myHistory.getElements(historyLocators.GROUP_EAT_PEOPLE)
        assert len(people_list) > 0, "❌ 같이 먹은 사람이 등록되어 있지 않음!"
        print(f"✅ 등록된 사람 수: {len(people_list)}명")
        myHistory.logger.info(f"▶️ history025 - '그룹 - 같이 먹은 사람 등록/ 리스트' 확인")
        
        
        assert myHistory.getElement(historyLocators.MENU_NAME_TITLE) 
        assert myHistory.getElement(historyLocators.MENU_HAEMUL_PAJEON_INPUT) # @ 변경 필요
        myHistory.logger.info(f"▶️ history026 - '그룹 - 메뉴/ 비활성화 된 메뉴 이름' 확인")
        
        assert myHistory.getElement(historyLocators.CATEGORY_TITLE)
        assert myHistory.getElement(historyLocators.CATEGORY_DROPDOWN)
        assert myHistory.getElement(historyLocators.CATEGORY_SELECT_DISABLED)
        myHistory.logger.info(f"▶️ history027 - '그룹 - 카테고리/ 비활성화 된 카테고리 이름' 확인")
        
        assert myHistory.getElement(historyLocators.REVIEW_CONTENT_TITLE)
        assert myHistory.getElement(historyLocators.REVIEW_TEXTAREA)
        myHistory.logger.info(f"▶️ history028 - '그룹 - 후기/ 후기 입력칸' 확인")
      
        assert myHistory.getElement(historyLocators.RATING_TITLE)
        assert myHistory.getElement(historyLocators.STAR1)
        assert myHistory.getElement(historyLocators.STAR2)
        assert myHistory.getElement(historyLocators.STAR3)
        assert myHistory.getElement(historyLocators.STAR4)
        assert myHistory.getElement(historyLocators.STAR5)
        myHistory.logger.info(f"▶️ history029 - '그룹 - 별점/ 별점 칸' 확인")
        
        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

def test_history_012(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록페이지")
        
        myHistory.getElement(historyLocators.SUBMIT_REVIEW_BTN).click()
        
        assert myHistory.getElement(historyLocators.REVIEW_IMAGE_REQUIRED)
        assert myHistory.getElement(historyLocators.REVIEW_TEXT_REQUIRED)
        assert myHistory.getElement(historyLocators.STAR_REQUIRED)
        myHistory.logger.info(f"▶️ history030 - '그룹' 사진,후기,별점 에러 메세지 확인")
        
        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗{inspect.currentframe().f_code.co_name} : {e}")
        raise
    
def test_history_013(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록페이지")
        
        assert myHistory.screenDiff(historyLocators.REVIEW_IMG_INPUT, inspect.currentframe().f_code.co_name, "reviewImg", "image", myHistory.getRandomImage())
        myHistory.logger.info(f"▶️ history031 - '그룹' 사진 등록 확인")
        
        randomReview = myHistory.getRandomReview()
        myHistory.getElement(historyLocators.REVIEW_TEXTAREA).send_keys(randomReview)
        assert myHistory.getElement(historyLocators.REVIEW_TEXTAREA).get_attribute("value") == randomReview
        myHistory.logger.info(f"▶️ history032 - '그룹' 작성한 후기 노출 확인")
        
        randomValue, randomStar = myHistory.getRandomStar()
        myHistory.getElement(randomStar).click()
        assert myHistory.getElement(historyLocators.STAR_MENU_BTN).get_attribute("value") == randomValue
        myHistory.logger.info(f"▶️ history033 - '그룹' 별점 체크 확인")
        
        myHistory.getElement(historyLocators.SUBMIT_REVIEW_BTN).click()
        
        assert myHistory.getElement(historyLocators.REVIEW_SUBMIT_DONE_BTN)
        
        myHistory.logger.info(f"▶️ history034 - '그룹' 후기등록 완료 및 버튼 비활성화 확인")

        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗{inspect.currentframe().f_code.co_name} : {e}")
        raise

def test_history_014(createDriver: WebDriver):
    try:
        myHistory = history(createDriver)
        myHistory.goToPage("히스토리")
        
        assert myHistory.getElement(historyLocators.MENU_IMAGE3)
        assert myHistory.getElement(historyLocators.LABEL_HANSIK3)
        assert myHistory.getElement(historyLocators.LABEL_TEAM) 
        assert myHistory.getElement(historyLocators.MENU_MANDUGUK) # @ 변경 필요
        assert myHistory.getElement(historyLocators.AI_COMMAND3)
        assert myHistory.getElement(historyLocators.RECOMEND_BTN)
        myHistory.logger.info("▶️ history035 - '팀' 음식 딱지 노출 확인!")
        
        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗{inspect.currentframe().f_code.co_name} : {e}")
        raise

def test_history_015(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록페이지")
        
        assert myHistory.getElement(historyLocators.REVIEW_REGISTER_TITLE)
        myHistory.logger.info("▶️ history036 - '팀' 후기 등록하기 페이지 이동 확인")
        
        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

def test_history_016(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록페이지")
        
        myHistory.getElement(historyLocators.REVIEW_X_BTN).click()
        
        assert myHistory.getElement(historyLocators.RECOMEND_HISTORY)
        myHistory.logger.info("▶️ history037 - '팀' 팝업 취소 후 히스토리 창으로 이동")
        
        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗{inspect.currentframe().f_code.co_name} : {e}")
        raise

def test_history_017(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록페이지")

        assert myHistory.getElement(historyLocators.REVIEW_REGISTER_TITLE)
        myHistory.logger.info(f"▶️ history038 - '팀 - 후기 등록하기' 타이틀 문구 확인")

        assert myHistory.getElement(historyLocators.MEAL_TYPE_TITLE)
        myHistory.logger.info(f"▶️ history039 - '팀 - 식사 유형' 문구 확인")
        
        assert myHistory.getElement(historyLocators.HONBAB_RADIO_NO_SELECTED)
        assert myHistory.getElement(historyLocators.GROUP_RADIO_NO_SELECTED)
        assert myHistory.getElement(historyLocators.TEAM_RADIO_SELECTED)
        myHistory.logger.info(f"▶️ history039 - '팀 - 버튼만 활성화 확인")
        
        assert myHistory.getElement(historyLocators.PHOTO_TITLE)
        myHistory.logger.info(f"▶️ history040 - '팀 - 사진 / 사진 영역' 확인")
        
        assert myHistory.getElement(historyLocators.MENU_NAME_TITLE)
        assert myHistory.getElement(historyLocators.MENU_MANDUGUK_INPUT) # @ 변경 필요
        myHistory.logger.info(f"▶️ history041 - '팀 - 메뉴/ 비활성화 된 메뉴 이름' 확인")

        assert myHistory.getElement(historyLocators.CATEGORY_TITLE)
        assert myHistory.getElement(historyLocators.CATEGORY_DROPDOWN)
        assert myHistory.getElement(historyLocators.CATEGORY_SELECT_DISABLED)
        myHistory.logger.info(f"▶️ history042 - '팀 - 카테고리/ 비활성화 된 카테고리 이름' 확인")
        
        assert myHistory.getElement(historyLocators.REVIEW_CONTENT_TITLE)
        assert myHistory.getElement(historyLocators.REVIEW_TEXTAREA)
        myHistory.logger.info(f"▶️ history043 - '팀 - 후기/ 후기 입력칸' 확인")
        
        assert myHistory.getElement(historyLocators.RATING_TITLE)
        assert myHistory.getElement(historyLocators.STAR1)
        assert myHistory.getElement(historyLocators.STAR2)
        assert myHistory.getElement(historyLocators.STAR3)
        assert myHistory.getElement(historyLocators.STAR4)
        assert myHistory.getElement(historyLocators.STAR5)
        myHistory.logger.info(f"▶️ history044 - '팀 - 별점/ 별점 칸' 확인")
        
        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

def test_history_018(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록페이지")
        time.sleep(2)
        myHistory.getElement(historyLocators.SUBMIT_REVIEW_BTN).click()
        time.sleep(2)
        assert myHistory.getElement(historyLocators.REVIEW_IMAGE_REQUIRED)
        assert myHistory.getElement(historyLocators.REVIEW_TEXT_REQUIRED)
        assert myHistory.getElement(historyLocators.STAR_REQUIRED)
        myHistory.logger.info(f"▶️ history045 - '팀' 사진,후기,별점 에러 메세지 확인")
        
        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise
    
def test_history_019(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록페이지")
        
        assert myHistory.screenDiff(historyLocators.REVIEW_IMG_INPUT, inspect.currentframe().f_code.co_name, "reviewImg", "image", myHistory.getRandomImage())
        myHistory.logger.info(f"▶️ history046 - '팀' 사진 등록 확인")
        randomReview = myHistory.getRandomReview()
        myHistory.getElement(historyLocators.REVIEW_TEXTAREA).send_keys(randomReview)
        assert myHistory.getElement(historyLocators.REVIEW_TEXTAREA).get_attribute("value") == randomReview
        myHistory.logger.info(f"▶️ history047 - '팀' 작성한 후기 노출 확인")
        
        randomValue, randomStar = myHistory.getRandomStar()
        myHistory.getElement(randomStar).click()
        assert myHistory.getElement(historyLocators.STAR_MENU_BTN).get_attribute("value") == randomValue
        myHistory.logger.info(f"▶️ history048 - '팀' 별점 체크 확인")
        
        myHistory.getElement(historyLocators.SUBMIT_REVIEW_BTN).click()
        assert myHistory.getElement(historyLocators.REVIEW_SUBMIT_DONE_BTN)
        myHistory.logger.info(f"▶️ history048 - '팀' 후기등록 완료 및 버튼 비활성화 확인")
        myHistory.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise
