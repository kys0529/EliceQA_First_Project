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

        myfeed.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

def test_myFeed_002(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("프로필 수정")
        time.sleep(2)

        # 미구현 (프로필 수정까지는 진입 완료)

        myfeed.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.ys
def test_myFeed_003(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("[+] 버튼")
        time.sleep(2)

        # 미구현 ("[+] 버튼"까지는 진입 완료)

        myfeed.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

def test_myFeed_004(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("같은 메뉴 먹기")
        time.sleep(2)

        # 미구현 ("같은 메뉴 먹기"까지는 진입 완료)

        myfeed.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise