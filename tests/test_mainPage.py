# 작업자 이름: 5조 / 마무리: 강연수

import pytest
import inspect

from src.pages.mainPage import mainPage
from src.utils import mainLocators

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
        raise

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
        raise

@pytest.mark.finish
def test_register_003(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("회원가입 페이지")
        emailResult = myMainPage.screenDiff(mainLocators.REGP_EMAIL_INPUT, inspect.currentframe().f_code.co_name, "email", "click")
        assert emailResult == True

        pwResult = myMainPage.screenDiff(mainLocators.REGP_PW_INPUT, inspect.currentframe().f_code.co_name, "pw", "click")
        assert pwResult == True

        myMainPage.getElement(mainLocators.REGP_EMAIL_INPUT).send_keys(myMainPage.faker.email())
        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys(myMainPage.faker.password(length=8))
        myMainPage.getElement(mainLocators.REGP_GOING_BTN).click()
        assert myMainPage.getElement(mainLocators.AUTH_TXT)

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_004(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("회원가입 페이지")

        myMainPage.getElement(mainLocators.REGP_EMAIL_INPUT).send_keys(myMainPage.faker.email())

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
        raise

@pytest.mark.finish
def test_register_005(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("회원가입 페이지")

        myMainPage.getElement(mainLocators.REGP_EMAIL_INPUT).send_keys("test@naver")
        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys(myMainPage.faker.password(length=8))
        myMainPage.getElement(mainLocators.REGP_GOING_BTN).click()

        assert myMainPage.getElement(mainLocators.REGP_EMAIL_ERROR_TXT)
        
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_006(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("회원가입 페이지")

        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys(myMainPage.faker.password(length=8))
        myMainPage.getElement(mainLocators.REGP_PW_TOGGLE_BTN).click()
        assert "text" in myMainPage.getElement(mainLocators.REGP_PW_INPUT).get_attribute("type")

        myMainPage.getElement(mainLocators.REGP_PW_TOGGLE_BTN).click()
        assert "password" in myMainPage.getElement(mainLocators.REGP_PW_INPUT).get_attribute("type")

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_007(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("앱 인증 권한")
        assert myMainPage.getElement(mainLocators.AUTH_TXT)
        
        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

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
        raise

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
        raise

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
        raise

@pytest.mark.finish
def test_register_011(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("인적사항 작성 페이지")

        myMainPage.getElement(mainLocators.USERINFO_SUBMIT_BTN).click()
        assert myMainPage.getElement(mainLocators.USERINFO_NAME_ERROR) 
        assert myMainPage.getElement(mainLocators.USERINFO_TEAM_ERROR) 
        assert myMainPage.getElements(mainLocators.USERINFO_SLIDERBAR_ERROR) 
        assert myMainPage.getElements(mainLocators.USERINFO_TEXTAREA_ERROR)

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_012(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("인적사항 작성 페이지")

        name = myMainPage.faker.name()
        myMainPage.getElement(mainLocators.USERINFO_NAME_INPUT).send_keys(name)
        assert name == myMainPage.getElement(mainLocators.USERINFO_NAME_INPUT).get_attribute("value")

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_14(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("인적사항 작성 페이지")

        myMainPage.getElement(mainLocators.USERINFO_TEAM_DROP_DOWN).click()
        myMainPage.getElement(mainLocators.USERINFO_TEAM_DEV_1).click()
        assert "개발 1팀" == myMainPage.getElement(mainLocators.USERINFO_TEAM_NAME).text

        myMainPage.getElement(mainLocators.USERINFO_TEAM_DROP_DOWN).click()
        myMainPage.getElement(mainLocators.USERINFO_TEAM_DEV_2).click()
        assert "개발 2팀" == myMainPage.getElement(mainLocators.USERINFO_TEAM_NAME).text

        myMainPage.getElement(mainLocators.USERINFO_TEAM_DROP_DOWN).click()
        myMainPage.getElement(mainLocators.USERINFO_TEAM_DESIGN_1).click()
        assert "디자인 1팀" == myMainPage.getElement(mainLocators.USERINFO_TEAM_NAME).text

        myMainPage.getElement(mainLocators.USERINFO_TEAM_DROP_DOWN).click()
        myMainPage.getElement(mainLocators.USERINFO_TEAM_DESIGN_2).click()
        assert "디자인 2팀" == myMainPage.getElement(mainLocators.USERINFO_TEAM_NAME).text

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_15(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("인적사항 작성 페이지")

        sliders = myMainPage.getElements(mainLocators.USERINFO_SLIDER)
        for slider in sliders:
            myMainPage.action.click_and_hold(slider).move_by_offset(30, 0).release().perform()
     
        myMainPage.getElement(mainLocators.USERINFO_SUBMIT_BTN).click()

        assert len(myMainPage.getElements(mainLocators.USERINFO_SLIDERBAR_ERROR)) == 3

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_16(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("인적사항 작성 페이지")

        sliders = myMainPage.getElements(mainLocators.USERINFO_SLIDER)
        for slider in sliders:
            myMainPage.action.click_and_hold(slider).move_by_offset(240, 0).release().perform()

        values = myMainPage.getElements(mainLocators.USERINFO_SLIDER_VALUE)
        for value in values:
            assert value.text == "3.0"

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_17(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("인적사항 작성 페이지")

        myMainPage.getElement(mainLocators.USERINFO_TEXTAREA_LIKE).send_keys("일이삼사오육칠팔구")
        myMainPage.getElement(mainLocators.USERINFO_TEXTAREA_HATE).send_keys("일이삼사오육칠팔구")
        myMainPage.getElement(mainLocators.USERINFO_SUBMIT_BTN).click()
        assert len(myMainPage.getElements(mainLocators.USERINFO_TEXTAREA_ERROR)) == 2

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_18(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("인적사항 작성 페이지")

        myMainPage.getElement(mainLocators.USERINFO_NAME_INPUT).send_keys(myMainPage.faker.name())
        myMainPage.getElement(mainLocators.USERINFO_TEAM_DROP_DOWN).click()
        myMainPage.getElement(myMainPage.getRandomTeam()).click()
        sliders = myMainPage.getElements(mainLocators.USERINFO_SLIDER)
        for slider in sliders:
            myMainPage.action.click_and_hold(slider).move_by_offset(240, 0).release().perform()
        myMainPage.getElement(mainLocators.USERINFO_TEXTAREA_LIKE).send_keys("피자, 치킨, 마라샹궈, 보쌈, 초밥, 과자")
        myMainPage.getElement(mainLocators.USERINFO_TEXTAREA_HATE).send_keys("생강, 미역줄기, 민초, 고수, 미더덕, 굴")
        myMainPage.getElement(mainLocators.USERINFO_SUBMIT_BTN).click()

        assert myMainPage.getElement(mainLocators.MAINP_TXT)

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

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
        raise

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
        raise

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
        raise

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
        raise

@pytest.mark.finish
def test_login_006(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")

        myMainPage.getElement(mainLocators.LOGINP_EMAIL_INPUT).send_keys(myMainPage.userInfo['id'])
        myMainPage.getElement(mainLocators.LOGINP_PW_INPUT).send_keys(myMainPage.userInfo['pw'])
        myMainPage.getElement(mainLocators.LOGINP_GOING_BTN).click()

        assert myMainPage.getElement(mainLocators.HOME_TXT)

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_login_007(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")

        myMainPage.getElement(mainLocators.LOGINP_PW_RESET_HREF).click()
        assert myMainPage.getElement(mainLocators.RESET_TXT)

        myMainPage.getElement(mainLocators.RESET_BACK_LOGIN_BTN).click()
        assert myMainPage.getElement(mainLocators.LOGINP_TXT)

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_login_009(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("비밀번호 재설정 페이지")

        myMainPage.getElement(mainLocators.RESET_EMAIL_INPUT).send_keys("test@")
        myMainPage.getElement(mainLocators.RESET_GOING_BTN).click()
        assert myMainPage.getElement(mainLocators.RESET_EMAIL_ERROR_TXT)

        myMainPage.getElement(mainLocators.RESET_EMAIL_INPUT).clear()
        myMainPage.getElement(mainLocators.RESET_EMAIL_INPUT).send_keys("test@naver.com")
        myMainPage.getElement(mainLocators.RESET_GOING_BTN).click()
        assert myMainPage.getElement(mainLocators.MAIL_TXT)

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_login_011(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("메일 확인 안내 페이지")
        myMainPage.getElement(mainLocators.MAIL_RESEND_EMAIL_BTN).click()
        assert myMainPage.getElement(mainLocators.RESET_TXT)

        myMainPage.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise