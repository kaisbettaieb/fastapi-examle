pipeline{
    environment {
        registry = 'kaisbettaieb/fastapi-example'
        registryCredential = 'dockerhub-credentials'
        dockerImage = ''
        scannerHome = tool 'SonarQube scanner'
        sonarToken = credentials('credentials-sonar')
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
                sh 'pip install -r requirements.txt --user'
            }
        }

        stage('Unit testing') {
            steps {
                sh 'python -m unittest discover'
            }

        }

        stage('SonarQube analysis') {
            steps {
                 withSonarQubeEnv('SonarQube') {
                      bat "${scannerHome}\\sonar-scanner.bat -Dsonar.login=$sonarToken"
                 }
            }

        }

        stage("Quality Gate") {
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage ('Artifactory configuration') {
            steps {
                rtServer (
                    id: "ARTIFACTORY_SERVER",
                    url: "https://kaisbettaieb.jfrog.io/artifactory",
                    credentialsId: "artifactory-credentials"
                )
            }
        }

        stage ('Build python package') {
            steps {
                sh '''
                    python setup.py sdist bdist_wheel
                '''
            }
        }

        stage ('Upload packages') {
            steps {
                rtUpload (
                    serverId: "ARTIFACTORY_SERVER",
                    spec: '''{
                        "files": [
                            {
                                "pattern": "dist/",
                                "target": "artifactory-python-dev-local/"
                            }
                        ]
                    }'''
                )
            }
        }

         stage ('Publish build info') {
            steps {
                rtPublishBuildInfo (
                    serverId: "ARTIFACTORY_SERVER"
                )
            }
        }

        stage ('Kuberenetes deployment'){
            steps {

                sh  '''
                    export KUBECONFIG=C:/Users/kaisb/.kube/config
                    kubectl apply -f deployment.yaml
                '''
            
            }

        }

        stage ('Kubernetes service'){
            steps {
                sh '''
                    export KUBECONFIG=C:/Users/kaisb/.kube/config
                    kubectl apply -f service.yaml
                '''
                

            }

        }

        /*stage('Docker build image ') {
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
}


