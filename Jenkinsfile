// Jenkins CI/CD 파이프라인 정의 파일

pipeline {
    agent any
    
    stages {
        stage('Run Tests') {
            steps {
                withCredentials([file(credentialsId: 'credentials-json', variable: 'CREDENTIALS_JSON')]) {
                    sh '''
                    cp $CREDENTIALS_JSON credentials.json
                    
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    python3 -m pytest
                    
                    rm credentials.json
                    '''
                }
            }
        }
    }
}
