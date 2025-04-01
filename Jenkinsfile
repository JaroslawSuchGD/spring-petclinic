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
        GIT_LONG_HASH = "$GIT_COMMIT"
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
                script {
                    def SHORTENED_GIT_HASH = "$GIT_LONG_HASH".substring(0, 6)
                    echo "$SHORTENED_GIT_HASH"
                    sh 'docker login -u $CREDS_USR -p $CREDS_PSW'
                    sh 'docker build -t jsuchgd/mr:$SHORTENED_GIT_HASH . && docker push jsuchgd/mr:$SHORTENED_GIT_HASH'
                    echo 'Building docker image for main repository ...'
                }
            }
        }

        stage('Docker-image-main') {
            steps {
                sh 'docker login -u $CREDS_USR -p $CREDS_PSW'
                sh 'docker build -t jsuchgd/main:1.0 . && docker push jsuchgd/main:1.0'
                echo 'Building docker image for main repository ...'
            }
        }
    }
}
