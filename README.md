## 팀명
HighFive

## 팀원


## 파일 구조
```
project_root/
├── src/                 # 자동화 프레임워크의 소스 코드
│   ├── pages/           # Page Object 클래스 (UI 요소 및 메서드 정의)
│   │   ├── __init__.py
│   │   └── example_page.py
│   ├── utils/           # 공통 유틸리티 함수 및 헬퍼 모듈
│   │   ├── __init__.py
│   │   └── helpers.py
│   ├── config/          # 환경 설정 파일 (config.ini, 환경별 설정 등)
│   │   └── config.ini
│   └── resources/       # 테스트 데이터 및 기타 리소스 파일
│       ├── testdata/    # JSON, CSV, XML 형태의 테스트 데이터
│       └── assets/      # 이미지 등 기타 자원 파일
├── tests/               # 실제 테스트 케이스 구현 디렉토리 (pytest 테스트 코드)
│   ├── conftest.py      # pytest fixture 및 공통 설정 정의
│   ├── test_example.py  # 실제 테스트 스크립트 (test_*.py 형식)
│   └── ...
├── reports/             # 테스트 실행 후 생성된 보고서 및 로그 저장 디렉토리
│   ├── logs/
│   └── screenshots/
├── requirements.txt     # Python 의존성 패키지 목록 (pip install -r requirements.txt)
├── pytest.ini           # pytest 설정 파일 (테스트 옵션 지정)
└── Jenkinsfile          # Jenkins CI/CD 파이프라인 정의 파일
```
