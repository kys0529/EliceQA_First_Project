# 작업자 이름: 채승호

import time
import pytest
import inspect
from selenium.webdriver.chrome.webdriver import WebDriver
from src.pages.teamFeed import teamFeed
from src.utils import teamFeedLocators
from faker import Faker
from PIL import Image, ImageChops
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.sh
def test_teamFeed_001(createDriver: WebDriver):  # 팀 피드 진입
    try:
        myTeamFeed = teamFeed(createDriver)
        myTeamFeed.goToPage("팀 피드")
        myTeamFeed.logger.info("▶️ team_feed_001 - 팀 피드 페이지 정상 노출")
        myTeamFeed.logger.info("▶️ team_feed_002 - 다른 팀은 어떤 메뉴를 먹었을까요? 문구 확인")
        myTeamFeed.logger.info("▶️ team_feed_003 - 현재 로그인 계정팀이 기본 선택인지 확인")
        
        assert myTeamFeed.getElement(teamFeedLocators.TEAM_FEED_TXT).is_displayed()
        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise
    

@pytest.mark.finish
def test_teamFeed_002(createDriver: WebDriver):
    try:
        myTeamFeed = teamFeed(createDriver) #드롭박스 선택
        myTeamFeed.goToPage("팀 피드")
        myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DROP_DOWN).click()
        myTeamFeed.logger.info("▶️ team_feed_004 - 드롭박스 클릭")
        assert myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DROP_DOWN).is_displayed()
        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise
    

@pytest.mark.finish
def test_teamFeed_003(createDriver: WebDriver):
    try:
        myTeamFeed = teamFeed(createDriver) # 드롭박스 개발 1팀 선택
        myTeamFeed.goToPage("팀 피드")
        myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DROP_DOWN).click()
        myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DEV_1).click()  # 개발 1팀
        myTeamFeed.logger.info("▶️ team_feed_005 - 개발 1팀 선택됨")
        assert myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DROP_DOWN).is_displayed()
        
        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise
   

@pytest.mark.finish
def test_teamFeed_004(createDriver: WebDriver):
    try:
        myTeamFeed = teamFeed(createDriver) # 드롭박스 개발 2팀 선택
        myTeamFeed.goToPage("팀 피드")
        myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DROP_DOWN).click()
        myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DEV_2).click()  # 개발 2팀
        myTeamFeed.logger.info("▶️ team_feed_028 - 개발 2팀 선택됨")
        assert myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DROP_DOWN).is_displayed()
        
        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_teamFeed_005(createDriver: WebDriver):
    try:
        myTeamFeed = teamFeed(createDriver) # 드롭박스 디자인 1팀 선택
        myTeamFeed.goToPage("팀 피드")
        myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DROP_DOWN).click()
        myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DESIGN_1).click()  # 디자인 1팀
        myTeamFeed.logger.info("▶️ team_feed_035 - 디자인 1팀 선택됨")
        assert myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DROP_DOWN).is_displayed()
        
        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_teamFeed_006(createDriver: WebDriver):
    try:
        myTeamFeed = teamFeed(createDriver) # 드롭박스 디자인 2팀 선택
        myTeamFeed.goToPage("팀 피드")
        myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DROP_DOWN).click()
        myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DESIGN_2).click()  # 디자인 2팀
        myTeamFeed.logger.info("▶️ team_feed_042 - 디자인 2팀 선택됨")
        assert myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DROP_DOWN).is_displayed()
        
        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise


@pytest.mark.finish
def test_teamFeed_007(createDriver: WebDriver):
    try:
        myTeamFeed = teamFeed(createDriver)
        myTeamFeed.goToPage("팀 피드")
        myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click()  # 프로필 수정 팝업 진입
        myTeamFeed.logger.info("▶️ team_feed_007 - 프로필 수정 팝업 진입")
        
        assert myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE_SVG).is_displayed()
        
        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise




# # @pytest.mark.sh
# def test_teamFeed_008(createDriver: WebDriver):
#     try:
#         myTeamFeed = teamFeed(createDriver) # 슬라이드 바 유효하지 않은 값 테스트
#         myTeamFeed.goToPage("프로필 수정")

