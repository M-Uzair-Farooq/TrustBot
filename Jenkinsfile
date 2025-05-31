pipeline {
    agent any

    environment {
        VENV_DIR = "venv"  
        FLASK_APP = "app.py"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', 
                url: 'https://github.com/M-Uzair-Farooq/TrustBot.git'
            }
        }

        stage('Setup Environment') {
            steps {
                bat """
                    python -m venv "%VENV_DIR%"
                    call "%VENV_DIR%\\Scripts\\activate"
                    pip install -r requirements.txt
                """
            }
        }

        stage('Initialize DB') {
            steps {
                bat """
                    call "%VENV_DIR%\\Scripts\\activate"
                    python -c "from app import db; db.create_all()"
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat 'echo "No tests yet"'

                // // call "%VENV_DIR%\\Scripts\\activate"
                // python -m pytest
            }
        }
    }
}