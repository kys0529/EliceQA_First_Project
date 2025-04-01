// Jenkins CI/CD 파이프라인 정의 파일

pipeline {
    agent any

    environment {
        CREDS_JSON = credentials('credentials-json')
    }
    
    stages {
        stage('Run Tests') {
            steps {
                sh '''
                    cd $WORKSPACE
                    cat "$CREDS_JSON" > credentials.json
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    python3 -m pytest
                '''
            }
        }
    }
}
