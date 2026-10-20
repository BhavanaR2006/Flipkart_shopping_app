pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'anishaflipkart27/flipkart_shopping_app:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
                    bat 'docker push %DOCKER_IMAGE%'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl rollout status deployment/flipkart-deployment'
            }
        }
    }

    post {
        success {
            echo 'Flipkart CI/CD Pipeline Successful!'
        }
        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}