#         sliders = myTeamFeed.getElements(teamFeedLocators.TEAM_PROFILE_SLIDER)
#         for slider in sliders:
#               # 필수! (삭제 X)
#             myTeamFeed.action.click_and_hold(slider).move_by_offset(30, 0).release().perform()
#             myTeamFeed.logger.info("▶️ team_feed_008 - '슬라이드 바 움직이며 선택된 값 노출")
#             myTeamFeed.logger.info("▶️ team_feed_010 - '슬라이드 바 움직이며 선택된 값 노출")
#             myTeamFeed.logger.info("▶️ team_feed_012 - '슬라이드 바 움직이며 선택된 값 노출")
#         myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE_COMPLETE_BTN).click()
#         myTeamFeed.logger.info("▶️ team_feed_009 - '맛에 대한 성향은 최소 1 이상 설정해주세요' 문구 노출")
#         myTeamFeed.logger.info("▶️ team_feed_011 - '맛에 대한 성향은 최소 1 이상 설정해주세요' 문구 노출")
#         myTeamFeed.logger.info("▶️ team_feed_013 - '맛에 대한 성향은 최소 1 이상 설정해주세요' 문구 노출")
#         assert myTeamFeed.getElements(teamFeedLocators.TEAM_PROFILE_SLIDERBAR_ERROR)

#         myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
#         raise


@pytest.mark.finish
def test_teamFeed_009(createDriver: WebDriver): # 프로필 수정 팝업 닫기 버튼 클릭
    try:
        myTeamFeed = teamFeed(createDriver)
        myTeamFeed.goToPage("팀 피드")
        myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click()
        myTeamFeed.getElement(teamFeedLocators.CLOSE_BUTTON).click() 
        myTeamFeed.logger.info("▶️ team_feed_006 - 화면 꺼지고 팀 피드 창 복귀")
        assert myTeamFeed.getElement(teamFeedLocators.TEAM_FEED_TXT).is_displayed()
        
        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_teamFeed_010(createDriver: WebDriver):  # 이런 음식은 좋아요! 텍스트 박스 10자 미만 텍스트 입력
    try:
        myTeamFeed = teamFeed(createDriver)
        myTeamFeed.goToPage("팀 피드")
        myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click()
        myTeamFeed.getElement(teamFeedLocators.TEXTAREA_LIKE).clear()
        myTeamFeed.logger.info("▶️ team_feed_014 - '좋아하는 음식 성향을 이야기해주세요' 문구 노출")
        myTeamFeed.getElement(teamFeedLocators.TEXTAREA_LIKE).send_keys("다 좋아요")  # 10자 미만 텍스트 입력
        myTeamFeed.getElement(teamFeedLocators.PROFILE_CHANGE_BTN).click()
        myTeamFeed.logger.info("▶️ team_feed_015 - '10자 이상 입력해주세요' 문구 노출")
        assert myTeamFeed.getElement(teamFeedLocators.TEXTAREA_MINUS_ERROR)
        

        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise
   

@pytest.mark.finish
def test_teamFeed_011(createDriver: WebDriver): # 이런 음식은 좋아요! 텍스트 박스 100자 이상 텍스트 입력
    try:
        myTeamFeed = teamFeed(createDriver) 
        myTeamFeed.goToPage("팀 피드")
        myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click()
        myTeamFeed.getElement(teamFeedLocators.TEXTAREA_LIKE).clear()
        myTeamFeed.getElement(teamFeedLocators.TEXTAREA_LIKE).send_keys(
            "매콤하면서도 깊은 감칠맛이 있는 음식은 좋아요! 특히 고추장 베이스의 한식이나 향신료가 풍부한 태국 요리는 식욕을 돋우는 맛의 조화가 완벽해서 자주 찾게 됩니다. 신선한 해산물이 들어간 요리도 좋아하는데, 바다의 깊은 맛이 입안에 퍼질 때의 그 만족감이 특별합니다."
        )
        myTeamFeed.getElement(teamFeedLocators.PROFILE_CHANGE_BTN).click()
        myTeamFeed.logger.info("▶️ team_feed_016 - '100자 이내 입력해주세요' 문구 노출")
        assert myTeamFeed.getElement(teamFeedLocators.TEXTAREA_PLUS_ERROR)
        
        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise


@pytest.mark.finish
def test_teamFeed_012(createDriver: WebDriver):  
    try:
        myTeamFeed = teamFeed(createDriver) # 이런 음식은 싫어요! 텍스트 박스 10자 미만 텍스트 입력
        myTeamFeed.goToPage("팀 피드")
        myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click()
        myTeamFeed.getElement(teamFeedLocators.TEXTAREA_HATE).clear()
        myTeamFeed.logger.info("▶️ team_feed_017 - '좋아하는 음식 성향을 이야기해주세요' 문구 노출")
        myTeamFeed.getElement(teamFeedLocators.TEXTAREA_HATE).send_keys("다 싫어요")  # 10자 미만 텍스트 입력
        myTeamFeed.getElement(teamFeedLocators.PROFILE_CHANGE_BTN).click()
        myTeamFeed.logger.info("▶️ team_feed_018 - '10자 이상 입력해주세요' 문구 노출")
        assert myTeamFeed.getElement(teamFeedLocators.TEXTAREA_MINUS_ERROR)
        

        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise
    

@pytest.mark.finish
def test_teamFeed_013(createDriver: WebDriver): 
    try:
        myTeamFeed = teamFeed(createDriver) # 이런 음식은 싫어요! 텍스트 박스 100자 이상 텍스트 입력
        myTeamFeed.goToPage("팀 피드")
        myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click()
        myTeamFeed.getElement(teamFeedLocators.TEXTAREA_HATE).clear()
        myTeamFeed.getElement(teamFeedLocators.TEXTAREA_HATE).send_keys(
            "비린내가 강한 해산물은 제가 정말 피하고 싶은 음식 중 하나입니다. 생선 특유의 비린 향이 코를 찌르면 식욕이 완전히 사라져 버립니다. 문어나 오징어 같은 탱글탱글한 식감의 해산물은 씹을 때마다 거부감이 들어요. 어릴 때 해산물을 먹고 심한 알레르기 반응을 경험한 후로 트라우마가 생겼습니다. 가족 모임이나 회식에서 해산물 요리가 나오면 항상 난처한 상황에 처하게 됩니다."
        )
        myTeamFeed.getElement(teamFeedLocators.PROFILE_CHANGE_BTN).click()
        myTeamFeed.logger.info("▶️ team_feed_019 - '100자 이내 입력해주세요' 문구 노출")
        assert myTeamFeed.getElement(teamFeedLocators.TEXTAREA_PLUS_ERROR)
        

        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise
    


# @pytest.mark.sh
# def test_teamFeed_014(createDriver: WebDriver):  # 유효한 수정 값
#     try:
#         myTeamFeed = teamFeed(createDriver) # 슬라이드 바 유효하지 않은 값 테스트
#         myTeamFeed.goToPage("팀 피드")
#         myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click()
#         

#         sliders = myTeamFeed.getElements(teamFeedLocators.TEAM_PROFILE_SLIDER)
#         for slider in sliders:
#               # 필수! (삭제 X)
#             myTeamFeed.action.click_and_hold(slider).move_by_offset(-30, 0).release().perform()
#             myTeamFeed.getElement(teamFeedLocators.TEXTAREA_LIKE).clear()
#             myTeamFeed.getElement(teamFeedLocators.TEXTAREA_LIKE).send_keys(
#                 "매콤하면서도 깊은 감칠맛이 있는 음식은 좋아요!"
#             )
#             myTeamFeed.getElement(teamFeedLocators.TEXTAREA_HATE).clear()
#             myTeamFeed.getElement(teamFeedLocators.TEXTAREA_HATE).send_keys(
#                 "비린내가 강한 해산물은 제가 정말 피하고 싶은 음식 중 하나입니다."
#             )

#         myTeamFeed.getElement(teamFeedLocators.PROFILE_CHANGE_BTN).click()
#         myTeamFeed.logger.info("▶️ team_feed_020 - [홈] 탭으로 이동")
#         assert (len(myTeamFeed.getElements(teamFeedLocators.TEAM_PROFILE_SLIDERBAR_ERROR))== 0)

#         myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
#     except Exception as e:
#         myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
#         raise
    
    

