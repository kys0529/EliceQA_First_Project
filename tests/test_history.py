# 작업자 이름: 윤찬유

import pytest
from src.pages.history import history

def test_history_001(createDriver): # 함수명 바꾸셔도 좋아요
    myHistory = history(createDriver) # 변수명 바꾸셔도 좋아요