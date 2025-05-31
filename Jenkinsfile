pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning Git repository...'
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                echo 'Creating virtual environment and installing dependencies...'
                bat '''
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Code Linting') {
            steps {
                echo 'Running flake8 for linting...'
                bat '''
                    call %VENV_DIR%\\Scripts\\activate
                    pip install flake8
                    flake8 app.py
                '''
            }
        }

        stage('Sanity Check - Flask Version') {
            steps {
                echo 'Checking Flask installation...'
                bat '''
                    call %VENV_DIR%\\Scripts\\activate
                    flask --version
                '''
            }
        }
    }

    post {
        success {
            echo 'Jenkins Build for Step 1 completed successfully!'
        }
        failure {
            echo 'Jenkins Build for Step 1 failed.'
        }
    }
}
