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

        
        
        
    }
}


