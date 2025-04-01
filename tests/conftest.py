# pytest fixture 및 공통 설정 정의

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def createDriver():
    chromeOption = Options()

    chromeOption.add_argument('--start-maximized')          # 브라우저 창을 시작 시 최대화
    # chromeOption.add_argument('--incognito')              # 시크릿 모드 실행 (기록 비활성화)
    chromeOption.add_argument('--no-sandbox')               # 샌드박스 보안 기능 비활성화 (리눅스 환경에서 주로 사용)
    chromeOption.add_argument('--disable-dev-shm-usage')    # /dev/shm 용량 부족 문제 방지 (Docker, CI 환경에서 유용)
    chromeOption.add_argument('--disable-gpu')              # GPU 가속 비활성화 (가상환경에서 렌더링 오류 방지)
    chromeOption.add_argument('--headless')               # GUI 없이 브라우저 실행 (백그라운드 테스트 시 사용)
    chromeOption.page_load_strategy = "eager"               # DOMContentLoaded 이벤트 이후 바로 다음 단계로 진행 (빠른 로딩)

    driver = webdriver.Chrome(options=chromeOption)
    driver.implicitly_wait(5) # Selenium이 요소를 찾을 때, 즉시 실패하지 않고 최대 n초 동안 계속 재시도하며 기다리는 기본 설정
    driver.delete_all_cookies() # Selenium에서 브라우저에 저장된 모든 쿠키를 삭제

    yield driver

    driver.quit()
