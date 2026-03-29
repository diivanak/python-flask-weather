pipeline {
    agent any

    environment {
        IMAGE_NAME = "weather-app"
    }

    stages {

        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Test') {
            steps {
                sh 'pip install pytest'
                sh 'pytest'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                curl -X POST https://api.render.com/deploy/srv-XXXXX?key=YOUR_API_KEY
                '''
            }
        }
    }
}