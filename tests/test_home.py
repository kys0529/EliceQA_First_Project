# 작업자 이름: 김다예

import time
import pytest
import inspect
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from src.pages.home import home
from src.utils import homeLocators

# @pytest.mark.dy /검증완료 → @pytest.mark.finish
# 테스트 끝나면 함수 내 모든 time.sleep() 삭제하기
# 실행문: PYTHONPATH=. pytest tests/test_home.py -m "dy"
# time.sleep(2)
@pytest.mark.finish
def test_home_001(createDriver): # 함수명 바꾸셔도 좋아요
    try:
        myhome = home(createDriver) # 변수명 바꾸셔도 좋아요
        # [혼자먹기] 버튼 선택> 추천 옵션 타이틀 확인
        myhome.goToPage("혼자 먹기")
        assert myhome.getElement(homeLocators.RECOMMEND_OPTION_TITLE_TXT)
      
        # [뒤로가기] 버튼 선택> 이전페이지로 이동 
        myhome.wait.until(EC.presence_of_element_located(homeLocators.RECOMMEND_BACK_BTN))
        myhome.getElement(homeLocators.RECOMMEND_BACK_BTN).click()
        assert myhome.getElement(homeLocators.HOME_ALONE_BTN)
        
        # 혼자먹기 재진입
        myhome.goToPage("혼자 먹기")

        # 한식 카테고리 선택> 한식 카테고리 입력
        myhome.getElement(homeLocators.RECOMMEND_CATEGORY_DROPDOWN).click()
        myhome.getElement(homeLocators.RECOMMEND_OPTION_KOREAN).click()
        assert myhome.getElement(homeLocators.RECOMMEND_OPTION_KOREAN_RESULT)

        # [선택 완료] 버튼 선택> 메뉴 추천 페이지로 이동
        myhome.getElement(homeLocators.RECOMMEND_SUBMIT_BTN).click()
        assert myhome.getElement(homeLocators.RECOMMEND_OPTION_KOREAN_RESULT)       
        
        myhome.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myhome.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.dy
def test_home_003(createDriver): 
    try:
        myhome = home(createDriver) 
        # [같이먹기] 버튼 선택> 추천 옵션 타이틀 확인
        myhome.goToPage("같이 먹기")
        assert myhome.getElement(homeLocators.RECOMMEND_SEARCH_NAME)
      
        # [뒤로가기] 버튼 선택> 이전페이지로 이동 
        myhome.wait.until(EC.presence_of_element_located(homeLocators.RECOMMEND_BACK_BTN))
        myhome.getElement(homeLocators.RECOMMEND_BACK_BTN).click()
        assert myhome.getElement(homeLocators.HOME_ALONE_BTN)

        # 같이먹기 재진입
        myhome.goToPage("같이 먹기")

        # 전부 미선택> [선택 완료] 버튼 비활성화 상태 확인
        submit_btn = myhome.getElement(homeLocators.RECOMMEND_SUBMIT_BTN )
        assert submit_btn.get_attribute("disabled") is not None

        # 한식 카테고리 선택> 한식 카테고리 입력
        myhome.getElement(homeLocators.RECOMMEND_CATEGORY_DROPDOWN).click()
        myhome.getElement(homeLocators.RECOMMEND_OPTION_KOREAN).click()
        assert myhome.getElement(homeLocators.RECOMMEND_OPTION_KOREAN_RESULT)

        # 먹는 인원 검색 "김" 
        myhome.getElement(homeLocators.RECOMMEND_SEARCH_NAME).click()
        myhome.getElement(homeLocators.RECOMMEND_SEARCH_NAME).send_keys("김")
        assert myhome.getElement(homeLocators.RECOMMEND_SEARCH_RESULT)

        # "김" 텍스트 선택
        myhome.getElement(homeLocators.RECOMMEND_SEARCH_RESULT).click()
        assert myhome.getElement(homeLocators.RECOMMEND_SEARCH_RESULT)

        # 추가된 이름 삭제 (재확인 필요ㅠㅠㅠㅠㅠ fail.....bbb)
        # myhome.getElement(homeLocators.RECOMMEND_SEARCH_SELECTED).click()
        # time.sleep(1)

        el = myhome.getElement(homeLocators.RECOMMEND_SEARCH_SELECTED)
        myhome.driver.execute_script("arguments[0].click();", el)

        assert not myhome.driver.find_elements(*homeLocators.RECOMMEND_SEARCH_SELECTED), "❗ 요소가 아직 존재합니다"

        # assert myhome.wait.until(EC.staleness_of(selected_element))

        # myfeed.getElement(myFeedLocators.MY_MENU_PLUS_GROUP_BTN).click()
        # assert myfeed.screenDiff(myFeedLocators.MY_MENU_PLUS_IMG_INPUT, inspect.currentframe().f_code.co_name, "reviewImg", "image", myfeed.getRandomImage())

        # myfeed.getElement(myFeedLocators.MY_MENU_PLUS_PERSON_NAME_INPUT).send_keys("김")
        # myfeed.getElement(myFeedLocators.MY_MENU_PLUS_PERSON_NAME_SEARCH_RESULT).click()
        # assert len(myfeed.getElements(myFeedLocators.MY_MENU_PLUS_PERSON_REMOVE_SVG)) == 1

        # time.sleep(2)
        # myfeed.getElement(myFeedLocators.MY_MENU_PLUS_PERSON_REMOVE_SVG).click()


        myhome.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myhome.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.finish
def test_home_005(createDriver): 
    try:
        myhome = home(createDriver) 
        myhome.goToPage("회식 하기")
        assert myhome.getElement(homeLocators.RECOMMEND_TEAM_BADGE)
      
        # [뒤로가기] 버튼 선택> 이전페이지로 이동 
        myhome.wait.until(EC.presence_of_element_located(homeLocators.RECOMMEND_BACK_BTN))
        myhome.getElement(homeLocators.RECOMMEND_BACK_BTN).click()
        assert myhome.getElement(homeLocators.HOME_ALONE_BTN)
        
        # 회식하기 재진입
        myhome.goToPage("회식 하기")

        # 한식 카테고리 선택> 한식 카테고리 입력
        myhome.getElement(homeLocators.RECOMMEND_CATEGORY_DROPDOWN).click()
        myhome.getElement(homeLocators.RECOMMEND_OPTION_KOREAN).click()
        assert myhome.getElement(homeLocators.RECOMMEND_OPTION_KOREAN_RESULT)

        # [선택 완료] 버튼 선택> 메뉴 추천 페이지로 이동
        myhome.getElement(homeLocators.RECOMMEND_SUBMIT_BTN).click()
        assert myhome.getElement(homeLocators.RECOMMEND_OPTION_KOREAN_RESULT)       
        
        myhome.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myhome.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise