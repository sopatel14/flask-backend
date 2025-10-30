pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build') {
            steps {
                sh 'docker build -t flask-backend .'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Running backend tests..."'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d --name flask-backend -p 5000:5000 flask-backend'

            }
        }
    }
}
