pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/nissam7/django-docker-db-ci.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Clean Old Containers') {
            steps {
                sh '''
                docker rm -f django-db || true
                docker rm -f django-docker-db-ci_web || true
                '''
            }
        }

        stage('Run Containers') {
            steps {
                sh '''
                docker-compose up -d
                '''
            }
        }

        stage('Verify Containers') {
            steps {
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo "✅ Deployment completed successfully"
        }
        failure {
            echo "❌ Deployment failed"
        }
    }
}

