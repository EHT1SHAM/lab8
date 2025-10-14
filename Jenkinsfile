pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
            }
        }
        
        stage('Install Python') {
            steps {
                sh 'apt-get update && apt-get install -y python3 python3-pip'
            }
        }
        
        stage('Setup Python') {
            steps {
                sh 'python3 --version'
                sh 'pip3 install --upgrade pip'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
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