@pytest.mark.sh
def test_teamFeed_015(createDriver: WebDriver):  # 뒤로가기
    try:
        myTeamFeed = teamFeed(createDriver)
        myTeamFeed.goToPage("팀 피드")
        myTeamFeed.getElement(teamFeedLocators.TEAM_FEED_BACK_PAGE).click()
        assert myTeamFeed.getElement(teamFeedLocators.TEAM_FEED_TXT)
        

        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise
    

@pytest.mark.sh
def test_teamFeed_016(createDriver: WebDriver):  # 팀이 먹은 메뉴의 [+] 버튼 클릭
    try:
        myTeamFeed = teamFeed(createDriver)
        myTeamFeed.goToPage("[+] 버튼")
        myTeamFeed.logger.info("▶️ team_feed_051 - 새로운 후기 등록하기 페이지 노출")
        assert myTeamFeed.getElement(teamFeedLocators.MY_MENU_PLUS_CANCEL_SVG).is_displayed()
        
        
        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise
    

@pytest.mark.sh
def test_teamFeed_017(createDriver: WebDriver):  # 새로운 후기 등록하기 에서 닫기 버튼
    try:
        myTeamFeed = teamFeed(createDriver)
        myTeamFeed.goToPage("[+] 버튼")
        myTeamFeed.getElement(teamFeedLocators.CLOSE_BUTTON).click()
        
        myTeamFeed.logger.info("▶️ team_feed_052 - 팀 피드 페이지 노출")
        assert myTeamFeed.getElement(teamFeedLocators.TEAM_FEED_TXT).is_displayed()
        

        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise
    

@pytest.mark.sh
def test_teamFeed_018(createDriver: WebDriver):  # 새로운 후기 등록하기 에서 혼밥, 그룹, 회식 버튼 클릭
    try:
        myTeamFeed = teamFeed(createDriver)
        myTeamFeed.goToPage("[+] 버튼")
        myTeamFeed.getElement(teamFeedLocators.TEAM_PLUS_ALONE_BTN).click() #혼밥 라디오 버튼 클릭
        
        assert myTeamFeed.getElement(teamFeedLocators.TEAM_PLUS_ALONE_BTN).is_displayed()
        myTeamFeed.getElement(teamFeedLocators.TEAM_PLUS_GROUP_BTN).click() #그룹 라디오 버튼 
        myTeamFeed.logger.info("▶️ team_feed_053 - 같이 먹은 사람 등록 텍스트박스 추가로 노출")
        
        assert myTeamFeed.getElement(teamFeedLocators.TEAM_PLUS_GROUP_BTN).is_displayed()
        myTeamFeed.getElement(teamFeedLocators.TEAM_PLUS_TEAM_BTN).click()  #회식 라디오 버튼 클릭
        
        assert myTeamFeed.getElement(teamFeedLocators.TEAM_PLUS_TEAM_BTN).is_displayed()
        
        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.sh
def test_teamFeed_019(createDriver: WebDriver):  # 필수입력사항 누락
    try:
        myTeamFeed = teamFeed(createDriver)
        myTeamFeed.goToPage("[+] 버튼")
        myTeamFeed.getElement(teamFeedLocators.TEAM_PLUS_COMPLETE_BTN).click()
        assert myTeamFeed.getElement(teamFeedLocators.TEAM_MENU_IMG_ERROR).is_displayed()
        assert myTeamFeed.getElement(teamFeedLocators.TEAM_MENU_MENU_NAME_ERROR).is_displayed()   
        assert myTeamFeed.getElement(teamFeedLocators.TEAM_MENU_CATEGORY_ERROR).is_displayed()   
        assert myTeamFeed.getElement(teamFeedLocators.TEAM_MENU_REVIEW_ERROR).is_displayed()   
        assert myTeamFeed.getElement(teamFeedLocators.TEAM_MENU_STAR_ERROR).is_displayed()   
        myTeamFeed.logger.info("▶️ team_feed_059 - 이미지, 메뉴명, 카테고리, 후기, 별점 모두 필수입력 메시지 노출")
        
        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.sh
