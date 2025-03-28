# 작업자 이름: @@@

import pytest
from src.pages.myFeed import myFeed

def test_myFeed_001(createDriver): # 함수명 바꾸셔도 좋아요
    myfeed = myFeed(createDriver) # 변수명 바꾸셔도 좋아요