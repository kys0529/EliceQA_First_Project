# 작업자 이름: 강연수

import os
import time
import pytest
import inspect

from src.pages.myFeed import myFeed
from src.utils import myFeedLocators

@pytest.mark.ys
def test_myFeed_001(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("개인 피드")

        assert myfeed.getElement(myFeedLocators.MY_FEED_TXT)
        assert myfeed.getElement(myFeedLocators.MY_PROFILE_CHANGE_SVG)
        assert myfeed.getElement(myFeedLocators.MY_PROFILE_STAT_IMG)
        assert myfeed.getElement(myFeedLocators.MY_MENU_PLUS_BTN)
        assert myfeed.getElement(myFeedLocators.MY_EAT_SAME_MENU_BTN)
        myfeed.logger.info("▶️ myfeed_001 - 개인 피드 탭 선택 시 UI 요소 확인")

        myfeed.getElement(myFeedLocators.MY_FEED_BACK_PAGE).click()
        assert myfeed.getElement(myFeedLocators.HOME_TXT)
        myfeed.logger.info("▶️ myfeed_002 - [뒤로가기] 버튼 클릭 시 이전 페이지로 이동 확인")

        myfeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_myFeed_002(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("프로필 수정")
        assert myfeed.getElement(myFeedLocators.MY_PROFILE_CHANGE_TXT)
        myfeed.logger.info("▶️ myfeed_003 - [수정하기] 버튼 클릭 시 프로필 수정 창 열림 확인")

        time.sleep(1) # 필수! (삭제 X)
        myfeed.getElement(myFeedLocators.MY_PROFILE_CHANGE_CANCEL_SVG).click()
        assert myfeed.getElement(myFeedLocators.MY_FEED_TXT)
        myfeed.logger.info("▶️ myfeed_004 - [X] 버튼 클릭 시 프로필 수정 창 닫힘 확인")

        myfeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish 
def test_myFeed_003(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("프로필 수정")

        #myfeed.getElement(myFeedLocators.MY_PROFILE_IMG_CHANGE_BTN).click() : 이미지 변경 버튼 클릭시 파일 탐색기 팝업으로 테스트 방해 -> 주석 처리
        imageResult = myfeed.screenDiff(myFeedLocators.MY_PROFILE_IMG_INPUT, inspect.currentframe().f_code.co_name, "profileImageChange", "image", "profileImage.jpg")
        assert imageResult == True
        myfeed.logger.info("▶️ myfeed_006 - 이미지 수정 정상 반영 확인")

        myfeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish 
def test_myFeed_004(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("프로필 수정")

        func = 7
        sliders = myfeed.getElements(myFeedLocators.MY_PROFILE_SLIDER)
        for slider in sliders:
            time.sleep(1) # 필수! (삭제 X)
            myfeed.action.click_and_hold(slider).move_by_offset(-500, 0).release().perform()
            if func < 10:
                myfeed.logger.info(f"▶️ myfeed_00{func} - 슬라이드 바 조절 확인")
                func = func + 2
            elif func > 10:
                myfeed.logger.info(f"▶️ myfeed_0{func} - 슬라이드 바 조절 확인")

        myfeed.getElement(myFeedLocators.MY_PROFILE_CHANGE_COMPLETE_BTN).click()
        assert len(myfeed.getElements(myFeedLocators.MY_PROFILE_SLIDERBAR_ERROR)) == 3
        myfeed.logger.info(f"▶️ myfeed_008 - 슬라이드 바 에러 문구 확인")
        myfeed.logger.info(f"▶️ myfeed_010 - 슬라이드 바 에러 문구 확인")
        myfeed.logger.info(f"▶️ myfeed_012 - 슬라이드 바 에러 문구 확인")

        myfeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish 
def test_myFeed_005(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("프로필 수정")
        
        time.sleep(1) # 필수! (삭제 X)
        myfeed.getElement(myFeedLocators.MY_PROFILE_TEXTAREA_LIKE).clear()

        myfeed.getElement(myFeedLocators.MY_PROFILE_TEXTAREA_HATE).clear()
        myfeed.getElement(myFeedLocators.MY_PROFILE_CHANGE_COMPLETE_BTN).click()
        assert "좋아하는 음식 성향을 이야기해주세요!" == myfeed.getElement(myFeedLocators.MY_PROFILE_TEXTAREA_LIKE).get_attribute("placeholder")
        myfeed.logger.info(f"▶️ myfeed_013 - 좋아하는 음식 텍스트 기본 값 확인")
        assert "싫어하는 음식 성향을 이야기해주세요!" == myfeed.getElement(myFeedLocators.MY_PROFILE_TEXTAREA_HATE).get_attribute("placeholder")
        myfeed.logger.info(f"▶️ myfeed_015 - 싫어하는 음식 텍스트 기본 값 확인")

        myfeed.getElement(myFeedLocators.MY_PROFILE_TEXTAREA_LIKE).send_keys("일이삼사오육칠팔구")
        myfeed.getElement(myFeedLocators.MY_PROFILE_TEXTAREA_HATE).send_keys("일이삼사오육칠팔구")
        myfeed.getElement(myFeedLocators.MY_PROFILE_CHANGE_COMPLETE_BTN).click()
        assert len(myfeed.getElements(myFeedLocators.MY_PROFILE_TEXTAREA_ERROR)) == 2
        myfeed.logger.info(f"▶️ myfeed_014 - 좋아하는 음식 10자 미만 입력 후 에러 문구 확인")
        myfeed.logger.info(f"▶️ myfeed_016 - 싫어하는 음식 10자 미만 입력 후 에러 문구 확인")

        myfeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish 
def test_myFeed_006(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("프로필 수정")

        imagePath = os.path.abspath(os.path.join("src/resources/assets", "profileImage.jpg"))
        myfeed.getElement(myFeedLocators.MY_PROFILE_IMG_INPUT).send_keys(imagePath)
        sliders = myfeed.getElements(myFeedLocators.MY_PROFILE_SLIDER)
        for slider in sliders:
            time.sleep(1) # 필수! (삭제 X)
            myfeed.action.click_and_hold(slider).move_by_offset(500, 0).release().perform()
        myfeed.getElement(myFeedLocators.MY_PROFILE_TEXTAREA_LIKE).clear()
        myfeed.getElement(myFeedLocators.MY_PROFILE_TEXTAREA_HATE).clear()
        myfeed.getElement(myFeedLocators.MY_PROFILE_TEXTAREA_LIKE).send_keys("피자, 치킨, 마라샹궈, 보쌈, 초밥, 과자")
        myfeed.getElement(myFeedLocators.MY_PROFILE_TEXTAREA_HATE).send_keys("생강, 미역줄기, 민초, 고수, 미더덕, 굴")
        myfeed.getElement(myFeedLocators.MY_PROFILE_CHANGE_COMPLETE_BTN).click()
        assert myfeed.getElement(myFeedLocators.MY_PROFILE_CHANGE_COMPLETE_TXT)
        myfeed.logger.info(f"▶️ myfeed_017 - 유효성 조건 충족 후 [프로필 수정 완료] 버튼 클릭 시 정상적으로 수정 반영 확인")

        myfeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish 
def test_myFeed_007(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("개인 피드")

        assert myfeed.getElement(myFeedLocators.MY_PROFILE_STAT_TXT)
        assert myfeed.getElement(myFeedLocators.MY_PROFILE_STAT_IMG)
        myfeed.logger.info(f"▶️ myfeed_019 - 내 피드 페이지에 원형 차트 노출 확인")

        myfeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_myFeed_008(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("[+] 버튼")

        assert myfeed.getElement(myFeedLocators.MY_MENU_ALONE_BTN) 
        assert myfeed.getElement(myFeedLocators.MY_MENU_GROUP_BTN)
        assert myfeed.getElement(myFeedLocators.MY_MENU_TEAM_BTN)
        assert myfeed.getElement(myFeedLocators.MY_MENU_IMG_CHANGE_BTN)
        assert myfeed.getElement(myFeedLocators.MY_MENU_MENU_NAME_INPUT)
        assert myfeed.getElement(myFeedLocators.MY_MENU_CATEGORY_BTN)
        assert myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_TEXTAREA)
        assert myfeed.getElement(myFeedLocators.MY_MENU_STAR_BTN)
        assert myfeed.getElement(myFeedLocators.MY_MENU_COMPLETE_BTN)
        myfeed.logger.info(f"▶️ myfeed_024 - [+] 버튼 클릭 시 새로운 후기 등록하기 창 열림 확인")

        time.sleep(1) # 필수! (삭제 X)
        myfeed.getElement(myFeedLocators.MY_MENU_PLUS_CANCEL_SVG).click()
        assert myfeed.getElement(myFeedLocators.MY_FEED_TXT)
        myfeed.logger.info(f"▶️ myfeed_025 - [X] 버튼 클릭 시 새로운 후기 등록하기 창 닫힘 확인")

        myfeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish 
def test_myFeed_009(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("[+] 버튼")

        time.sleep(1) # 필수! (삭제 X)
        myfeed.getElement(myFeedLocators.MY_MENU_ALONE_BTN).click()
        myfeed.getElement(myFeedLocators.MY_MENU_COMPLETE_BTN).click()
        assert myfeed.getElement(myFeedLocators.MY_MENU_IMG_ERROR)
        assert myfeed.getElement(myFeedLocators.MY_MENU_MENU_NAME_ERROR)
        assert myfeed.getElement(myFeedLocators.MY_MENU_CATEGORY_ERROR)
        assert myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_ERROR)
        assert myfeed.getElement(myFeedLocators.MY_MENU_STAR_ERROR)
        myfeed.logger.info(f"▶️ myfeed_026 - [새로운 후기 등록/혼밥] 아무것도 입력하지 않고 [후기 작성 완료] 버튼 클릭 시 에러 문구 노출 확인")

        myfeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_myFeed_010(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("개인 피드")

        beforeReviewCount = myfeed.getReviewPostCount()

        myfeed.goToPage("[+] 버튼")

        time.sleep(1) # 필수! (삭제 X)
        myfeed.getClickableElement(myFeedLocators.MY_MENU_ALONE_BTN).click()
        assert myfeed.screenDiff(myFeedLocators.MY_MENU_IMG_INPUT, inspect.currentframe().f_code.co_name, "reviewImg", "image", myfeed.getRandomImage())

        randomMenuName = myfeed.getRandomMenuName() # 검증이 필요하므로, 변수에 담음
        myfeed.getElement(myFeedLocators.MY_MENU_MENU_NAME_INPUT).send_keys(randomMenuName)
        assert myfeed.getElement(myFeedLocators.MY_MENU_MENU_NAME_INPUT).get_attribute("value") == randomMenuName

        randomName, randomCategory = myfeed.getRandomCategory() # 검증이 필요하므로, 변수에 담음  
        myfeed.getClickableElement(myFeedLocators.MY_MENU_CATEGORY_BTN).click()
        myfeed.getClickableElement(randomCategory).click()
        assert myfeed.getElement(myFeedLocators.NY_MENU_CATEGORY_TXT).text == randomName

        randomReview = myfeed.getRandomReview() # 검증이 필요하므로, 변수에 담음
        myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_TEXTAREA).send_keys(randomReview)
        assert myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_TEXTAREA).get_attribute("value") == randomReview

        randomValue, randomStar = myfeed.getRandomStar() # 검증이 필요하므로, 변수에 담음
        myfeed.getClickableElement(randomStar).click()
        assert myfeed.getElement(myFeedLocators.MY_MENU_STAR_BTN).get_attribute("value") == randomValue

        myfeed.getClickableElement(myFeedLocators.MY_MENU_COMPLETE_BTN).click()

        afterReviewCount = myfeed.getReviewPostCount()

        assert beforeReviewCount + 1 == afterReviewCount
        myfeed.logger.info(f"▶️ myfeed_027 ~ 036 - [새로운 후기 등록/혼밥] 유효성 조건을 충족 후 [후기 작성 완료] 버튼 클릭 시 정상 등록 확인")

        myfeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_myFeed_015(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("개인 피드")

        beforeReviewCount = myfeed.getReviewPostCount()

        myfeed.goToPage("같은 메뉴 먹기")

        time.sleep(1) # 필수! (삭제 X)
        myfeed.getElement(myFeedLocators.MY_MENU_EAT_AGAIN_CANCEL_SVG).click()
        assert myfeed.getElement(myFeedLocators.MY_FEED_TXT)

        myfeed.goToPage("같은 메뉴 먹기")
        time.sleep(1) # 필수! (삭제 X)
        assert myfeed.getElement(myFeedLocators.MY_MENU_ALONE_BTN).get_attribute("data-state") == "checked"
        assert myfeed.getElement(myFeedLocators.MY_MENU_MENU_NAME_INPUT).get_attribute("disabled") is not None
        assert myfeed.getElement(myFeedLocators.MY_MENU_CATEGORY_BTN).get_attribute("disabled") is not None

        myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_TEXTAREA).clear()
        myfeed.getElement(myFeedLocators.MY_MENU_COMPLETE_BTN).click()
        assert myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_ERROR)
        assert myfeed.getElement(myFeedLocators.MY_MENU_STAR_ERROR)

        randomReview = myfeed.getRandomReview() # 검증이 필요하므로, 변수에 담음
        myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_TEXTAREA).send_keys(randomReview)
        assert myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_TEXTAREA).get_attribute("value") == randomReview

        randomValue, randomStar = myfeed.getRandomStar() # 검증이 필요하므로, 변수에 담음
        myfeed.getClickableElement(randomStar).click() 
        assert myfeed.getElement(myFeedLocators.MY_MENU_STAR_BTN).get_attribute("value") == randomValue
        myfeed.logger.info(f"▶️ myfeed_063 ~ 076 - 식사 유형이 혼밥인 경우, 같은 메뉴 먹기 기능 확인")

        myfeed.getElement(myFeedLocators.MY_MENU_COMPLETE_BTN).click()

        afterReviewCount = myfeed.getReviewPostCount()

        assert beforeReviewCount + 1 == afterReviewCount
        myfeed.logger.info(f"▶️ myfeed_077 - 식사 유형이 혼밥인 경우, 같은 메뉴 먹기 정상 등록 확인")

        myfeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_myFeed_011(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("[+] 버튼")

        time.sleep(1) # 필수! (삭제 X)
        myfeed.getClickableElement(myFeedLocators.MY_MENU_GROUP_BTN).click()
        myfeed.getClickableElement(myFeedLocators.MY_MENU_COMPLETE_BTN).click()
        assert myfeed.getElement(myFeedLocators.MY_MENU_IMG_ERROR)
        assert myfeed.getElement(myFeedLocators.MY_MENU_MENU_NAME_ERROR)
        assert myfeed.getElement(myFeedLocators.MY_MENU_CATEGORY_ERROR)
        assert myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_ERROR)
        assert myfeed.getElement(myFeedLocators.MY_MENU_STAR_ERROR)
        myfeed.logger.info(f"▶️ myfeed_037 - [새로운 후기 등록/그룹] 아무것도 입력하지 않고 [후기 작성 완료] 버튼 클릭 시 에러 문구 노출 확인")

        myfeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_myFeed_012(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("개인 피드")

        beforeReviewCount = myfeed.getReviewPostCount()

        myfeed.goToPage("[+] 버튼")

        time.sleep(1) # 필수! (삭제 X)
        myfeed.getClickableElement(myFeedLocators.MY_MENU_GROUP_BTN).click()
        assert myfeed.screenDiff(myFeedLocators.MY_MENU_IMG_INPUT, inspect.currentframe().f_code.co_name, "reviewImg", "image", myfeed.getRandomImage())

        myfeed.getElement(myFeedLocators.MY_MENU_PERSON_NAME_INPUT).send_keys("김")
        myfeed.getClickableElement(myFeedLocators.MY_MENU_PERSON_NAME_SEARCH_RESULT).click()
        assert myfeed.getElements(myFeedLocators.MY_MENU_PERSON_REMOVE_SVG)

        time.sleep(1) # 필수! (삭제 X)
        myfeed.getClickableElement(myFeedLocators.MY_MENU_PERSON_REMOVE_SVG).click()
        myfeed.waitUntilNotPresent(myFeedLocators.MY_MENU_PERSON_REMOVE_SVG) # 요소가 사라지지 않으면, 예외 발생
        
        time.sleep(1) # 필수! (삭제 X)
        myfeed.getElement(myFeedLocators.MY_MENU_PERSON_NAME_INPUT).send_keys("김")
        myfeed.getClickableElement(myFeedLocators.MY_MENU_PERSON_NAME_SEARCH_RESULT).click()

        randomMenuName = myfeed.getRandomMenuName() # 검증이 필요하므로, 변수에 담음
        myfeed.getElement(myFeedLocators.MY_MENU_MENU_NAME_INPUT).send_keys(randomMenuName)
        assert myfeed.getElement(myFeedLocators.MY_MENU_MENU_NAME_INPUT).get_attribute("value") == randomMenuName

        randomName, randomCategory = myfeed.getRandomCategory() # 검증이 필요하므로, 변수에 담음
        myfeed.getClickableElement(myFeedLocators.MY_MENU_CATEGORY_BTN).click()
        myfeed.getClickableElement(randomCategory).click()
        assert myfeed.getElement(myFeedLocators.NY_MENU_CATEGORY_TXT).text == randomName

        randomReview = myfeed.getRandomReview() # 검증이 필요하므로, 변수에 담음
        myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_TEXTAREA).send_keys(randomReview)
        assert myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_TEXTAREA).get_attribute("value") == randomReview

        randomValue, randomStar = myfeed.getRandomStar() # 검증이 필요하므로, 변수에 담음
        myfeed.getClickableElement(randomStar).click()
        assert myfeed.getElement(myFeedLocators.MY_MENU_STAR_BTN).get_attribute("value") == randomValue

        myfeed.getClickableElement(myFeedLocators.MY_MENU_COMPLETE_BTN).click()

        afterReviewCount = myfeed.getReviewPostCount()

        assert beforeReviewCount + 1 == afterReviewCount
        myfeed.logger.info(f"▶️ myfeed_038 ~ 051 - [새로운 후기 등록/그룹] 유효성 조건을 충족 후 [후기 작성 완료] 버튼 클릭 시 정상 등록 확인")

        myfeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_myFeed_016(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("개인 피드")

        beforeReviewCount = myfeed.getReviewPostCount()

        myfeed.goToPage("같은 메뉴 먹기")

        time.sleep(1) # 필수! (삭제 X)
        myfeed.getElement(myFeedLocators.MY_MENU_EAT_AGAIN_CANCEL_SVG).click()
        assert myfeed.getElement(myFeedLocators.MY_FEED_TXT)

        myfeed.goToPage("같은 메뉴 먹기")
        time.sleep(1) # 필수! (삭제 X)
        assert myfeed.getElement(myFeedLocators.MY_MENU_GROUP_BTN).get_attribute("data-state") == "checked"
        assert myfeed.getElement(myFeedLocators.MY_MENU_MENU_NAME_INPUT).get_attribute("disabled") is not None
        assert myfeed.getElement(myFeedLocators.MY_MENU_CATEGORY_BTN).get_attribute("disabled") is not None

        myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_TEXTAREA).clear()
        myfeed.getElement(myFeedLocators.MY_MENU_COMPLETE_BTN).click()
        assert myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_ERROR)
        assert myfeed.getElement(myFeedLocators.MY_MENU_STAR_ERROR)
        
        time.sleep(1) # 필수! (삭제 X)
        myfeed.getClickableElement(myFeedLocators.MY_MENU_PERSON_REMOVE_SVG).click()
        myfeed.waitUntilNotPresent(myFeedLocators.MY_MENU_PERSON_REMOVE_SVG) # 요소가 사라지지 않으면, 예외 발생

        myfeed.getElement(myFeedLocators.MY_MENU_PERSON_NAME_INPUT).send_keys("김")
        myfeed.getClickableElement(myFeedLocators.MY_MENU_PERSON_NAME_SEARCH_RESULT).click()
        assert myfeed.getElements(myFeedLocators.MY_MENU_PERSON_REMOVE_SVG)

        randomReview = myfeed.getRandomReview() # 검증이 필요하므로, 변수에 담음
        myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_TEXTAREA).send_keys(randomReview)
        assert myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_TEXTAREA).get_attribute("value") == randomReview

        randomValue, randomStar = myfeed.getRandomStar() # 검증이 필요하므로, 변수에 담음
        myfeed.getClickableElement(randomStar).click() 
        assert myfeed.getElement(myFeedLocators.MY_MENU_STAR_BTN).get_attribute("value") == randomValue
        myfeed.logger.info(f"▶️ myfeed_078 ~ 095 - 식사 유형이 그룹인 경우, 같은 메뉴 먹기 기능 확인")

        myfeed.getElement(myFeedLocators.MY_MENU_COMPLETE_BTN).click()

        afterReviewCount = myfeed.getReviewPostCount()

        assert beforeReviewCount + 1 == afterReviewCount
        myfeed.logger.info(f"▶️ myfeed_096 - 식사 유형이 그룹인 경우, 같은 메뉴 먹기 정상 등록 확인")

        myfeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_myFeed_013(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("[+] 버튼")

        time.sleep(1) # 필수! (삭제 X)
        myfeed.getClickableElement(myFeedLocators.MY_MENU_TEAM_BTN).click()
        myfeed.getClickableElement(myFeedLocators.MY_MENU_COMPLETE_BTN).click()
        time.sleep(1) # 필수! (삭제 X)
        assert myfeed.getElement(myFeedLocators.MY_MENU_IMG_ERROR)
        assert myfeed.getElement(myFeedLocators.MY_MENU_MENU_NAME_ERROR)
        assert myfeed.getElement(myFeedLocators.MY_MENU_CATEGORY_ERROR)
        assert myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_ERROR)
        assert myfeed.getElement(myFeedLocators.MY_MENU_STAR_ERROR)
        myfeed.logger.info(f"▶️ myfeed_052 - [새로운 후기 등록/회식] 아무것도 입력하지 않고 [후기 작성 완료] 버튼 클릭 시 에러 문구 노출 확인")

        myfeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_myFeed_014(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("개인 피드")

        beforeReviewCount = myfeed.getReviewPostCount()

        myfeed.goToPage("[+] 버튼")

        time.sleep(1) # 필수! (삭제 X)
        myfeed.getClickableElement(myFeedLocators.MY_MENU_TEAM_BTN).click()
        assert myfeed.screenDiff(myFeedLocators.MY_MENU_IMG_INPUT, inspect.currentframe().f_code.co_name, "reviewImg", "image", myfeed.getRandomImage())

        randomMenuName = myfeed.getRandomMenuName() # 검증이 필요하므로, 변수에 담음
        myfeed.getElement(myFeedLocators.MY_MENU_MENU_NAME_INPUT).send_keys(randomMenuName)
        assert myfeed.getElement(myFeedLocators.MY_MENU_MENU_NAME_INPUT).get_attribute("value") == randomMenuName

        randomName, randomCategory = myfeed.getRandomCategory() # 검증이 필요하므로, 변수에 담음
        myfeed.getClickableElement(myFeedLocators.MY_MENU_CATEGORY_BTN).click()
        myfeed.getClickableElement(randomCategory).click()
        assert myfeed.getElement(myFeedLocators.NY_MENU_CATEGORY_TXT).text == randomName

        randomReview = myfeed.getRandomReview() # 검증이 필요하므로, 변수에 담음
        myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_TEXTAREA).send_keys(randomReview)
        assert myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_TEXTAREA).get_attribute("value") == randomReview

        randomValue, randomStar = myfeed.getRandomStar() # 검증이 필요하므로, 변수에 담음
        myfeed.getClickableElement(randomStar).click()
        assert myfeed.getElement(myFeedLocators.MY_MENU_STAR_BTN).get_attribute("value") == randomValue

        myfeed.getClickableElement(myFeedLocators.MY_MENU_COMPLETE_BTN).click()

        afterReviewCount = myfeed.getReviewPostCount()

        assert beforeReviewCount + 1 == afterReviewCount
        myfeed.logger.info(f"▶️ myfeed_053 ~ 062 - [새로운 후기 등록/회식] 유효성 조건을 충족 후 [후기 작성 완료] 버튼 클릭 시 정상 등록 확인")

        myfeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_myFeed_017(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("개인 피드")

        beforeReviewCount = myfeed.getReviewPostCount()

        myfeed.goToPage("같은 메뉴 먹기")

        time.sleep(1) # 필수! (삭제 X)
        myfeed.getClickableElement(myFeedLocators.MY_MENU_EAT_AGAIN_CANCEL_SVG).click()
        assert myfeed.getElement(myFeedLocators.MY_FEED_TXT)

        myfeed.goToPage("같은 메뉴 먹기")
        time.sleep(1) # 필수! (삭제 X)
        assert myfeed.getElement(myFeedLocators.MY_MENU_TEAM_BTN).get_attribute("data-state") == "checked"
        assert myfeed.getElement(myFeedLocators.MY_MENU_MENU_NAME_INPUT).get_attribute("disabled") is not None
        assert myfeed.getElement(myFeedLocators.MY_MENU_CATEGORY_BTN).get_attribute("disabled") is not None

        myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_TEXTAREA).clear()
        myfeed.getClickableElement(myFeedLocators.MY_MENU_COMPLETE_BTN).click()
        assert myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_ERROR)
        assert myfeed.getElement(myFeedLocators.MY_MENU_STAR_ERROR)

        randomReview = myfeed.getRandomReview() # 검증이 필요하므로, 변수에 담음
        myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_TEXTAREA).send_keys(randomReview)
        assert myfeed.getElement(myFeedLocators.MY_MENU_REVIEW_TEXTAREA).get_attribute("value") == randomReview
        myfeed.logger.info(f"▶️ myfeed_097 ~ 110 - 식사 유형이 회식인 경우, 같은 메뉴 먹기 기능 확인")

        randomValue, randomStar = myfeed.getRandomStar() # 검증이 필요하므로, 변수에 담음
        myfeed.getClickableElement(randomStar).click() 
        assert myfeed.getElement(myFeedLocators.MY_MENU_STAR_BTN).get_attribute("value") == randomValue

        myfeed.getClickableElement(myFeedLocators.MY_MENU_COMPLETE_BTN).click()

        afterReviewCount = myfeed.getReviewPostCount()

        assert beforeReviewCount + 1 == afterReviewCount
        myfeed.logger.info(f"▶️ myfeed_096 - 식사 유형이 회식인 경우, 같은 메뉴 먹기 정상 등록 확인")

        myfeed.logger.info(f"✅ {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise