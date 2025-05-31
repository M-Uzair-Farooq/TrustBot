 pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Cloning GitHub Repository...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Creating virtual environment...'
                bat "python -m venv %VENV_DIR%"
            }
        }

        stage('Install Requirements') {
            steps {
                echo 'Activating venv and installing requirements...'
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Code Linting') {
            steps {
                echo 'Running flake8 for linting...'
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                    flake8 . --count --max-complexity=10 --max-line-length=120 --statistics
                """
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests with pytest...'
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    pytest tests || exit 1
                """
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            deleteDir()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
