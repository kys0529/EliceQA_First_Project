# 작업자 이름: 5조 / 마무리 연수

import time
import pytest
import inspect

from src.pages.mainPage import mainPage
from src.utils import mainLocators

# 테스트 끝나면 함수 내 모든 time.sleep() 삭제하기
def test_register_001(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("메인 페이지")
        myMainPage.getElement(mainLocators.REGISTER_BTN).click()

        assert myMainPage.getElement(mainLocators.REGISTER_TXT)
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

def test_register_002(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("회원가입 페이지")
        myMainPage.getElement(mainLocators.LOGIN_HREF).click()

        assert myMainPage.getElement(mainLocators.LOGIN_TXT)

        myMainPage.goToPage("로그인 페이지")
        myMainPage.getElement(mainLocators.REGISTER_HREF).click()

        assert myMainPage.getElement(mainLocators.REGISTER_TXT)
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

def test_register_003(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("회원가입 페이지")

        result = myMainPage.screenDiff(mainLocators.REGISTER_EMAIL, inspect.currentframe().f_code.co_name, "email", "click")
        assert result == True

        result = myMainPage.screenDiff(mainLocators.REGISTER_PW, inspect.currentframe().f_code.co_name, "pw", "click")
        assert result == True

        email, pw = myMainPage.getRandomAccount()
        myMainPage.getElement(mainLocators.REGISTER_EMAIL).send_keys(email)
        myMainPage.getElement(mainLocators.REGISTER_PW).send_keys(pw)
        myMainPage.getElement(mainLocators.RE_GOING_BTN).click()

        assert myMainPage.getElement(mainLocators.AUTH_TXT)
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

def test_register_004(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("회원가입 페이지")
        time.sleep(2)

        email, pw = myMainPage.getRandomAccount()
        myMainPage.getElement(mainLocators.REGISTER_EMAIL).send_keys(email)
        time.sleep(2)

        myMainPage.getElement(mainLocators.REGISTER_PW).send_keys("a")
        print(f"디버깅 확인용: {myMainPage.getElement(mainLocators.PW_LOWER_LETTER).get_attribute('class')}")

        # 구현 덜 함

        # myMainPage.screenDiff(mainLocators.REGISTER_PW, inspect.currentframe().f_code.co_name, "lower", "send", "a")
        # myMainPage.screenDiff(mainLocators.REGISTER_PW, inspect.currentframe().f_code.co_name, "upper", "send", "A")
        # myMainPage.screenDiff(mainLocators.REGISTER_PW, inspect.currentframe().f_code.co_name, "number", "send", "1")
        # myMainPage.screenDiff(mainLocators.REGISTER_PW, inspect.currentframe().f_code.co_name, "special", "send", "@")
        # myMainPage.screenDiff(mainLocators.REGISTER_PW, inspect.currentframe().f_code.co_name, "length", "send", "1234")
        
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

# # 확인불가 삭제예정
# @pytest.mark.dy
# # 터미널 실행문: python -m pytest -m "dy"   
# def test_register_022(createDriver):
#     try: 
#         myMainPage = mainPage(createDriver) # 이 코드는 내부적으로 이렇게 동작함 mainPage.__init__(myMainPage, createDriver)
#         myMainPage.goToPage("로그인 페이지")
#         result = myMainPage.screenDiff(mainLocators.ID_INPUT, inspect.currentframe().f_code.co_name, "email", "click")
        
#         assert result == True
#         myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

@pytest.mark.dy
def test_register_023(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")
        result = myMainPage.screenDiff(mainLocators.PW_INPUT, inspect.currentframe().f_code.co_name, "pw", "click")

        assert result == True
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")   

# 터미널 실행문: python -m pytest -m "sh"
def test_register_024(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")
        myMainPage.getElement(mainLocators.PW_INPUT).send_keys("a")
        assert "password" == myMainPage.getElement(mainLocators.PW_INPUT).get_attribute("type")
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

# 터미널 실행문: python -m pytest -m "cy"
def test_register_025(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")     
        
        myMainPage.getElement(mainLocators.PW_INPUT).send_keys("aA1@1234")
        
        myMainPage.getElement(mainLocators.PW_TOGGLE_BTN).click()
        assert "text" in myMainPage.getElement(mainLocators.PW_INPUT).get_attribute("type")
        myMainPage.getElement(mainLocators.PW_TOGGLE_BTN).click()
        assert "password" in myMainPage.getElement(mainLocators.PW_INPUT).get_attribute("type")
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")    

def test_register_026(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")     
        
        myMainPage.getElement(mainLocators.ID_INPUT).send_keys(myMainPage.userInfo['id'])
        myMainPage.getElement(mainLocators.PW_INPUT).send_keys(myMainPage.userInfo['pw'])
        myMainPage.getElement(mainLocators.GOING_BTN).click()
                
        assert "https://kdt-pt-1-pj-2-team03.elicecoding.com/" in myMainPage.driver.current_url
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

def test_register_027(createDriver): 
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")  
        myMainPage.getElement(mainLocators.PW_RESET).click() # 비밀번호를 잊으셨나요?
        time.sleep(2)
        
        assert myMainPage.getElement(mainLocators.PW_FORGET)
        
        myMainPage.getElement(mainLocators.PW_BACK_LOGIN).click() # 로그인 화면으로 돌아가기
        time.sleep(2)

        assert myMainPage.getElement(mainLocators.REGISTER_TXT)
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

def test_register_029(createDriver): 
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")
        myMainPage.getElement(mainLocators.PW_RESET).click()
        result = myMainPage.screenDiff(mainLocators.ID_INPUT, inspect.currentframe().f_code.co_name, "email", "click")
        
        assert result == True
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")

def test_register_030(createDriver):
    try:
        myMainPage = mainPage(createDriver)
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        
def test_register_032(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("비밀번호 재설정 페이지")
        myMainPage.getElement(mainLocators.REGISTER_EMAIL).send_keys("patrick_chae@naver.com")
        time.sleep(2)
        myMainPage.getElement(mainLocators.RESET_GOING_BUTTON).click()
        time.sleep(2)
        myMainPage.getElement(mainLocators.RESEND_EMAIL_BTN).click()
        time.sleep(2)

        assert myMainPage.getElement(mainLocators.RESET_GOING_BUTTON)
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")


