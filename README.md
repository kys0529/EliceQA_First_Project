## 5️⃣조 팀소개
- 팀명: High Five(하이파이브)
- 좌우명: 협업으로 최고의 성과를 내는 팀
   
## 👥 팀원
- 강연수(팀장)
- 채승호
- 윤찬유
- 김다예
   
## 📌 프로젝트 개요
오늘 뭐 먹지?   
AI 기반 직장인 점심 메뉴 및 회식 장소 추천 서비스   
- 🔗 [서비스 URL](https://kdt-pt-1-pj-2-team03.elicecoding.com/)
   
## 🔹 주요 기능
점심 메뉴 선택으로 고민하는 직장인들을 위해 AI 추천 시스템을 활용한 맞춤형 메뉴 추천 웹서비스입니다.   
사용자의 취향을 분석하여 개인 및 팀 맞춤형 점심 메뉴를 제공하며, 회식 장소 추천 기능도 포함됩니다.
- AI 추천 시스템을 통한 개인/팀 맞춤형 점심 메뉴 추천
- 사용자 취향 및 히스토리 기반 추천 기능
- 팀 단위 점심 및 회식 장소 추천
- 추천 결과에 대한 피드백 반영 및 개선
   
## 🛠 사용 기술
- 테스트 자동화: Selenium, Pytest
- CI/CD: GitLab CI/CD, Genkins
   
## 📁 파일 구조
```
project_root/
├── src/                   # 자동화 프레임워크의 소스 코드
│   ├── pages/             # Page Object 클래스 (UI 요소 및 메서드 정의)
│   │   ├── __init__.py
│   │   └── example_page.py
│   ├── utils/             # 공통 유틸리티 함수 및 헬퍼 모듈
│   │   ├── __init__.py
│   │   └── helpers.py
│   ├── config/            # 환경 설정 파일 (config.ini, 환경별 설정 등)
│   │   └── config.ini
│   └── resources/         # 테스트 데이터 및 기타 리소스 파일
│       ├── testdata/      # JSON, CSV, XML 형태의 테스트 데이터
│       └── assets/        # 이미지 등 기타 자원 파일
├── tests/                 # 실제 테스트 케이스 구현 디렉토리 (pytest 테스트 코드)
│   ├── conftest.py        # pytest fixture 및 공통 설정 정의
│   ├── test_example.py    # 실제 테스트 스크립트 (test_*.py 형식)
│   └── ...
├── reports/               # 테스트 실행 후 생성된 보고서 및 로그 저장 디렉토리
│   ├── logs/
│   └── screenshots/
├── requirements.txt       # Python 의존성 패키지 목록 (pip install -r requirements.txt)
├── pytest.ini             # pytest 설정 파일 (테스트 옵션 지정)
└── Jenkinsfile            # Jenkins CI/CD 파이프라인 정의 파일
```
