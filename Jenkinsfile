
pipeline {
    agent {
        docker { image 'python:3.10.1-alpine' }
    }
    stages {
        stage('Build with unit testing') {
            steps {
                echo 'Building...' + env.BRANCH_NAME
            }
        }
        stage('Security Stage') {
            steps {
                echo "Testing security with snyk"
            }
        }
        stage('DB migrations'){
            steps {
                sh '''
                chmod +x django_project_api/project_api/docker-entrypoint.sh'
                ./docker-entrypoint.sh
                '''
            }
        }
        stage('Code coverage Test') {
            steps {
                echo "Todo install sonarqube server"
            }
        }
        stage("Test stage") {
            steps {
                secho "Todo test"
            }
        }
        stage("Build") {
            steps {
                echo "Todo build"
            }
        }
    }
}
