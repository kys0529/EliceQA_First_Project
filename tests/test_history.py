# 작업자 이름: 윤찬유

import pytest
import inspect
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from src.pages.history import history
from src.utils import historyLocators

@pytest.mark.cy
def test_history_001(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("히스토리")
        assert myHistory.getElement((By.XPATH, '//span[text()="추천 히스토리"]'))

        # 첫 번째 카드 정보 로딩 기다림
        myHistory.wait.until(EC.presence_of_element_located((By.XPATH, '(//div[contains(@class, "text-white bg-main")])[1]')))
        myHistory.wait.until(EC.presence_of_element_located((By.XPATH, '(//div[contains(@class, "text-white bg-sub")])[1]')))
        myHistory.wait.until(EC.presence_of_element_located((By.XPATH, '(//div[contains(@class, "font-semibold")])[1]')))

        # 🟢 첫 번째 카드에서 정보 저장
        selected_meal_type = myHistory.getElement((By.XPATH, '(//div[contains(@class, "text-white bg-main")])[1]')).text.strip()
        selected_category = myHistory.getElement((By.XPATH, '(//div[contains(@class, "text-white bg-sub")])[1]')).text.strip()
        selected_menu = myHistory.getElement((By.XPATH, '(//div[contains(@class, "font-semibold")])[1]')).text.strip()

        # 추천 후기 등록 버튼 클릭
        myHistory.wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="추천 후기 등록하기"]')))
        myHistory.getElement((By.XPATH, '(//button[text()="추천 후기 등록하기"])[1]')).click()

        # 🟢 후기 폼에서 값 추출
        input_menu = myHistory.getElement((By.XPATH, '//input[@placeholder="메뉴 명"]')).get_attribute("value").strip()
        selected_option = myHistory.getElement((By.XPATH, '//select/option[@selected]')).text.strip()
        selected_radio = myHistory.getElement((By.XPATH, '//input[@type="radio" and @checked]/following-sibling::label')).text.strip()

        # ✅ 값 비교
        assert input_menu == selected_menu
        assert selected_option == selected_category
        assert selected_radio == selected_meal_type

        myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise


# #TESTCASE
# # @pytest.mark.cy
# def test_history_001(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("히스토리")
#         assert myHistory.getElement(historyLocators.RECOMEND_HISTORY)
#         assert myHistory.getElement(historyLocators.RECOMEND_TITLE)
#         assert myHistory.getElement(historyLocators.FIRST_MENU_IMAGE)
#         assert myHistory.getElement(historyLocators.LABEL_HANSIK)
#         assert myHistory.getElement(historyLocators.LABEL_HONBAB)
#         assert myHistory.getElement(historyLocators.MENU_RICECAKESOUP)
#         assert myHistory.getElement(historyLocators.AI_COMMAND)
#         assert myHistory.getElement(historyLocators.RECOMEND_HON_BTN)
    
#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise

# # @pytest.mark.cy
# def test_history_002(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("히스토리")
        
#         myHistory.getElement(historyLocators.HISTORY_BACK).click()
#         time.sleep(2)
#         assert myHistory.getElement(historyLocators.HOME_BACK)
        
#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise
        
# # @pytest.mark.cy
# def test_history_003(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("후기등록혼밥")
#         time.sleep(2)
#         assert myHistory.getElement(historyLocators.REVIEW_REGISTER_TITLE)
        
#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise

# def test_history_004(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("후기등록혼밥")
#         myHistory.getElement(historyLocators.REVIEW_X_BTN).click()
#         assert myHistory.getElement(historyLocators.RECOMEND_HISTORY)
        
        
#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise

