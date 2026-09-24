pipeline {
    agent { label 'wsl' }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/george-dal/devops-project.git'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                sh 'cd app && python3 -m pytest'
            }
        }

        stage('Build & Deploy with Ansible') {
            steps {
                sh 'ansible-playbook -i inventory.ini deploy.yml'
            }
        }
    }
}