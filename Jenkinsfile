pipeline{
    environment {
        registry = 'kaisbettaieb/fastapi-example'
        registryCredential = 'dockerhub-credentials'
        scannerHome = tool 'SonarQube scanner'
        sonarToken = credentials('credentials-sonar')
        build_version = "1.${BUILD_NUMBER}"
    }
    agent any

    stages {
        stage('Clone github repo'){
            steps {
                git credentialsId: 'github-credentials', url: 'https://github.com/kaisbettaieb/fastapi-examle', branch: 'build'

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

        stage('Docker build image ') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$build_version"
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
                sh "docker rmi $registry:$build_version"
            }
        }

        stage ('Update prod branch') {
            steps {
                    withCredentials([usernamePassword(credentialsId: 'github-credentials', passwordVariable: 'git_password', usernameVariable: 'git_username')]) {
                        sh  """
                        git init
                        echo $git_username
                        echo $git_name
                        git config --global user.email $git_username
                        git config --global user.name $git_name
                        git checkout prod
                        echo $build_version > .version
                        git add .version
                        git commit -m "update build version"
                        git push
                        """
                    }
                   
                    
                }

            }

            
    }
}


