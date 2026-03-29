pipeline {
    agent any

    parameters {
        choice(name: 'DEPLOY_ENV', choices: ['local', 'render'], description: 'Deployment target')
    }

    environment {
        IMAGE_NAME = "weather-app"
        CONTAINER_NAME = "weather-container"
        RENDER_HOOK = credentials('RENDER_DEPLOY_HOOK_URL')
    }

    stages {

        stage('Build') {
            steps {
                echo "Building Docker image: $IMAGE_NAME"
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
                sh 'docker run --rm weather-app pytest -v tests.py'
            }
        }

        stage('Deploy Local') {
            when {
                expression { params.DEPLOY_ENV == 'local' }
            }
            steps {
                echo "Deploying to local environment..."
                sh 'docker rm -f $CONTAINER_NAME || true'
                sh 'docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME'
            }
        }

        stage('Deploy Render') {
            when {
                expression { params.DEPLOY_ENV == 'render' }
            }
            steps {
                echo "Deploying to Render..."
                sh 'curl -X POST $RENDER_HOOK'
            }
        }
    }
}