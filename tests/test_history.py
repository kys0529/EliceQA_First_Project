# 작업자 이름: 윤찬유

import pytest
from src.pages.history import history

def test_history_001(createDriver):
    myHistory = history(createDriver)