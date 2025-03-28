# 작업자 이름: 채승호

import pytest
from src.pages.teamFeed import teamFeed

def test_teamFeed_001(createDriver): # 함수명 바꾸셔도 좋아요
    myTeamFeed = teamFeed(createDriver) # 변수명 바꾸셔도 좋아요