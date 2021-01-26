node {
    checkout scm

    docker.withRegistry('registry.hub.docker.com', 'dockerhub-credentials'){
        def customImage = docer.build("fastapi-example:app")
        customImage.push()
    }

}