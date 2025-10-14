pipeline {
    agent {
        docker {
            image 'python:3.9'
        }
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
            }
        }
        
        stage('Setup Python') {
            steps {
                sh 'python --version'
                sh 'pip install --upgrade pip'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                // Add test commands here if you have tests
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building application...'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed.'
        }
    }
}