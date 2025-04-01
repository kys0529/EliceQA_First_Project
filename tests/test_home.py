# 작업자 이름: 김다예

import time
import pytest
import inspect
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from src.pages.home import home
from src.utils import homeLocators

# @pytest.mark.dy /검증완료 → @pytest.mark.finish
# 테스트 끝나면 함수 내 모든 time.sleep() 삭제하기
# 실행문: PYTHONPATH=. pytest tests/test_home.py -m "dy"
# time.sleep(2)
@pytest.mark.finish
def test_home_001(createDriver): 
    try:
        myhome = home(createDriver)
        # [혼자먹기] 버튼 선택> 추천 옵션 타이틀 확인
        myhome.goToPage("혼자 먹기")
        assert myhome.getElement(homeLocators.RECOMMEND_OPTION_TITLE_TXT)
        myhome.logger.info("▶️ home_001 - 혼자 먹기 페이지 이동 확인")

        # [뒤로가기] 버튼 선택> 이전페이지로 이동 
        myhome.wait.until(EC.presence_of_element_located(homeLocators.RECOMMEND_BACK_BTN))
        myhome.getElement(homeLocators.RECOMMEND_BACK_BTN).click()
        assert myhome.getElement(homeLocators.HOME_ALONE_BTN)
        myhome.logger.info("▶️ home_002 - 뒤로가기 버튼 확인")
        
        # 혼자먹기 재진입
        myhome.goToPage("혼자 먹기")

        # [선택 완료] 버튼 비활성화 확인
        submit_btn = myhome.getElement(homeLocators.RECOMMEND_SUBMIT_BTN)
        assert submit_btn.get_attribute("disabled") is not None
        myhome.logger.info("▶️ home_003 - [선택 완료] 버튼 비활성화 확인")

        # 한식 카테고리 선택> 한식 카테고리 입력
        myhome.getElement(homeLocators.RECOMMEND_CATEGORY_DROPDOWN).click()
        myhome.logger.info("▶️ home_004 - 드롭다운 카테고리 노출 확인")
        myhome.getElement(homeLocators.RECOMMEND_OPTION_KOREAN).click()
        assert myhome.getElement(homeLocators.RECOMMEND_OPTION_KOREAN_RESULT)
        myhome.logger.info("▶️ home_005 - 드롭다운 카테고리 한식 선택 확인")

        # [선택 완료] 버튼 선택> 메뉴 추천 페이지로 이동
        myhome.getElement(homeLocators.RECOMMEND_SUBMIT_BTN).click()
        myhome.logger.info("▶️ home_006 - [선택 완료] 버튼 활성화 확인")
        assert myhome.getElement(homeLocators.RESULT_HEADER_TITLE)  
        myhome.logger.info("▶️ home_007 - [선택 완료] 버튼 이동 확인")
               

        # 맛집 리스트가 나올 때까지 반복문
        while True:
            try:
                myhome.driver.find_element(*homeLocators.RESULT_NO_RESTAURANT)
                myhome.logger.info("▶️ home_008 - 맛집 리스트 미존재 확인")
                retry_btn = myhome.getElement(homeLocators.RESULT_RETRY_BTN)
                # [다시 추천 받기] 버튼이 뷰포트 하단에 숨겨져 있어서 자동 클릭 안됨> 스크롤 다운
                myhome.driver.execute_script("arguments[0].scrollIntoView(true);", retry_btn)
                time.sleep(1) # 스크롤 후 렌더링 대기
                retry_btn.click()
                myhome.logger.info("▶️ home_009 - [다시 추천받기] 버튼 확인")

            except NoSuchElementException:
                break

        # 맛집 리스트 있는 경우 진입, 테스트 시작
        try:
            first_dot = myhome.getElement(homeLocators.RESULT_RESTAURANT_CAROUSEL_FIRST)
            second_dot = myhome.getElement(homeLocators.RESULT_RESTAURANT_CAROUSEL_SECOND)

            second_dot.click()
            first_dot.click()
        
            active_dot = myhome.getElement(homeLocators.RESULT_RESTAURANT_CAROUSEL_ACTIVE)
            assert first_dot == active_dot
            myhome.logger.info("▶️ home_010 - 캐러셀 이동 확인")

            # 맛집 리스트 선택
            myhome.getElement(homeLocators.RESULT_RESTAURANT_FIRST).click()

            # 탭이 2개가 됐는지 확인
            tabs = myhome.driver.window_handles
            assert len(tabs) == 2, "❗ 새 탭이 열리지 않았습니다"

            # 새 탭으로 전환
            myhome.driver.switch_to.window(tabs[1])
            time.sleep(1)

            # URL 검증 (예: 특정 도메인 또는 식별자 포함)
            assert "store" in myhome.driver.current_url or "place" in myhome.driver.current_url, "❗ 예상 URL 아님"
            myhome.logger.info("▶️ home_011 - 카카오맵(새탭) 확인)")

            # 다시 원래 탭으로 복귀
            myhome.driver.close()
            myhome.driver.switch_to.window(tabs[0])

            # [추천 수락하기] 버튼 선택
            myhome.getElement(homeLocators.RESULT_ACCEPT_BTN).click()
            assert myhome.getElement(homeLocators.RESULT_ACCEPT_BTN_AFTER)
            myhome.logger.info("▶️ home_012 - [추천 수락하기] 버튼 선택")

            # myhome.logger.info(f"▶️ {inspect.currentframe().f_code.co_name} 통과")
        except Exception as e:
            # myhome.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            raise

        myhome.logger.info(f"✅ {inspect.currentframe().f_code.co_name} '혼자 먹기 통과'")
    except Exception as e:
        myhome.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
        raise


@pytest.mark.finish
def test_home_002(createDriver): 
    try:
        myhome = home(createDriver) 
        # [같이먹기] 버튼 선택> 추천 옵션 타이틀 확인
        myhome.goToPage("같이 먹기")
        assert myhome.getElement(homeLocators.RECOMMEND_SEARCH_NAME)
        myhome.logger.info("▶️ home_013 - 혼자 먹기 페이지 이동 확인")

        # [뒤로가기] 버튼 선택> 이전페이지로 이동 
        myhome.wait.until(EC.presence_of_element_located(homeLocators.RECOMMEND_BACK_BTN))
        myhome.getElement(homeLocators.RECOMMEND_BACK_BTN).click()
        assert myhome.getElement(homeLocators.HOME_ALONE_BTN)
        myhome.logger.info("▶️ home_014 - 뒤로가기 버튼 확인")

        # 같이먹기 재진입
        myhome.goToPage("같이 먹기")

        # 전부 미선택> [선택 완료] 버튼 비활성화 상태 확인
        submit_btn = myhome.getElement(homeLocators.RECOMMEND_SUBMIT_BTN )
        assert submit_btn.get_attribute("disabled") is not None
        myhome.logger.info("▶️ home_015 - [선택 완료] 버튼 비활성화 확인")

        # 한식 카테고리 선택> 한식 카테고리 입력
        myhome.getElement(homeLocators.RECOMMEND_CATEGORY_DROPDOWN).click()
        myhome.logger.info("▶️ home_016 - 드롭다운 카테고리 노출 확인")
        myhome.getElement(homeLocators.RECOMMEND_OPTION_KOREAN).click()
        assert myhome.getElement(homeLocators.RECOMMEND_OPTION_KOREAN_RESULT)
        myhome.logger.info("▶️ home_017 - 드롭다운 카테고리 한식 선택 확인")

        # 이름을 검색해주세요 선택 
        myhome.getElement(homeLocators.RECOMMEND_SEARCH_NAME).click()
        myhome.logger.info("▶️ home_018 - 이름 포커싱")

        # 먹는 인원 검색 "김김김김김" / 미 등록된 이름
        myhome.getElement(homeLocators.RECOMMEND_SEARCH_NAME).send_keys("김김김김김")
        assert not myhome.driver.find_elements(*homeLocators.RECOMMEND_SEARCH_RESULT)
        myhome.logger.info("▶️ home_019 - 미 등록된 이름 검색")

        # 먹는 인원 검색 "김" / 등록된 이름
        myhome.getElement(homeLocators.RECOMMEND_SEARCH_NAME).clear()
        myhome.getElement(homeLocators.RECOMMEND_SEARCH_NAME).send_keys("김")
        assert myhome.getElement(homeLocators.RECOMMEND_SEARCH_RESULT)
        myhome.logger.info("▶️ home_020 - 등록된 이름 검색")
        results = myhome.driver.find_elements(*homeLocators.RECOMMEND_SEARCH_RESULT)
        assert len(results) > 0, "등록된 이름 검색 결과가 없습니다"

        # "김" 텍스트 선택
        myhome.getElement(homeLocators.RECOMMEND_SEARCH_RESULT).click()
        assert myhome.getElement(homeLocators.RECOMMEND_SEARCH_SELECTED_BOX)
        myhome.logger.info("▶️ home_021 - 등록된 이름 선택")
        myhome.logger.info("▶️ home_022 - 등록된 이름 추가")

        # 추가된 이름 삭제 (재확인 필요ㅠㅠㅠㅠㅠ fail.....bbb)
        # myhome.getElement(homeLocators.RECOMMEND_SEARCH_SELECTED).click()
        # assert not myhome.driver.find_elements(*homeLocators.RECOMMEND_SEARCH_SELECTED), "❗ 요소가 아직 존재합니다"
        # myhome.logger.info("▶️ home_023 - 등록된 이름 'x' 아이콘 선택")
        # myhome.logger.info("▶️ home_024 - 등록된 이름 삭제")
        # myhome.logger.info("▶️ home_025 - 등록된 이름 체크박스 해제")
        # myhome.logger.info("▶️ home_026 - 등록된 이름 삭제")

        # [선택 완료] 버튼 선택> 메뉴 추천 페이지로 이동
        myhome.getElement(homeLocators.RECOMMEND_SUBMIT_BTN).click()
        myhome.logger.info("▶️ home_027 - [선택 완료] 버튼 활성화 확인")
        assert myhome.getElement(homeLocators.RESULT_HEADER_TITLE)  
        myhome.logger.info("▶️ home_028 - [선택 완료] 버튼 이동 확인")


         # 맛집 리스트가 나올 때까지 반복문
        while True:
            try:
                myhome.driver.find_element(*homeLocators.RESULT_NO_RESTAURANT)
                myhome.logger.info("▶️ home_029 - 맛집 리스트 미존재 확인")
                retry_btn = myhome.getElement(homeLocators.RESULT_RETRY_BTN)
                # [다시 추천 받기] 버튼이 뷰포트 하단에 숨겨져 있어서 자동 클릭 안됨> 스크롤 다운
                myhome.driver.execute_script("arguments[0].scrollIntoView(true);", retry_btn)
                time.sleep(1) # 스크롤 후 렌더링 대기
                retry_btn.click()
                myhome.logger.info("▶️ home_030 - [다시 추천받기] 버튼 확인")

            except NoSuchElementException:
                break

        # 맛집 리스트 있는 경우 진입, 테스트 시작
        try:
            first_dot = myhome.getElement(homeLocators.RESULT_RESTAURANT_CAROUSEL_FIRST)
            second_dot = myhome.getElement(homeLocators.RESULT_RESTAURANT_CAROUSEL_SECOND)

            second_dot.click()
            first_dot.click()
        
            active_dot = myhome.getElement(homeLocators.RESULT_RESTAURANT_CAROUSEL_ACTIVE)
            assert first_dot == active_dot
            myhome.logger.info("▶️ home_031 - 캐러셀 이동 확인")

            # 맛집 리스트 선택
            myhome.getElement(homeLocators.RESULT_RESTAURANT_FIRST).click()

            # 탭이 2개가 됐는지 확인
            tabs = myhome.driver.window_handles
            assert len(tabs) == 2, "❗ 새 탭이 열리지 않았습니다"

            # 새 탭으로 전환
            myhome.driver.switch_to.window(tabs[1])

            # URL 검증 (예: 특정 도메인 또는 식별자 포함)
            assert "store" in myhome.driver.current_url or "place" in myhome.driver.current_url, "❗ 예상 URL 아님"
            myhome.logger.info("▶️ home_032 - 카카오맵(새탭) 확인)")

            # 다시 원래 탭으로 복귀
            myhome.driver.close()
            myhome.driver.switch_to.window(tabs[0])

            # [추천 수락하기] 버튼 선택
            myhome.getElement(homeLocators.RESULT_ACCEPT_BTN).click()
            assert myhome.getElement(homeLocators.RESULT_ACCEPT_BTN_AFTER)
            myhome.logger.info("▶️ home_033 - [추천 수락하기] 버튼 선택")

            # myhome.logger.info(f"▶️ {inspect.currentframe().f_code.co_name} 통과")
        except Exception as e:
            # myhome.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            raise

        myhome.logger.info(f"✅ {inspect.currentframe().f_code.co_name} '같이 먹기 통과'")
    except Exception as e:
        myhome.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise


@pytest.mark.dy
def test_home_003(createDriver): 
    try:
        myhome = home(createDriver) 
        myhome.goToPage("회식 하기")
        assert myhome.getElement(homeLocators.RECOMMEND_TEAM_BADGE)
        myhome.logger.info("▶️ home_034 - 회식 하기 페이지 이동 확인")
      
        # [뒤로가기] 버튼 선택> 이전페이지로 이동 
        myhome.wait.until(EC.presence_of_element_located(homeLocators.RECOMMEND_BACK_BTN))
        myhome.getElement(homeLocators.RECOMMEND_BACK_BTN).click()
        assert myhome.getElement(homeLocators.HOME_ALONE_BTN)
        myhome.logger.info("▶️ home_035 - 뒤로가기 버튼 확인")

        # 회식하기 재진입
        myhome.goToPage("회식 하기")

        # 전부 미선택> [선택 완료] 버튼 비활성화 상태 확인
        submit_btn = myhome.getElement(homeLocators.RECOMMEND_SUBMIT_BTN )
        assert submit_btn.get_attribute("disabled") is not None
        myhome.logger.info("▶️ home_036 - [선택 완료] 버튼 비활성화 확인")

        # 한식 카테고리 선택> 한식 카테고리 입력
        myhome.getElement(homeLocators.RECOMMEND_CATEGORY_DROPDOWN).click()
        myhome.logger.info("▶️ home_037 - 드롭다운 카테고리 노출 확인")
        myhome.getElement(homeLocators.RECOMMEND_OPTION_KOREAN).click()
        assert myhome.getElement(homeLocators.RECOMMEND_OPTION_KOREAN_RESULT)
        myhome.logger.info("▶️ home_038 - 드롭다운 카테고리 한식 선택 확인")

        # [선택 완료] 버튼 선택> 메뉴 추천 페이지로 이동
        myhome.getElement(homeLocators.RECOMMEND_SUBMIT_BTN).click()
        myhome.logger.info("▶️ home_039 - [선택 완료] 버튼 활성화 확인")
        assert myhome.getElement(homeLocators.RESULT_HEADER_TITLE)  
        myhome.logger.info("▶️ home_040 - [선택 완료] 버튼 이동 확인")
               
        # 맛집 리스트가 나올 때까지 반복문
        while True:
            try:
                myhome.driver.find_element(*homeLocators.RESULT_NO_RESTAURANT)
                myhome.logger.info("▶️ home_041 - 맛집 리스트 미존재 확인")
                retry_btn = myhome.getElement(homeLocators.RESULT_RETRY_BTN)
                # [다시 추천 받기] 버튼이 뷰포트 하단에 숨겨져 있어서 자동 클릭 안됨> 스크롤 다운
                myhome.driver.execute_script("arguments[0].scrollIntoView(true);", retry_btn)
                time.sleep(1) # 스크롤 후 렌더링 대기
                retry_btn.click()
                myhome.logger.info("▶️ home_042 - [다시 추천받기] 버튼 확인")

            except NoSuchElementException:
                break

        # 맛집 리스트 있는 경우 진입, 테스트 시작
        try:
            first_dot = myhome.getElement(homeLocators.RESULT_RESTAURANT_CAROUSEL_FIRST)
            second_dot = myhome.getElement(homeLocators.RESULT_RESTAURANT_CAROUSEL_SECOND)

            second_dot.click()
            first_dot.click()
        
            active_dot = myhome.getElement(homeLocators.RESULT_RESTAURANT_CAROUSEL_ACTIVE)
            assert first_dot == active_dot
            myhome.logger.info("▶️ home_043 - 캐러셀 이동 확인")

            # 맛집 리스트 선택
            myhome.getElement(homeLocators.RESULT_RESTAURANT_FIRST).click()

            # 탭이 2개가 됐는지 확인
            tabs = myhome.driver.window_handles
            assert len(tabs) == 2, "❗ 새 탭이 열리지 않았습니다"

            # 새 탭으로 전환
            myhome.driver.switch_to.window(tabs[1])

            # URL 검증 (예: 특정 도메인 또는 식별자 포함)
            assert "store" in myhome.driver.current_url or "place" in myhome.driver.current_url, "❗ 예상 URL 아님"
            myhome.logger.info("▶️ home_044 - 카카오맵(새탭) 확인)")

            # 다시 원래 탭으로 복귀
            myhome.driver.close()
            myhome.driver.switch_to.window(tabs[0])

            # [추천 수락하기] 버튼 선택
            myhome.getElement(homeLocators.RESULT_ACCEPT_BTN).click()
            assert myhome.getElement(homeLocators.RESULT_ACCEPT_BTN_AFTER)
            myhome.logger.info("▶️ home_045 - [추천 수락하기] 버튼 선택")

            # myhome.logger.info(f"▶️ {inspect.currentframe().f_code.co_name} 통과")
        except Exception as e:
            # myhome.logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            raise
        
        myhome.logger.info(f"✅ {inspect.currentframe().f_code.co_name} '회식 하기 통과'")
    except Exception as e:
        myhome.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise