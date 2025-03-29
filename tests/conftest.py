# pytest fixture 및 공통 설정 정의

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def createDriver():
    chromeOption = Options()

    chromeOption.add_argument('--start-maximized') # 전체 화면
    chromeOption.add_argument('--incognito') # 시크릿 모드
    chromeOption.add_argument("--no-sandbox") # 브라우저의 보안 기능 없이 테스트
    chromeOption.add_argument('--disable-dev-shm-usage')  # shared memory 문제 방지
    chromeOption.add_argument('--disable-gpu')  # 가상환경에서 GPU 기능 비활성화
    chromeOption.add_argument("--headless") # GUI 없이 테스트

    driver = webdriver.Chrome(options=chromeOption)

    yield driver

    driver.quit()