def test_teamFeed_020(createDriver: WebDriver):  # [+]버튼 메뉴 등록 유효값
    try:
        myTeamFeed = teamFeed(createDriver)
        myTeamFeed.goToPage("[+] 버튼")
        assert myTeamFeed.screenDiff(teamFeedLocators.TEAM_MENU_PLUS_IMG_INPUT,inspect.currentframe().f_code.co_name,"reviewImg","image",myTeamFeed.getRandomImage())  # 이미지 업로드

        randomMenuName = (myTeamFeed.getRandomMenuName())  # 검증이 필요하므로, 변수에 담음
        myTeamFeed.getElement(teamFeedLocators.TEAM_MENU_NAME).send_keys(randomMenuName)
        assert (myTeamFeed.getElement(teamFeedLocators.TEAM_MENU_NAME).get_attribute("value") == randomMenuName)

        randomName, randomCategory = (
            myTeamFeed.getRandomCategory()
        )  # 검증이 필요하므로, 변수에 담음   카테고리 현재 작동이 안됨
        myTeamFeed.getElement(teamFeedLocators.RECOMMEND_CATEGORY_DROPDOWN).click()
        myTeamFeed.getElement(randomCategory).click()
        assert (myTeamFeed.getElement(teamFeedLocators.RECOMMEND_OPTION_LABEL).text == randomName)

        randomReview = myTeamFeed.getRandomReview()  # 검증이 필요하므로, 변수에 담음
        myTeamFeed.getElement(teamFeedLocators.MY_MENU_PLUS_REVIEW_TEXTAREA).send_keys(randomReview)
        assert (myTeamFeed.getElement(teamFeedLocators.MY_MENU_PLUS_REVIEW_TEXTAREA).get_attribute("value") == randomReview)

        randomValue, randomStar = (
            myTeamFeed.getRandomStar()
        )  # 검증이 필요하므로, 변수에 담음
        myTeamFeed.getElement(randomStar).click()
        assert (myTeamFeed.getElement(teamFeedLocators.TEAM_MENU_STAR_BTN).get_attribute("value") == randomValue)

        myTeamFeed.getElement(teamFeedLocators.TEAM_PLUS_COMPLETE_BTN).click()
        myTeamFeed.logger.info("▶️ team_feed_062 - 내가 먹은 메뉴에 노출")
        

        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise




@pytest.mark.sh
def test_teamFeed_021(createDriver: WebDriver):  # 또 먹은 후기 노출
    try:
        myTeamFeed = teamFeed(createDriver)
        myTeamFeed.goToPage("같은 메뉴 먹기")
        myTeamFeed.logger.info("▶️ team_feed_067 - 또 먹은 후기 등록하기 페이지 노출")
        assert myTeamFeed.getElement(teamFeedLocators.MY_MENU_EAT_AGAIN_CANCEL_SVG).is_displayed()
        
        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise


@pytest.mark.sh
def test_teamFeed_022(createDriver):    # 같은 메뉴 먹기 후기 등록 유효값
    try:
        myTeamFeed = teamFeed(createDriver)
        myTeamFeed.goToPage("같은 메뉴 먹기")
        myTeamFeed.getElement(teamFeedLocators.TEAM_MENU_REVIEW_TEXTAREA).clear()
        myTeamFeed.getElement(teamFeedLocators.TEAM_MENU_COMPLETE_BTN).click()
        assert myTeamFeed.getElement(teamFeedLocators.TEAM_MENU_REVIEW_ERROR)
        assert myTeamFeed.getElement(teamFeedLocators.TEAM_MENU_STAR_ERROR)

        randomReview = myTeamFeed.getRandomReview() # 검증이 필요하므로, 변수에 담음
        myTeamFeed.getElement(teamFeedLocators.TEAM_MENU_REVIEW_TEXTAREA).send_keys(randomReview)
        assert myTeamFeed.getElement(teamFeedLocators.TEAM_MENU_REVIEW_TEXTAREA).get_attribute("value") == randomReview

        randomValue, randomStar = myTeamFeed.getRandomStar() # 검증이 필요하므로, 변수에 담음
        myTeamFeed.getClickableElement(randomStar).click() 
        assert myTeamFeed.getElement(teamFeedLocators.TEAM_MENU_STAR_BTN).get_attribute("value") == randomValue

        myTeamFeed.getElement(teamFeedLocators.TEAM_MENU_COMPLETE_BTN).click()
        myTeamFeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myTeamFeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise
