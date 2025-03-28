# 작업자 이름: 김다예

import pytest
from src.pages.home import home

def test_home_001(createDriver): # 함수명 바꾸셔도 좋아요
    myhome = home(createDriver) # 변수명 바꾸셔도 좋아요