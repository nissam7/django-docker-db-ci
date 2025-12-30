pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker-compose down || true'
                sh 'docker-compose build'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Database Migration') {
            steps {
                sh 'docker exec django-web python manage.py migrate'
            }
        }
    }
}

