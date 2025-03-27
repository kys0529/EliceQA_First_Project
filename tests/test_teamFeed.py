# 작업자 이름: 채승호

import pytest
from src.pages.teamFeed import teamFeed

def test_teamFeed_001(createDriver):
    myTeamFeed = teamFeed(createDriver)