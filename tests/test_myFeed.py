# 작업자 이름: 강연수

import time
import pytest
import inspect

from src.pages.myFeed import myFeed
from src.utils import myFeedLocators

@pytest.mark.finish
def test_myFeed_001(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("개인 피드")
        assert myfeed.getElement(myFeedLocators.MY_FEED_TXT)

        myfeed.getElement(myFeedLocators.MY_FEED_BACK_PAGE).click()
        assert myfeed.getElement(myFeedLocators.HOME_TXT)

        myfeed.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_myFeed_002(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("프로필 수정")

        myfeed.getElement(myFeedLocators.MY_PROFILE_CHANGE_CANCEL_SVG).click()
        assert myfeed.getElement(myFeedLocators.MY_FEED_TXT)

        myfeed.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_myFeed_003(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("프로필 수정")

        #myfeed.getElement(myFeedLocators.MY_PROFILE_IMG_CHANGE_BTN).click() : 이미지 변경 버튼 클릭시 파일 탐색기 팝업으로 테스트 방해 -> 주석 처리
        imageResult = myfeed.screenDiff(myFeedLocators.MY_PROFILE_IMG_INPUT, inspect.currentframe().f_code.co_name, "profileImageChange", "image", "profileImage.jpg")
        assert imageResult == True

        myfeed.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_myFeed_004(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("프로필 수정")
        
        sliders = myfeed.getElements(myFeedLocators.MY_PROFILE_SLIDER)
        for slider in sliders:
            myfeed.action.click_and_hold(slider).move_by_offset(-500, 0).release().perform()
     
        myfeed.getElement(myFeedLocators.MY_PROFILE_CHANGE_COMPLETE_BTN).click()
        assert len(myfeed.getElements(myFeedLocators.MY_PROFILE_SLIDERBAR_ERROR)) == 3

        myfeed.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_myFeed_005(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("프로필 수정")
        
        myfeed.getVisibilityElement(myFeedLocators.MY_PROFILE_TEXTAREA_LIKE).clear()
        myfeed.getVisibilityElement(myFeedLocators.MY_PROFILE_TEXTAREA_HATE).clear()
        myfeed.getElement(myFeedLocators.MY_PROFILE_CHANGE_COMPLETE_BTN).click()
        assert "좋아하는 음식 성향을 이야기해주세요!" == myfeed.getElement(myFeedLocators.MY_PROFILE_TEXTAREA_LIKE).get_attribute("placeholder")
        assert "싫어하는 음식 성향을 이야기해주세요!" == myfeed.getElement(myFeedLocators.MY_PROFILE_TEXTAREA_HATE).get_attribute("placeholder")

        myfeed.getElement(myFeedLocators.MY_PROFILE_TEXTAREA_LIKE).send_keys("일이삼사오육칠팔구")
        myfeed.getElement(myFeedLocators.MY_PROFILE_TEXTAREA_HATE).send_keys("일이삼사오육칠팔구")
        myfeed.getElement(myFeedLocators.MY_PROFILE_CHANGE_COMPLETE_BTN).click()
        assert len(myfeed.getElements(myFeedLocators.MY_PROFILE_TEXTAREA_ERROR)) == 2

        myfeed.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.ys
def test_myFeed_006(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("프로필 수정")
        
        # 미구현

        myfeed.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise