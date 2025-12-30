pipeline {
    agent none

    triggers {
        githubPush()
    }

    stages {

        stage('Checkout Source') {
            agent any
            steps {
                git branch: 'main',
                    url: 'https://github.com/nissam7/django-docker-db-ci.git'
            }
        }

        stage('Deploy on Remote Node') {
            agent { label 'remote' }

            steps {
                sh '''
                if [ ! -d "$HOME/python_docker" ]; then
                    git clone https://github.com/nissam7/django-docker-db-ci.git $HOME/python_docker
                fi

                cd $HOME/python_docker
                git pull

                docker-compose down --remove-orphans || true
                docker-compose build
                docker-compose up -d
                '''
            }
        }

        stage('Verify Containers') {
            agent { label 'remote' }
            steps {
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo "✅ Deployment completed successfully on remote server"
        }
        failure {
            echo "❌ Deployment failed on remote server"
        }
    }
}
