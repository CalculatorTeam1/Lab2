pipeline {
    agent {
        docker { image 'python:3.11' }
    }
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/CalculatorTeam1/Lab2.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh '''
                python -m venv venv
                source venv/bin/activate
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
}
