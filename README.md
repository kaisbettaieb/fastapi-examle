# fastapi-examle
This is a playground to test CI/CD tools such as Jenkins, Sonar, Docker, Jfrog Artifactory and kubernetes

## What's working
For now Jenkins pipeline is responsible for :
1. Jenkins pipeline get trigered by github webhooks when a new commit is pushed.
2. Jenkins will checkout the new code.
3. Run unit tests and validate that they passed.
4. Run the code againt SonarQube and check if any bugs/code smells or any other issues exist on code.
5. Build the application and push it to a private Jfrog artifactory
6. Build and push a Docker image to Docker hub registry
