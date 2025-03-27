# 작업자 이름: 김다예

import pytest
from src.pages.home import home

def test_home_001(createDriver):
    myhome = home(createDriver)