pipeline {
    agent any
    
    tools {
        maven 'M3'
    }

    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('gcp-creds')
        GIT_SHORT_HASH = "$GIT_COMMIT".substring(0, 6)
    }

    stages {
        
        stage('Cloning petclinic repository') {
            steps {
                git branch: 'main', credentialsId: 'github-creds', url: 'https://github.com/JaroslawSuchGD/spring-petclinic.git'
            }
        }
        stage ('DEBUGGING') {
            steps {
                echo "${env.action}"
                echo "${env.event}"
            }
        }
        stage('Static code analysis') {
            steps {
                sh 'mvn jacoco:report'
                sh 'mvn checkstyle:checkstyle'
            }
        }
        stage('Tests') {
            steps {
                //sh 'mvn test'
                sh 'mvn verify'
            }
        }
        stage('Build') {
            steps {
                sh 'mvn -Dmaven.test.skip=true install'
            }
        }
        stage('Creating artifact') {
            steps {
                sh "docker build -t ${params.REGION}-docker.pkg.dev/${params.PROJECT_ID}/spring-petclinic-registry/petclinic-app:$GIT_SHORT_HASH ."
            }
        }
        stage('Pushing artifact to artifact registry') {
            steps {
                sh "gcloud auth configure-docker ${params.REGION}-docker.pkg.dev"
                sh "docker push ${params.REGION}-docker.pkg.dev/${params.PROJECT_ID}/spring-petclinic-registry/petclinic-app:$GIT_SHORT_HASH"
            }
        }
    }
}