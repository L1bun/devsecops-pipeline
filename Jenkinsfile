pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/L1bun/devsecops-pipeline.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devsecops-app ./app'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 devsecops-app'
            }
        }
    }
}
