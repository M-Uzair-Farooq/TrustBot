pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Setup Python') {
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
                    %VENV_DIR%\\Scripts\\python.exe -m pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Code Linting') {
            steps {
                echo 'Running flake8 for linting...'
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    %VENV_DIR%\\Scripts\\flake8 .
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    %VENV_DIR%\\Scripts\\python.exe -m unittest discover
                """
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up virtual environment...'
            bat "rmdir /s /q %VENV_DIR%"
        }
    }
}
