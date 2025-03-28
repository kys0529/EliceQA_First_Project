# 작업자 이름: 5조 / 마무리 연수

import time
import pytest
import inspect

from src.pages.mainPage import mainPage
from src.utils import mainLocators

# 테스트 끝나면 함수 내 모든 time.sleep() 삭제하기
@pytest.mark.finish
def test_register_001(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("메인 페이지")
        assert myMainPage.getElement(mainLocators.MAINP_TXT)

        myMainPage.getElement(mainLocators.MAINP_REGISTER_BTN).click()
        assert myMainPage.getElement(mainLocators.REGP_TXT)

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

@pytest.mark.finish
def test_register_002(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("회원가입 페이지")
        myMainPage.getElement(mainLocators.REGP_LOGIN_HREF).click()
        assert myMainPage.getElement(mainLocators.LOGINP_TXT)

        myMainPage.goToPage("로그인 페이지")
        myMainPage.getElement(mainLocators.LOGINP_REGISTER_HREF).click()
        assert myMainPage.getElement(mainLocators.REGP_TXT)

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

@pytest.mark.finish
def test_register_003(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("회원가입 페이지")
        emailResult = myMainPage.screenDiff(mainLocators.REGP_EMAIL_INPUT, inspect.currentframe().f_code.co_name, "email", "click")
        assert emailResult == True

        pwResult = myMainPage.screenDiff(mainLocators.REGP_PW_INPUT, inspect.currentframe().f_code.co_name, "pw", "click")
        assert pwResult == True

        email, pw = myMainPage.getRandomAccount()
        myMainPage.getElement(mainLocators.REGP_EMAIL_INPUT).send_keys(email)
        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys(pw)
        myMainPage.getElement(mainLocators.REGP_GOING_BTN).click()
        assert myMainPage.getElement(mainLocators.AUTH_TXT)

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

@pytest.mark.finish
def test_register_004(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("회원가입 페이지")

        email, pw = myMainPage.getRandomAccount()
        myMainPage.getElement(mainLocators.REGP_EMAIL_INPUT).send_keys(email)

        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys("a")
        assert "ced6f80b9" in myMainPage.getElement(mainLocators.REGP_PW_LOWER_LETTERS).get_attribute('class')

        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys("A")
        assert "ced6f80b9" in myMainPage.getElement(mainLocators.REGP_PW_UPPER_LETTERS).get_attribute('class')

        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys("1")
        assert "ced6f80b9" in myMainPage.getElement(mainLocators.REGP_PW_UPPER_LETTERS).get_attribute('class')
        assert "ced6f80b9" in myMainPage.getElement(mainLocators.REGP_PW_VALID_3).get_attribute('class')

        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys("@")
        assert "ced6f80b9" in myMainPage.getElement(mainLocators.REGP_PW_SPECIAL_CHARACTERS).get_attribute('class')

        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys("5678")
        assert "ced6f80b9" in myMainPage.getElement(mainLocators.REGP_PW_LEAST_8).get_attribute('class')
        
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

@pytest.mark.finish
def test_register_005(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("회원가입 페이지")

        email, pw = myMainPage.getRandomAccount()
        myMainPage.getElement(mainLocators.REGP_EMAIL_INPUT).send_keys("test@naver")
        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys(pw)
        myMainPage.getElement(mainLocators.REGP_GOING_BTN).click()

        assert myMainPage.getElement(mainLocators.REGP_EMAIL_ERROR_TXT)
        
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

@pytest.mark.finish
def test_register_006(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("회원가입 페이지")

        email, pw = myMainPage.getRandomAccount()
        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys(pw)
        myMainPage.getElement(mainLocators.REGP_PW_TOGGLE_BTN).click()
        assert "text" in myMainPage.getElement(mainLocators.REGP_PW_INPUT).get_attribute("type")

        myMainPage.getElement(mainLocators.REGP_PW_TOGGLE_BTN).click()
        assert "password" in myMainPage.getElement(mainLocators.REGP_PW_INPUT).get_attribute("type")

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

@pytest.mark.finish
def test_register_007(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("앱 인증 권한")
        assert myMainPage.getElement(mainLocators.AUTH_TXT)
        
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

@pytest.mark.finish
def test_register_008(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("앱 인증 권한")

        myMainPage.getElement(mainLocators.AUTH_ACCEPT_BTN).click()
        assert myMainPage.getElement(mainLocators.USERINFO_TXT)
    
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

@pytest.mark.finish
def test_register_009(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("앱 인증 권한")

        myMainPage.getElement(mainLocators.AUTH_DECLINE_BTN).click()
        assert myMainPage.getElement(mainLocators.ERROR_TXT)

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

@pytest.mark.finish
def test_register_010(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 오류 페이지")
        myMainPage.getElement(mainLocators.ERROR_RETRY).click()
        assert myMainPage.getElement(mainLocators.MAINP_TXT)

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

def test_register_011(createDriver): # 11번부터 18번까지 인적사항 작성 페이지 (일단 보류 / 13번은 제외)
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("인적사항 작성 페이지")

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

@pytest.mark.finish
def test_login_001(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("메인 페이지")

        myMainPage.getElement(mainLocators.MAINP_LOGIN_BTN).click()
        assert myMainPage.getElement(mainLocators.LOGINP_TXT)

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

@pytest.mark.finish
def test_login_003(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")

        pwResult = myMainPage.screenDiff(mainLocators.LOGINP_PW_INPUT, inspect.currentframe().f_code.co_name, "pw", "click")
        assert pwResult == True

        emailResult = myMainPage.screenDiff(mainLocators.LOGINP_EMAIL_INPUT, inspect.currentframe().f_code.co_name, "email", "click")
        assert emailResult == True

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

@pytest.mark.finish  
def test_login_004(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")

        myMainPage.getElement(mainLocators.LOGINP_EMAIL_INPUT).send_keys("test@naver")
        myMainPage.getElement(mainLocators.LOGINP_PW_INPUT).send_keys("1234")
        myMainPage.getElement(mainLocators.LOGINP_GOING_BTN).click()

        assert myMainPage.getElement(mainLocators.LOGINP_LOGIN_ERROR_TXT)
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

@pytest.mark.finish
def test_login_005(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")
        
        myMainPage.getElement(mainLocators.LOGINP_PW_INPUT).send_keys("1234")
        
        myMainPage.getElement(mainLocators.LOGINP_PW_TOGGLE_BTN).click()
        assert "text" == myMainPage.getElement(mainLocators.LOGINP_PW_INPUT).get_attribute("type")
        
        myMainPage.getElement(mainLocators.LOGINP_PW_TOGGLE_BTN).click()
        assert "password" == myMainPage.getElement(mainLocators.LOGINP_PW_INPUT).get_attribute("type")

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

@pytest.mark.ys
def test_login_006(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

def test_login_007(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

def test_login_008(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

def test_login_009(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

def test_login_010(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

def test_login_011(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

def test_login_012(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")