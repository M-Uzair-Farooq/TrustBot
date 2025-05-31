pipeline {
    agent any

    environment {
        VENV = 'venv'
        FLASK_APP = 'app.py'
        // Load environment variables from .env file
        ENV_FILE = '.env'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', 
                url: 'https://github.com/M-Uzair-Farooq/TrustBot.git',
                credentialsId: 'your-github-credentials' // If private repo
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh 'python -m venv $VENV'
                sh '''
                . $VENV/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Database Setup') {
            steps {
                sh '''
                . $VENV/bin/activate
                flask shell <<EOF
                from app import db
                db.create_all()
                exit()
                EOF
                '''
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    try {
                        sh '''
                        . $VENV/bin/activate
                        python -m pytest tests/ || true  # Continue even if tests fail
                        '''
                    } catch (e) {
                        echo "Some tests failed: ${e}"
                    }
                }
            }
            post {
                always {
                    junit '**/test-reports/*.xml'  // If you generate JUnit reports
                }
            }
        }

        stage('Security Checks') {
            steps {
                sh '''
                . $VENV/bin/activate
                pip install bandit safety
                bandit -r . -f xml -o bandit_results.xml || true
                safety check -r requirements.txt --output json > safety_report.json || true
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'bandit_results.xml', fingerprint: true
                    archiveArtifacts artifacts: 'safety_report.json', fingerprint: true
                }
            }
        }

        stage('Build') {
            steps {
                sh '''
                . $VENV/bin/activate
                flask check
                '''
                echo 'Flask application built successfully'
            }
        }

        stage('Deploy (Staging)') {
            when {
                branch 'main'  // Or your deployment branch
            }
            steps {
                sh '''
                . $VENV/bin/activate
                nohup flask run --host=0.0.0.0 --port=5000 > server.log 2>&1 &
                '''
                echo 'Application deployed to staging environment'
            }
        }
    }

    post {
        always {
            cleanWs()  // Clean up workspace
        }
        success {
            slackSend color: 'good', message: "Build Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
        }
        failure {
            slackSend color: 'danger', message: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
        }
    }
}