# def test_history_005(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("후기등록혼밥")
#         assert myHistory.getElement(historyLocators.REVIEW_REGISTER_TITLE)
#         assert myHistory.getElement(historyLocators.MEAL_TYPE_TITLE)
#         assert myHistory.getElement(historyLocators.HONBAB_RADIO_SELECTED)
#         assert myHistory.getElement(historyLocators.GROUP_RADIO_NO_SELECTED)
#         assert myHistory.getElement(historyLocators.TEAM_RADIO_NO_SELECTED)
#         assert myHistory.getElement(historyLocators.PHOTO_TITLE)
#         assert myHistory.getElement(historyLocators.MENU_NAME_TITLE)
#         assert myHistory.getElement(historyLocators.MENU_NAME_INPUT)
#         assert myHistory.getElement(historyLocators.CATEGORY_TITLE)
#         assert myHistory.getElement(historyLocators.CATEGORY_DROPDOWN)
#         assert myHistory.getElement(historyLocators.CATEGORY_SELECT_DISABLED)
#         assert myHistory.getElement(historyLocators.REVIEW_CONTENT_TITLE)
#         assert myHistory.getElement(historyLocators.REVIEW_TEXTAREA)
#         assert myHistory.getElement(historyLocators.RATING_TITLE)
#         assert myHistory.getElement(historyLocators.STAR1)
#         assert myHistory.getElement(historyLocators.STAR2)
#         assert myHistory.getElement(historyLocators.STAR3)
#         assert myHistory.getElement(historyLocators.STAR4)
#         assert myHistory.getElement(historyLocators.STAR5)
        
#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise

# def test_history_006(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("후기등록혼밥")
#         myHistory.getElement(historyLocators.SUBMIT_REVIEW_BTN).click()
#         assert myHistory.getElement(historyLocators.REVIEW_IMAGE_REQUIRED)
#         assert myHistory.getElement(historyLocators.REVIEW_TEXT_REQUIRED)
#         assert myHistory.getElement(historyLocators.STAR_REQUIRED)
        
#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise
    
# # @pytest.mark.cy
# def test_history_007(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("후기등록혼밥")
        
#         assert myHistory.screenDiff(historyLocators.REVIEW_IMG_INPUT, inspect.currentframe().f_code.co_name, "reviewImg", "image", myHistory.getRandomImage())
        
#         randomReview = myHistory.getRandomReview()
#         myHistory.getElement(historyLocators.REVIEW_TEXTAREA).send_keys(randomReview)
#         assert myHistory.getElement(historyLocators.REVIEW_TEXTAREA).get_attribute("value") == randomReview

#         randomValue, randomStar = myHistory.getRandomStar()
#         myHistory.getElement(randomStar).click()
#         assert myHistory.getElement(historyLocators.STAR_MENU_BTN).get_attribute("value") == randomValue

#         myHistory.getElement(historyLocators.SUBMIT_REVIEW_BTN).click()
#         time.sleep(2)
#         assert myHistory.getElement(historyLocators.REVIEW_SUBMIT_DONE_BTN)

#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise

# # @pytest.mark.cy
# def test_history_008(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("히스토리")
#         assert myHistory.getElement(historyLocators.RECOMEND_HISTORY)
#         assert myHistory.getElement(historyLocators.RECOMEND_TITLE)
#         assert myHistory.getElement(historyLocators.FIRST_MENU_IMAGE)
#         assert myHistory.getElement(historyLocators.LABEL_HANSIK)
#         assert myHistory.getElement(historyLocators.LABEL_GROUP) #변경
#         assert myHistory.getElement(historyLocators.MENU_DONGTAETANG) #변경경
#         assert myHistory.getElement(historyLocators.AI_COMMAND)
#         assert myHistory.getElement(historyLocators.RECOMEND_HON_BTN)
    
#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise

        
# # @pytest.mark.cy
# def test_history_009(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("후기등록같이")
#         time.sleep(2)
#         assert myHistory.getElement(historyLocators.REVIEW_REGISTER_TITLE)
        
#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise

# # @pytest.mark.cy
# def test_history_010(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("후기등록같이")
#         time.sleep(2)
#         myHistory.getElement(historyLocators.REVIEW_X_BTN).click()
#         assert myHistory.getElement(historyLocators.RECOMEND_HISTORY)
        
        
#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise

