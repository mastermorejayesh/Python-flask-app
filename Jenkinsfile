pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/mastermorejayesh/Python-flask-app.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
              echo 'Build stage complate'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker-compose up -d'
              echo 'Running Container'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker ps'
              echo 'Verify complate'
            }
        }
    }
}
