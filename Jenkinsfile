pipeline {
    agent {
        label 'agent1'
    }

    tools {
        maven 'M3'
        dockerTool 'Docker'
    }

    environment {
        CREDS = credentials('docker-creds')
    }

    stages{
        stage('Cloning Repository') {
            steps {
                sh 'rm -rf spring-petclinic'
                sh 'git clone https://github.com/JaroslawSuchGD/spring-petclinic.git'
                echo 'Cloning petclinic repository ...'
            }
        }

        stage('Checkstyle') {
            steps {
                sh 'mvn checkstyle:checkstyle > checkstyle-report.txt'
                echo 'Generating checkstyle report'
            }
        }

        stage('Test') {
            steps{
                sh 'mvn test'
                echo 'Testing application'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn -Dmaven.test.skip=true install'
                echo 'Building project ...'
            }
        }

        stage('Docker-image-mr') {
            steps {
                echo "$CREDS_USR"
                echo "$CREDS_PSW"
                
                sh 'docker login -u $CREDS_USR -p $CREDS_PSW'
                sh 'docker build -t jsuchgd/mr:$GIT_COMMIT . && docker push jsuchgd/mr:$GIT_COMMIT'
                echo 'Building docker image for mr repository ...'
            }
        }

        stage('Docker-image-main') {
            steps {
                sh 'docker login -u $CREDS_USR -p $CREDS_PSW'
                sh 'docker build -t jsuchgd/main:$GIT_COMMIT . && docker push jsuchgd/main:$GIT_COMMIT'
                echo 'Building docker image for main repository ...'
            }
        }
    }
}
