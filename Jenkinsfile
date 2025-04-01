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
                def git_hash = $GIT_COMMIT
                def short_git_hash = git_hash.substring(0, 6)
                sh 'docker login -u $CREDS_USR -p $CREDS_PSW'
                sh 'docker build -t jsuchgd/mr:$short_git_hash . && docker push jsuchgd/mr:$short_git_hash'
                echo 'Building docker image for main repository ...'
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
