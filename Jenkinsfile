pipeline {
    agent any

    environment {
        CREDS_JSON = credentials('credentials-json')
    }

    stages {
        stage('Run Tests') {
            steps {
                dir("$WORKSPACE") {
                    sh """
                        cat <<EOF > credentials.json
$CREDS_JSON
EOF
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                        python3 -m pytest
                    """
                }
            }
        }
    }
}
