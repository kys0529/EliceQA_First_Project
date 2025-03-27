# 작업자 이름: @@@

import pytest
from src.pages.myFeed import myFeed

def test_myFeed_001(createDriver):
    myhome = myFeed(createDriver)