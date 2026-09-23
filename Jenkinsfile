pipeline {
    agent any
    stages {
        stage('Install pytest') {
            steps {
                bat 'python -m pip install pytest'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v test_app.py'
            }
        }
    }
    post {
        success {
            echo 'SUCCESS LOGGED'
        }
        failure {
            echo 'FAILURE LOGGED'
        }
    }
}