# @pytest.mark.cy
# def test_history_011(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("후기등록같이")
#         assert myHistory.getElement(historyLocators.REVIEW_REGISTER_TITLE)
#         assert myHistory.getElement(historyLocators.MEAL_TYPE_TITLE)
#         assert myHistory.getElement(historyLocators.HONBAB_RADIO_NO_SELECTED) #변경경
#         assert myHistory.getElement(historyLocators.GROUP_RADIO_SELECTED) #변경경
#         assert myHistory.getElement(historyLocators.TEAM_RADIO_NO_SELECTED) #변경경
#         assert myHistory.getElement(historyLocators.PHOTO_TITLE)
#         assert myHistory.getElement(historyLocators.MENU_NAME_TITLE) 
#         assert myHistory.getElement(historyLocators.MENU_NAME_INPUT_GROUP) #변경경
#         assert myHistory.getElement(historyLocators.GROUP_EAT)
#         people_list = myHistory.getElement(historyLocators.GROUP_EAT_PEOPLE)
#         assert len(people_list) > 0, "❌ 같이 먹은 사람이 등록되어 있지 않음!"
#         print(f"✅ 등록된 사람 수: {len(people_list)}명")
#         assert myHistory.getElement(historyLocators.CATEGORY_TITLE)
#         assert myHistory.getElement(historyLocators.CATEGORY_DROPDOWN)
#         assert myHistory.getElement(historyLocators.CATEGORY_SELECT_DISABLED)
#         assert myHistory.getElement(historyLocators.REVIEW_CONTENT_TITLE)
#         assert myHistory.getElement(historyLocators.REVIEW_TEXTAREA)
#         assert myHistory.getElement(historyLocators.RATING_TITLE)
#         assert myHistory.getElement(historyLocators.STAR1)
#         assert myHistory.getElement(historyLocators.STAR2)
#         assert myHistory.getElement(historyLocators.STAR3)
#         assert myHistory.getElement(historyLocators.STAR4)
#         assert myHistory.getElement(historyLocators.STAR5)
        
#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise

# def test_history_012(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("후기등록같이")
#         myHistory.getElement(historyLocators.SUBMIT_REVIEW_BTN).click()
#         assert myHistory.getElement(historyLocators.REVIEW_IMAGE_REQUIRED)
#         assert myHistory.getElement(historyLocators.REVIEW_TEXT_REQUIRED)
#         assert myHistory.getElement(historyLocators.STAR_REQUIRED)
        
#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise
    
# # @pytest.mark.cy
# def test_history_013(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("후기등록같이")
        
#         assert myHistory.screenDiff(historyLocators.REVIEW_IMG_INPUT, inspect.currentframe().f_code.co_name, "reviewImg", "image", myHistory.getRandomImage())
        
#         randomReview = myHistory.getRandomReview()
#         myHistory.getElement(historyLocators.REVIEW_TEXTAREA).send_keys(randomReview)
#         assert myHistory.getElement(historyLocators.REVIEW_TEXTAREA).get_attribute("value") == randomReview

#         randomValue, randomStar = myHistory.getRandomStar()
#         myHistory.getElement(randomStar).click()
#         assert myHistory.getElement(historyLocators.STAR_MENU_BTN).get_attribute("value") == randomValue

#         myHistory.getElement(historyLocators.SUBMIT_REVIEW_BTN).click()
#         time.sleep(2)
#         assert myHistory.getElement(historyLocators.REVIEW_SUBMIT_DONE_BTN)

#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise

# # @pytest.mark.cy
# def test_history_014(createDriver: WebDriver):  ### 팀 회식 확인인
#     try:
#         myHistory = history(createDriver)
#         myHistory.goToPage("히스토리")
#         assert myHistory.getElement(historyLocators.RECOMEND_HISTORY)
#         assert myHistory.getElement(historyLocators.RECOMEND_TITLE)
#         assert myHistory.getElement(historyLocators.FIRST_MENU_IMAGE)
#         assert myHistory.getElement(historyLocators.LABEL_HANSIK) # 변경
#         assert myHistory.getElement(historyLocators.LABEL_TEAM) # 변경경
#         assert myHistory.getElement(historyLocators.MENU_HOE) # 변경
#         assert myHistory.getElement(historyLocators.AI_COMMAND)
#         assert myHistory.getElement(historyLocators.RECOMEND_HON_BTN)
    
#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise

# # @pytest.mark.cy
# def test_history_015(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("후기등록팀")
#         time.sleep(2)
#         assert myHistory.getElement(historyLocators.REVIEW_REGISTER_TITLE)
        
#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise

# def test_history_016(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("후기등록팀")
#         myHistory.getElement(historyLocators.REVIEW_X_BTN).click()
#         assert myHistory.getElement(historyLocators.RECOMEND_HISTORY)
        
        
#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise

# def test_history_018(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("후기등록팀")
#         assert myHistory.getElement(historyLocators.REVIEW_REGISTER_TITLE)
#         assert myHistory.getElement(historyLocators.MEAL_TYPE_TITLE)
#         assert myHistory.getElement(historyLocators.HONBAB_RADIO_NO_SELECTED)
#         assert myHistory.getElement(historyLocators.GROUP_RADIO_NO_SELECTED)
#         assert myHistory.getElement(historyLocators.TEAM_RADIO_SELECTED)
#         assert myHistory.getElement(historyLocators.PHOTO_TITLE)
#         assert myHistory.getElement(historyLocators.MENU_NAME_TITLE)
#         assert myHistory.getElement(historyLocators.MENU_NAME_INPUT) #변경경
#         assert myHistory.getElement(historyLocators.CATEGORY_TITLE)
#         assert myHistory.getElement(historyLocators.CATEGORY_DROPDOWN)
#         assert myHistory.getElement(historyLocators.CATEGORY_SELECT_DISABLED)
#         assert myHistory.getElement(historyLocators.REVIEW_CONTENT_TITLE)
#         assert myHistory.getElement(historyLocators.REVIEW_TEXTAREA)
#         assert myHistory.getElement(historyLocators.RATING_TITLE)
#         assert myHistory.getElement(historyLocators.STAR1)
#         assert myHistory.getElement(historyLocators.STAR2)
#         assert myHistory.getElement(historyLocators.STAR3)
#         assert myHistory.getElement(historyLocators.STAR4)
#         assert myHistory.getElement(historyLocators.STAR5)
        
#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise

# def test_history_019(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("후기등록팀")
#         myHistory.getElement(historyLocators.SUBMIT_REVIEW_BTN).click()
#         assert myHistory.getElement(historyLocators.REVIEW_IMAGE_REQUIRED)
#         assert myHistory.getElement(historyLocators.REVIEW_TEXT_REQUIRED)
#         assert myHistory.getElement(historyLocators.STAR_REQUIRED)
        
#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise
    
# # @pytest.mark.cy
# def test_history_020(createDriver: WebDriver): 
#     try:
#         myHistory = history(createDriver) 
#         myHistory.goToPage("후기등록팀")
        
#         assert myHistory.screenDiff(historyLocators.REVIEW_IMG_INPUT, inspect.currentframe().f_code.co_name, "reviewImg", "image", myHistory.getRandomImage())
        
#         randomReview = myHistory.getRandomReview()
#         myHistory.getElement(historyLocators.REVIEW_TEXTAREA).send_keys(randomReview)
#         assert myHistory.getElement(historyLocators.REVIEW_TEXTAREA).get_attribute("value") == randomReview

#         randomValue, randomStar = myHistory.getRandomStar()
#         myHistory.getElement(randomStar).click()
#         assert myHistory.getElement(historyLocators.STAR_MENU_BTN).get_attribute("value") == randomValue

#         myHistory.getElement(historyLocators.SUBMIT_REVIEW_BTN).click()
#         time.sleep(2)
#         assert myHistory.getElement(historyLocators.REVIEW_SUBMIT_DONE_BTN)

#         myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
#         raise
