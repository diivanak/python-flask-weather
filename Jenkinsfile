pipeline {
    agent any

    parameters {
        choice(name: 'DEPLOY_ENV', choices: ['local', 'render'], description: 'Deployment target')
    }

    environment {
        IMAGE_NAME = "weather-app"
        CONTAINER_NAME = "weather-container"
        RENDER_HOOK = credentials('render-deploy-hook')
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
                sh 'pip install pytest requests'
                sh 'pytest'
            }
        }

        stage('Deploy Local') {
            echo "Deploying to local environment..."
            when {
                expression { params.DEPLOY_ENV == 'local' }
            }
            steps {
                sh 'docker rm -f $CONTAINER_NAME || true'
                sh 'docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME'
            }
        }

        stage('Deploy Render') {
            echo "Deploying to Render..."
            when {
                expression { params.DEPLOY_ENV == 'render' }
            }
            steps {
                sh 'curl -X POST $RENDER_HOOK'
            }
        }
    }
}