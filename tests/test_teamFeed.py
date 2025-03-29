# 작업자 이름: 채승호

import time
import pytest
from src.pages.teamFeed import teamFeed
from src.utils import teamFeedLocators
from selenium.webdriver.common.keys import Keys


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


def test_teamFeed_007(createDriver):
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click() #프로필 수정 팝업 진입
    time.sleep(2)
         
def test_teamFeed_008(createDriver):
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click() 
    myTeamFeed.getElement(teamFeedLocators.CLOSE_BUTTON).click() #닫기
    time.sleep(1)
    
@pytest.mark.sh 
def test_teamFeed_009(createDriver): #10자 미만 텍스트 입력
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click()
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_LIKE).send_keys(Keys.CONTROL, 'a')
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_LIKE).send_keys("다좋아요") #10자 미만 텍스트 입력
    myTeamFeed.getElement(teamFeedLocators.PROFILE_CHANGE_BTN).click()
    time.sleep(1)
    
def test_teamFeed_010(createDriver): #100자 이상 텍스트 입력
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click()
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_LIKE).send_keys(Keys.CONTROL, 'a')
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_LIKE).send_keys("매콤하면서도 깊은 감칠맛이 있는 음식은 좋아요! 특히 고추장 베이스의 한식이나 향신료가 풍부한 태국 요리는 식욕을 돋우는 맛의 조화가 완벽해서 자주 찾게 됩니다. 신선한 해산물이 들어간 요리도 좋아하는데, 바다의 깊은 맛이 입안에 퍼질 때의 그 만족감이 특별합니다.") 
    myTeamFeed.getElement(teamFeedLocators.PROFILE_CHANGE_BTN).click()
    time.sleep(1)
    