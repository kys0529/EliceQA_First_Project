# 작업자 이름: 채승호

import time
import pytest
from src.pages.teamFeed import teamFeed
from src.utils import teamFeedLocators


def test_teamFeed_001(createDriver): # 함수명 바꾸셔도 좋아요
    myTeamFeed = teamFeed(createDriver) # 변수명 바꾸셔도 좋아요
    myTeamFeed.goToPage("팀 피드")
    time.sleep(1)


def test_teamFeed_002(createDriver):
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DROP_DOWN).click()


def test_teamFeed_003(createDriver):
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DROP_DOWN).click()
    myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DEV_1).click() #개발 1팀
    time.sleep(1)
    

def test_teamFeed_004(createDriver):
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DROP_DOWN).click()
    myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DEV_2).click() #개발 2팀
    time.sleep(1)
    

def test_teamFeed_005(createDriver):
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DROP_DOWN).click()
    myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DESIGN_1).click() #디자인 1팀
    time.sleep(1)
    
    
def test_teamFeed_006(createDriver):
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DROP_DOWN).click()
    myTeamFeed.getElement(teamFeedLocators.USERINFO_TEAM_DESIGN_2).click() #디자인 2팀
    time.sleep(1)

def test_teamFeed_007(createDriver):
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click() #프로필 수정 팝업 진입
    time.sleep(1)

#슬라이드 바 테스트 하는 방법 필요
def test_teamFeed_0071(createDriver):
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click()
    myTeamFeed.getElement(teamFeedLocators.USERINFO_SLIDER)
    myTeamFeed.getElement(teamFeedLocators.USERINFO_SLIDER_VALUE)
    time.sleep(1)
        
def test_teamFeed_008(createDriver):
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click() 
    myTeamFeed.getElement(teamFeedLocators.CLOSE_BUTTON).click() #닫기
    time.sleep(1)
    

def test_teamFeed_009(createDriver): #이런 음식은 좋아요! 텍스트 박스 10자 미만 텍스트 입력
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click()
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_LIKE).clear()
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_LIKE).send_keys("다 좋아요") #10자 미만 텍스트 입력
    myTeamFeed.getElement(teamFeedLocators.PROFILE_CHANGE_BTN).click()
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_MINUS_ERROR)
    time.sleep(1)


def test_teamFeed_010(createDriver): #이런 음식은 좋아요! 텍스트 박스 100자 이상 텍스트 입력
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click()
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_LIKE).clear()
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_LIKE).send_keys("매콤하면서도 깊은 감칠맛이 있는 음식은 좋아요! 특히 고추장 베이스의 한식이나 향신료가 풍부한 태국 요리는 식욕을 돋우는 맛의 조화가 완벽해서 자주 찾게 됩니다. 신선한 해산물이 들어간 요리도 좋아하는데, 바다의 깊은 맛이 입안에 퍼질 때의 그 만족감이 특별합니다.") 
    myTeamFeed.getElement(teamFeedLocators.PROFILE_CHANGE_BTN).click()
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_PLUS_ERROR)
    time.sleep(1)
    

def test_teamFeed_011(createDriver): #이런 음식은 싫어요! 텍스트 박스 10자 미만 텍스트 입력
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click()
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_HATE).clear()
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_HATE).send_keys("다 싫어요") #10자 미만 텍스트 입력
    myTeamFeed.getElement(teamFeedLocators.PROFILE_CHANGE_BTN).click()
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_MINUS_ERROR)
    time.sleep(1)
    

def test_teamFeed_012(createDriver): #이런 음식은 싫어요! 텍스트 박스 100자 이상 텍스트 입력
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click()
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_HATE).clear()
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_HATE).send_keys("비린내가 강한 해산물은 제가 정말 피하고 싶은 음식 중 하나입니다. 생선 특유의 비린 향이 코를 찌르면 식욕이 완전히 사라져 버립니다. 문어나 오징어 같은 탱글탱글한 식감의 해산물은 씹을 때마다 거부감이 들어요. 어릴 때 해산물을 먹고 심한 알레르기 반응을 경험한 후로 트라우마가 생겼습니다. 가족 모임이나 회식에서 해산물 요리가 나오면 항상 난처한 상황에 처하게 됩니다.") 
    myTeamFeed.getElement(teamFeedLocators.PROFILE_CHANGE_BTN).click()
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_PLUS_ERROR)
    time.sleep(1)   
    
@pytest.mark.sh    
def test_teamFeed_013(createDriver): #유효한 수정 값
    myTeamFeed = teamFeed(createDriver)
    myTeamFeed.goToPage("팀 피드")
    myTeamFeed.getElement(teamFeedLocators.TEAM_PROFILE_CHANGE).click()
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_LIKE).clear()
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_LIKE).send_keys("매콤하면서도 깊은 감칠맛이 있는 음식은 좋아요!")
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_HATE).clear()
    myTeamFeed.getElement(teamFeedLocators.TEXTAREA_HATE).send_keys("비린내가 강한 해산물은 제가 정말 피하고 싶은 음식 중 하나입니다.") 
    myTeamFeed.getElement(teamFeedLocators.PROFILE_CHANGE_BTN).click()
    time.sleep(1)


    