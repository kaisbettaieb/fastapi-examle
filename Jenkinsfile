pipeline{
    environment {
        registry = 'kaisbettaieb/fastapi-example'
        registryCredential = 'dockerhub-credentials'
        dockerImage = ''
        scannerHome = tool 'SonarQube scanner'
    }
    agent any

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

        stage('SonarQube analysis') {
            steps {
            withCredentials([string(credentialsId: 'credentials-sonar', variable: 'token')]) {
                    sh '${scannerHome}/bin/sonar-scanner sonar-scanner -Dsonar.login=$token'
                }
            }

        }
    }



        /*

        stage('Docker build image ') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }

        stage('Docker push') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                           dockerImage.push()
                    }
                }
            }
        }

        stage('Cleaning local image') {
            steps {
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }*/

}
