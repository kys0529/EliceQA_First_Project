// Jenkins CI/CD 파이프라인 정의 파일

pipeline {
    agent any

    stages {
        stage('Run Tests') {
            steps {
                dir("${env.WORKSPACE}") {
                    withCredentials([file(credentialsId: 'credentials-json', variable: 'CREDS_FILE')]) {
                        sh '''
                            cat "$CREDS_FILE" > credentials.json
                            python3 -m venv venv
                            . venv/bin/activate
                            pip install -r requirements.txt
                            python3 -m pytest
                        '''
                    }
                }
            }
        }
    }
}
