pipeline {
    agent {
        docker { image 'python:3.11-bullseye' }
    }

    stages {
        stage('Clone') {
            steps {
                sh 'git clone -b main https://github.com/CalculatorTeam1/Lab2.git .'
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                python -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Build/Test') {
            steps {
                sh '''
                source venv/bin/activate
                python -m py_compile app.py
                echo "App validated successfully!"
                '''
            }
        }
    }

    post {
        success { echo "Build completed successfully!" }
        failure { echo "Build failed!" }
    }
}
