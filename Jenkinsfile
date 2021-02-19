pipeline{
    environment {
        registry = 'kaisbettaieb/fastapi-example'
        registryCredential = 'dockerhub-credentials'
        dockerImage = ''
        scannerHome = tool 'SonarQube scanner'
        sonarToken = credentials('credentials-sonar')
        build_version = "1+${BUILD_NUMBER}"
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

        stage ('Commit in prod branch') {
            steps {

                sh '''
                    echo "commit prod branch"
                '''
            }

        }

        
        
    }
}


