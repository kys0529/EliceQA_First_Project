# 작업자 이름: 채승호

import time
import pytest
from src.pages.teamFeed import teamFeed
from src.utils import teamFeedLocators


def test_teamFeed_001(createDriver): # 함수명 바꾸셔도 좋아요
    myTeamFeed = teamFeed(createDriver) # 변수명 바꾸셔도 좋아요
    myTeamFeed.goToPage("팀 피드")
    time.sleep(2)


def test_teamFeed_002(createDriver):
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.DROP_DOWN).click()
   
def test_teamFeed_003(createDriver):
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.DROP_DOWN).click()
    myTeamFeed.getElement(teamFeedLocators.DROP_OPTION_DEV_1).click() #개발 1팀
   
def test_teamFeed_004(createDriver):
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.DROP_DOWN).click()
    myTeamFeed.getElement(teamFeedLocators.DROP_OPTION_DEV_2).click() #개발 2팀
    
def test_teamFeed_005(createDriver):
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.DROP_DOWN).click()
    myTeamFeed.getElement(teamFeedLocators.DROP_OPTION_DESIGN_1).click() #디자인 1팀
    
def test_teamFeed_006(createDriver):
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.DROP_DOWN).click()
    myTeamFeed.getElement(teamFeedLocators.DROP_OPTION_DESIGN_2).click() #디자인 2팀
@pytest.mark.sh      
def test_teamFeed_007(createDriver):
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click()
    time.sleep(2)
