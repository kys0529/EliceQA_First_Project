# 작업자 이름: 5조 / 마무리: 강연수

import time
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
        myMainPage.logger.info("▶️ register_001 - 메인 페이지 이동 확인")

        myMainPage.getElement(mainLocators.MAINP_REGISTER_BTN).click()
        assert myMainPage.getElement(mainLocators.REGP_TXT)
        myMainPage.logger.info("▶️ register_002 - [회원가입] 버튼 클릭 시 회원가입 페이지 이동 확인")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_002(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("회원가입 페이지")
        myMainPage.getElement(mainLocators.REGP_LOGIN_HREF).click()
        assert myMainPage.getElement(mainLocators.LOGINP_TXT)
        myMainPage.logger.info("▶️ register_003 - 회원가입 페이지 내 [로그인] 하이퍼링크 확인")

        myMainPage.goToPage("로그인 페이지")
        myMainPage.getElement(mainLocators.LOGINP_REGISTER_HREF).click()
        assert myMainPage.getElement(mainLocators.REGP_TXT)
        myMainPage.logger.info("▶️ register_004 - 로그인 페이지 내 [회원가입] 하이퍼링크 확인")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_003(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("회원가입 페이지")
        emailResult = myMainPage.screenDiff(mainLocators.REGP_EMAIL_INPUT, inspect.currentframe().f_code.co_name, "email", "click")
        assert emailResult == True
        myMainPage.logger.info("▶️ register_006 - '이메일 주소' 필드 클릭 확인")
        myMainPage.logger.info("▶️ register_007 - '이메일 주소' 필드 입력 시 사용자 입력 정상 반영 확인")

        pwResult = myMainPage.screenDiff(mainLocators.REGP_PW_INPUT, inspect.currentframe().f_code.co_name, "pw", "click")
        assert pwResult == True
        myMainPage.logger.info("▶️ register_008 - '비밀번호' 필드 클릭 확인")
        myMainPage.logger.info("▶️ register_009 - '비밀번호' 필드 입력 시 사용자 입력 정상 반영 확인")

        myMainPage.getElement(mainLocators.REGP_EMAIL_INPUT).send_keys(myMainPage.faker.email())
        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys(myMainPage.faker.password(length=8))
        myMainPage.getElement(mainLocators.REGP_GOING_BTN).click()
        assert myMainPage.getElement(mainLocators.AUTH_TXT)
        myMainPage.logger.info("▶️ register_010 - [계속하기] 버튼 클릭 시 OAuth 인증 페이지 이동 확인")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_004(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("회원가입 페이지")

        myMainPage.getElement(mainLocators.REGP_EMAIL_INPUT).send_keys(myMainPage.faker.email())

        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys("a")
        assert "ced6f80b9" in myMainPage.getElement(mainLocators.REGP_PW_LOWER_LETTERS).get_attribute('class')
        myMainPage.logger.info("▶️ register_013 - '비밀번호' 소문자 유효성 검사 확인")

        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys("A")
        assert "ced6f80b9" in myMainPage.getElement(mainLocators.REGP_PW_UPPER_LETTERS).get_attribute('class')
        myMainPage.logger.info("▶️ register_014 - '비밀번호' 대문자 유효성 검사 확인")

        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys("1")
        assert "ced6f80b9" in myMainPage.getElement(mainLocators.REGP_PW_UPPER_LETTERS).get_attribute('class')
        assert "ced6f80b9" in myMainPage.getElement(mainLocators.REGP_PW_VALID_3).get_attribute('class')
        myMainPage.logger.info("▶️ register_015 - '비밀번호' 숫자 및 유효성 검사 최소 3개 만족 확인")

        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys("@")
        assert "ced6f80b9" in myMainPage.getElement(mainLocators.REGP_PW_SPECIAL_CHARACTERS).get_attribute('class')
        myMainPage.logger.info("▶️ register_016 - '비밀번호' 특수문자 유효성 검사 확인")

        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys("5678")
        assert "ced6f80b9" in myMainPage.getElement(mainLocators.REGP_PW_LEAST_8).get_attribute('class')
        myMainPage.logger.info("▶️ register_017 - '비밀번호' 길이 최소 8자리 유효성 검사 확인")
        
        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
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
        myMainPage.logger.info("▶️ register_018 - 이메일 에러 문구 노출 확인")
        
        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_006(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("회원가입 페이지")

        myMainPage.getElement(mainLocators.REGP_PW_INPUT).send_keys(myMainPage.faker.password(length=8))
        myMainPage.getElement(mainLocators.REGP_PW_TOGGLE_BTN).click()
        time.sleep(1)
        assert "text" in myMainPage.getElement(mainLocators.REGP_PW_INPUT).get_attribute("type")
        myMainPage.logger.info("▶️ register_019 - 비밀번호 표시 아이콘 확인")

        myMainPage.getElement(mainLocators.REGP_PW_TOGGLE_BTN).click()
        time.sleep(1)
        assert "password" in myMainPage.getElement(mainLocators.REGP_PW_INPUT).get_attribute("type")
        myMainPage.logger.info("▶️ register_020 - 비밀번호 숨기기 아이콘 확인")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_007(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("앱 인증 권한")
        assert myMainPage.getElement(mainLocators.AUTH_TXT)
        myMainPage.logger.info("▶️ register_021 - OAuth 인증 페이지 이동 확인")
        
        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_008(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("앱 인증 권한")

        myMainPage.getElement(mainLocators.AUTH_ACCEPT_BTN).click()
        assert myMainPage.getElement(mainLocators.USERINFO_TXT)
        myMainPage.logger.info("▶️ register_023 - [Accept] 버튼 클릭 시 인적사항 페이지 이동 확인")
    
        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_009(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("앱 인증 권한")

        myMainPage.getElement(mainLocators.AUTH_DECLINE_BTN).click()
        assert myMainPage.getElement(mainLocators.ERROR_TXT)
        myMainPage.logger.info("▶️ register_024 - [Decline] 버튼 클릭 시 로그인 오류 페이지 이동 확인")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_010(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 오류 페이지")
        myMainPage.getElement(mainLocators.ERROR_RETRY).click()
        assert myMainPage.getElement(mainLocators.MAINP_TXT)
        myMainPage.logger.info("▶️ register_026 - [다시 시도하기] 버튼 클릭 시 메인 페이지 이동 확인")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
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
        myMainPage.logger.info("▶️ register_027 - 아무것도 입력하지 않고 [제출하기] 버튼 클릭 시 에러 문구 노출")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_012(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("인적사항 작성 페이지")

        name = myMainPage.faker.name()
        myMainPage.getElement(mainLocators.USERINFO_NAME_INPUT).send_keys(name)
        assert name == myMainPage.getElement(mainLocators.USERINFO_NAME_INPUT).get_attribute("value")
        myMainPage.logger.info("▶️ register_028 - '이름' 필드 클릭 시 포커스 확인")
        myMainPage.logger.info("▶️ register_029 - '이름' 필드 입력 시 사용자 입력 정상 반영 확인")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_14(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("인적사항 작성 페이지")

        myMainPage.getElement(mainLocators.USERINFO_TEAM_DROP_DOWN).click()
        myMainPage.logger.info("▶️ register_031 - '팀 선택' 클릭 시 드롭다운 노출 확인")

        myMainPage.getElement(mainLocators.USERINFO_TEAM_DEV_1).click()
        assert "개발 1팀" == myMainPage.getElement(mainLocators.USERINFO_TEAM_NAME).text
        myMainPage.logger.info("▶️ register_032 - '개발 1팀' 선택 확인")

        myMainPage.getElement(mainLocators.USERINFO_TEAM_DROP_DOWN).click()
        myMainPage.getElement(mainLocators.USERINFO_TEAM_DEV_2).click()
        assert "개발 2팀" == myMainPage.getElement(mainLocators.USERINFO_TEAM_NAME).text
        myMainPage.logger.info("▶️ register_033 - '개발 2팀' 선택 확인")

        myMainPage.getElement(mainLocators.USERINFO_TEAM_DROP_DOWN).click()
        myMainPage.getElement(mainLocators.USERINFO_TEAM_DESIGN_1).click()
        assert "디자인 1팀" == myMainPage.getElement(mainLocators.USERINFO_TEAM_NAME).text
        myMainPage.logger.info("▶️ register_034 - '디자인 1팀' 선택 확인")

        myMainPage.getElement(mainLocators.USERINFO_TEAM_DROP_DOWN).click()
        myMainPage.getElement(mainLocators.USERINFO_TEAM_DESIGN_2).click()
        assert "디자인 2팀" == myMainPage.getElement(mainLocators.USERINFO_TEAM_NAME).text
        myMainPage.logger.info("▶️ register_035 - '디자인 2팀' 선택 확인")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_15(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("인적사항 작성 페이지")

        sliders = myMainPage.getElements(mainLocators.USERINFO_SLIDER)
        for slider in sliders:
            time.sleep(1) # 필수! (삭제 X)
            myMainPage.action.click_and_hold(slider).move_by_offset(-500, 0).release().perform()
            time.sleep(1) # 필수! (삭제 X)
            myMainPage.action.click_and_hold(slider).move_by_offset(30, 0).release().perform()
     
        myMainPage.getElement(mainLocators.USERINFO_SUBMIT_BTN).click()

        assert len(myMainPage.getElements(mainLocators.USERINFO_SLIDERBAR_ERROR)) == 3
        myMainPage.logger.info("▶️ register_036 - 음식 성향 슬라이드 바 1.0 미만 시 에러 문구 노출 확인")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_register_16(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("인적사항 작성 페이지")

        sliders = myMainPage.getElements(mainLocators.USERINFO_SLIDER)
        for slider in sliders:
            time.sleep(1) # 필수! (삭제 X)
            myMainPage.action.click_and_hold(slider).move_by_offset(-500, 0).release().perform()
            time.sleep(1) # 필수! (삭제 X)
            myMainPage.action.click_and_hold(slider).move_by_offset(240, 0).release().perform()

        func = 37
        values = myMainPage.getElements(mainLocators.USERINFO_SLIDER_VALUE)
        for value in values:
            assert value.text == "3.0"
            myMainPage.logger.info(f"▶️ register_0{func} - 음식 성향 슬라이드 바 3.0 노출 확인")
            func = func + 1

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
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
        myMainPage.logger.info("▶️ register_040 - 좋아하는 음식 텍스트 10자 미만 입력 시 에러 문구 노출 확인")
        myMainPage.logger.info("▶️ register_042 - 싫어하는 음식 텍스트 10자 미만 입력 시 에러 문구 노출 확인")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.ys
def test_register_18(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("인적사항 작성 페이지")

        myMainPage.getElement(mainLocators.USERINFO_NAME_INPUT).send_keys(myMainPage.faker.name())
        myMainPage.getElement(mainLocators.USERINFO_TEAM_DROP_DOWN).click()
        myMainPage.getElement(myMainPage.getRandomTeam()).click()
        sliders = myMainPage.getElements(mainLocators.USERINFO_SLIDER)
        for slider in sliders:
            time.sleep(1) # 필수! (삭제 X)
            myMainPage.action.click_and_hold(slider).move_by_offset(240, 0).release().perform()
        myMainPage.getElement(mainLocators.USERINFO_TEXTAREA_LIKE).send_keys("피자, 치킨, 마라샹궈, 보쌈, 초밥, 과자")
        myMainPage.getElement(mainLocators.USERINFO_TEXTAREA_HATE).send_keys("생강, 미역줄기, 민초, 고수, 미더덕, 굴")
        myMainPage.getElement(mainLocators.USERINFO_SUBMIT_BTN).click()

        assert myMainPage.getElement(mainLocators.HOME_TXT)
        myMainPage.logger.info("▶️ register_044 - 인적사항 유효성 조건 모두 충족 후 [제출하기] 버튼 클릭 시 메인 페이지 이동 확인")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_login_001(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("메인 페이지")

        myMainPage.getElement(mainLocators.MAINP_LOGIN_BTN).click()
        assert myMainPage.getElement(mainLocators.LOGINP_TXT)
        myMainPage.logger.info("▶️ login_001 - [로그인] 버튼 클릭 시 로그인 페이지 이동 확인")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_login_003(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")

        pwResult = myMainPage.screenDiff(mainLocators.LOGINP_PW_INPUT, inspect.currentframe().f_code.co_name, "pw", "click")
        assert pwResult == True
        myMainPage.logger.info("▶️ login_003 - '이메일 주소' 필드 클릭 시 포커스 확인")

        emailResult = myMainPage.screenDiff(mainLocators.LOGINP_EMAIL_INPUT, inspect.currentframe().f_code.co_name, "email", "click")
        assert emailResult == True
        myMainPage.logger.info("▶️ login_004 - '비밀번호' 필드 클릭 시 포커스 확인'")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
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
        myMainPage.logger.info("▶️ login_009 - 유효하지 않은 값 입력 후 [계속하기] 버튼 클릭 시 에러 문구 노출 확인")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_login_005(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")
        
        myMainPage.getElement(mainLocators.LOGINP_PW_INPUT).send_keys("1234")
        
        myMainPage.getElement(mainLocators.LOGINP_PW_TOGGLE_BTN).click()
        assert "text" == myMainPage.getElement(mainLocators.LOGINP_PW_INPUT).get_attribute("type")
        myMainPage.logger.info("▶️ login_010 - 비밀번호 표시 아이콘 확인")
        
        myMainPage.getElement(mainLocators.LOGINP_PW_TOGGLE_BTN).click()
        assert "password" == myMainPage.getElement(mainLocators.LOGINP_PW_INPUT).get_attribute("type")
        myMainPage.logger.info("▶️ login_011 - 비밀번호 숨기기 아이콘 확인")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
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
        myMainPage.logger.info("▶️ login_012 - 로그인 성공 시 홈 탭 이동 확인")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_login_007(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("로그인 페이지")

        myMainPage.getElement(mainLocators.LOGINP_PW_RESET_HREF).click()
        assert myMainPage.getElement(mainLocators.RESET_TXT)
        myMainPage.logger.info("▶️ login_013 - 로그인 페이지 내 [비밀번호를 잊으셨나요?] 하이퍼링크 확인")

        myMainPage.getElement(mainLocators.RESET_BACK_LOGIN_BTN).click()
        assert myMainPage.getElement(mainLocators.LOGINP_TXT)
        myMainPage.logger.info("▶️ login_014 - 로그인 페이지 내 [로그인 화면으로 돌아가기] 하이퍼링크 확인")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_login_009(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("비밀번호 재설정 페이지")

        myMainPage.getElement(mainLocators.RESET_EMAIL_INPUT).send_keys("test@")
        myMainPage.getElement(mainLocators.RESET_GOING_BTN).click()
        assert myMainPage.getElement(mainLocators.RESET_EMAIL_ERROR_TXT)
        myMainPage.logger.info("▶️ login_017 - 유효하지 않은 이메일 입력 후 [계속] 버튼 클릭 시 에러 문구 노출 확인")

        myMainPage.getElement(mainLocators.RESET_EMAIL_INPUT).clear()
        myMainPage.getElement(mainLocators.RESET_EMAIL_INPUT).send_keys("test@naver.com")
        myMainPage.getElement(mainLocators.RESET_GOING_BTN).click()
        assert myMainPage.getElement(mainLocators.MAIL_TXT)
        myMainPage.logger.info("▶️ login_018 - 유효한 이메일 입력 후 [계속] 버튼 클릭 시 메일 확인 안내 페이지 이동 확인")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_login_011(createDriver):
    try:
        myMainPage = mainPage(createDriver)
        myMainPage.goToPage("메일 확인 안내 페이지")
        myMainPage.getElement(mainLocators.MAIL_RESEND_EMAIL_BTN).click()
        assert myMainPage.getElement(mainLocators.RESET_TXT)
        myMainPage.logger.info("▶️ login_020 - [Resend email] 버튼 클릭 시 비밀번호 재설정 페이지 이동 확인]")

        myMainPage.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myMainPage.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise