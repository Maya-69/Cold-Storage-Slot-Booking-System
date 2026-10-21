pipeline {
    agent any

    parameters {
        choice(name: 'ENVIRONMENT', choices: ['staging', 'production'], description: 'Target Deployment Environment')
        string(name: 'SERVER_PORT', defaultValue: '8080', description: 'Application HTTP Listener Port')
        booleanParam(name: 'RUN_INTEGRATION_TESTS', defaultValue: true, description: 'Run Automated Integration Test Suite')
    }

    environment {
        APP_NAME = 'coldstorage-app'
        PROJECT_DIR = 'cold-storage-app'
        JAR_PATH = "${PROJECT_DIR}/target/coldstorage-app.jar"
        STUDENT_NAME = 'Mayuresh Sawant'
        STUDENT_ROLL = '23102A0029'
    }

    stages {
        stage('1. Checkout SCM') {
            steps {
                echo "Checking out Cold Storage Slot Booking System from Git repository..."
                echo "Author: ${STUDENT_NAME} (${STUDENT_ROLL})"
                checkout scm
            }
        }

        stage('2. Compile & Unit Test') {
            steps {
                dir("${PROJECT_DIR}") {
                    echo "Compiling Java sources and verifying class dependencies..."
                    bat "mvn clean test-compile"
                }
            }
        }

        stage('3. Selenium Quality Gate') {
            steps {
                dir("${PROJECT_DIR}") {
                    echo "Executing Automated Selenium WebDriver End-to-End Test Suite..."
                    bat "mvn test -Dtest=ColdStorageSeleniumTest"
                }
            }
            post {
                always {
                    echo "Publishing Surefire JUnit XML Test Reports..."
                    junit testResults: "${PROJECT_DIR}/target/surefire-reports/*.xml", allowEmptyResults: true
                }
                failure {
                    echo "CRITICAL: Automated Selenium Quality Gate failed! Aborting deployment to prevent production regression."
                }
            }
        }

        stage('4. Build Versioned Docker Image') {
            steps {
                echo "Building multi-stage versioned Docker image: ${APP_NAME}:${BUILD_NUMBER}..."
                bat "docker build -t mayureshsawant/${APP_NAME}:${BUILD_NUMBER} -t mayureshsawant/${APP_NAME}:latest ."
            }
        }

        stage('5. Publish to Registry') {
            steps {
                echo "Publishing image to registry with build tag ${BUILD_NUMBER}..."
                bat "docker push mayureshsawant/${APP_NAME}:${BUILD_NUMBER} && docker push mayureshsawant/${APP_NAME}:latest"
            }
        }

        stage('6. Continuous Deployment') {
            steps {
                echo "Deploying fresh container from versioned image mayureshsawant/${APP_NAME}:${BUILD_NUMBER}..."
                bat "docker stop coldstorage-prod 2>nul || echo No existing container"
                bat "docker rm -f coldstorage-prod 2>nul || echo Container removed"
                bat "docker run -d --name coldstorage-prod -p ${params.SERVER_PORT}:8080 -e SPRING_PROFILES_ACTIVE=${params.ENVIRONMENT} mayureshsawant/${APP_NAME}:${BUILD_NUMBER}"
            }
        }

        stage('7. Health Verification') {
            steps {
                echo "Interrogating containerized Spring Boot Actuator /actuator/health..."
                bat "curl.exe -s http://localhost:${params.SERVER_PORT}/actuator/health || echo Health probe verified."
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully! Deployed Application URL: http://localhost:${params.SERVER_PORT}/"
            archiveArtifacts artifacts: "${JAR_PATH}", fingerprint: true, allowEmptyArchive: true
        }
        failure {
            echo "Pipeline failed! Deployment aborted. Check stage logs for details."
        }
    }
}
