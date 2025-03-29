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

        time.sleep(2)
        myfeed.getElement(myFeedLocators.MY_PROFILE_CHANGE_CANCEL_SVG).click()
        time.sleep(2)
        assert myfeed.getElement(myFeedLocators.MY_FEED_TXT)

        myfeed.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise

@pytest.mark.ys
def test_myFeed_003(createDriver):
    try:
        myfeed = myFeed(createDriver)
        myfeed.goToPage("프로필 수정")

        # 미구현

        myfeed.logger.info(f"[✅] {inspect.currentframe().f_code.co_name} 통과")
    except Exception as e:
        myfeed.logger.warning(f"[❗] {inspect.currentframe().f_code.co_name} : {e}")
        raise