# 작업자 이름: 윤찬유

import pytest
import inspect
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from src.pages.history import history
from src.utils import historyLocators

# @pytest.mark.cy
def test_history_001(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("히스토리")
        assert myHistory.getElement(historyLocators.RECOMEND_HISTORY)
        assert myHistory.getElement(historyLocators.RECOMEND_TITLE)
        assert myHistory.getElement(historyLocators.FIRST_MENU_IMAGE)
        assert myHistory.getElement(historyLocators.LABEL_HANSIK)
        assert myHistory.getElement(historyLocators.LABEL_HONBAB)
        assert myHistory.getElement(historyLocators.MENU_RICECAKESOUP)
        assert myHistory.getElement(historyLocators.AI_COMMAND)
        assert myHistory.getElement(historyLocators.RECOMEND_HON_BTN)
    
        myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

# @pytest.mark.cy
def test_history_002(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("히스토리")
        
        myHistory.getElement(historyLocators.HISTORY_BACK).click()
        time.sleep(2)
        assert myHistory.getElement(historyLocators.HOME_BACK)
        
        myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise
        
# @pytest.mark.cy
def test_history_003(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록혼밥")
        time.sleep(2)
        assert myHistory.getElement(historyLocators.REVIEW_REGISTER_TITLE)
        
        myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

def test_history_004(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록혼밥")
        myHistory.getElement(historyLocators.REVIEW_X_BTN).click()
        assert myHistory.getElement(historyLocators.RECOMEND_HISTORY)
        
        
        myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

def test_history_005(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록혼밥")
        assert myHistory.getElement(historyLocators.REVIEW_REGISTER_TITLE)
        assert myHistory.getElement(historyLocators.MEAL_TYPE_TITLE)
        assert myHistory.getElement(historyLocators.HONBAB_RADIO_SELECTED)
        assert myHistory.getElement(historyLocators.GROUP_RADIO_NO_SELECTED)
        assert myHistory.getElement(historyLocators.TEAM_RADIO_NO_SELECTED)
        assert myHistory.getElement(historyLocators.PHOTO_TITLE)
        assert myHistory.getElement(historyLocators.MENU_NAME_TITLE)
        assert myHistory.getElement(historyLocators.MENU_NAME_INPUT)
        assert myHistory.getElement(historyLocators.CATEGORY_TITLE)
        assert myHistory.getElement(historyLocators.CATEGORY_DROPDOWN)
        assert myHistory.getElement(historyLocators.CATEGORY_SELECT_DISABLED)
        assert myHistory.getElement(historyLocators.REVIEW_CONTENT_TITLE)
        assert myHistory.getElement(historyLocators.REVIEW_TEXTAREA)
        assert myHistory.getElement(historyLocators.RATING_TITLE)
        assert myHistory.getElement(historyLocators.STAR1)
        assert myHistory.getElement(historyLocators.STAR2)
        assert myHistory.getElement(historyLocators.STAR3)
        assert myHistory.getElement(historyLocators.STAR4)
        assert myHistory.getElement(historyLocators.STAR5)
        
        myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

def test_history_006(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록혼밥")
        myHistory.getElement(historyLocators.SUBMIT_REVIEW_BTN).click()
        assert myHistory.getElement(historyLocators.REVIEW_IMAGE_REQUIRED)
        assert myHistory.getElement(historyLocators.REVIEW_TEXT_REQUIRED)
        assert myHistory.getElement(historyLocators.STAR_REQUIRED)
        
        myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise
    
@pytest.mark.cy
def test_history_006(createDriver: WebDriver): 
    try:
        myHistory = history(createDriver) 
        myHistory.goToPage("후기등록혼밥")
        
        assert myHistory.screenDiff(historyLocators.REVIEW_IMG_INPUT, inspect.currentframe().f_code.co_name, "reviewImg", "image", myHistory.getRandomImage())
        
        randomReview = myHistory.getRandomReview()
        myHistory.getElement(historyLocators.REVIEW_TEXTAREA).send_keys(randomReview)
        assert myHistory.getElement(historyLocators.REVIEW_TEXTAREA).get_attribute("value") == randomReview

        randomValue, randomStar = myHistory.getRandomStar()
        myHistory.getElement(randomStar).click()
        assert myHistory.getElement(historyLocators.STAR_MENU_BTN).get_attribute("value") == randomValue

        myHistory.getElement(historyLocators.SUBMIT_REVIEW_BTN).click()

        myHistory.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myHistory.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise
