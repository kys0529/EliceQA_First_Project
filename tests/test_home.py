# 작업자 이름: 김다예

import pytest
import inspect
from selenium.webdriver.common.by import By

from src.pages.home import home
from src.utils import homeLocators

# @pytest.mark.dy /검증완료 → @pytest.mark.finish
# 테스트 끝나면 함수 내 모든 time.sleep() 삭제하기
# 실행문: PYTHONPATH=. pytest tests/test_home.py -m "dy"
@pytest.mark.dy
def test_home_001(createDriver): # 함수명 바꾸셔도 좋아요
    try:
        myhome = home(createDriver) # 변수명 바꾸셔도 좋아요
        myhome.goToPage("혼자 먹기")
        assert myhome.getElement(homeLocators.RECOMMEND_OPTION_TITLE_TXT)

        myhome.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myhome.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

    