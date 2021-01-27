pipeline{
    agent any
    def app
    stages {
        stage('Clone github repo'){
            steps {
                git credentialsId: 'github-credentials', url: 'https://github.com/kaisbettaieb/fastapi-examle', branch: 'main'

            }
        }

        stage('Setup') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Unit testing') {
            steps {
                sh 'python -m unittest discover'
            }

        }

        stage('Docker build') {
            steps {
                app = docker.build("kaisbettaieb/fastapi-example")
            }
        }

        stage('Docker push') {
            steps {
                docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                       app.push("${env.BUILD_NUMBER}")
                       app.push("latest")
                }
            }
        }
    }
}
