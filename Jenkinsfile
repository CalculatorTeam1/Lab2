pipeline {
    agent {
        docker {
            image 'python:3.11-bullseye'
            args '-u root:root'
        }
    }

    environment {
        VENV_DIR = 'venv'
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
                python -m venv $VENV_DIR
                source $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Build/Test') {
            steps {
                sh '''
                source $VENV_DIR/bin/activate
                python -m py_compile app.py
                echo "App validated successfully!"
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source $VENV_DIR/bin/activate
                echo "No tests defined yet"
                '''
            }
        }
    }

    post {
        success {
            echo "Build completed successfully!"
        }
        failure {
            echo "Build failed!"
        }
    }
}
