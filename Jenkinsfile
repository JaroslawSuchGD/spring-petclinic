pipeline {
    agent any
    
    tool name: 'M3', type: 'maven'
    tool name: 'Docker', type: 'dockerTool'

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
        stage('Static code analysis') {
            steps {
                sh 'mvn verify'
                sh 'mvn jacoco:report'
                sh 'mvn checkstyle:checkstyle'
            }
        }
        stage('Tests') {
            steps {
                sh 'mvn test'
            }
        }
        stage('Build') {
            steps {
                sh 'mvn -Dmaven.test.skip=true install'
            }
        }
        stage('Creating artifact') {
            steps {
                sh 'docker build -t $REGION-docker.pkg.dev/$PROJECT_ID/petclinic-app:$GIT_SHORT_HASH .'
            }
        }
        stage('Pushing artifact to artifact registry') {
            steps {
                sh "gcloud auth configure-docker ${params.REGION}-docker.pkg.dev"
                sh "docker push ${params.REGION}-docker.pkg.dev/${params.PROJECT_ID}/petclinic-app:$GIT_SHORT_HASH"
            }
        }
    }
}