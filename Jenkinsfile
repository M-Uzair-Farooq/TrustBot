<<<<<<< HEAD
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
=======
pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
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
                bat "python -m venv ${VENV_DIR}"
            }
        }

        stage('Install Requirements') {
            steps {
                echo 'Activating venv and installing requirements...'
                bat """
                    call ${VENV_DIR}\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Code Linting') {
            steps {
                echo 'Running flake8 for linting...'
                bat """
                    call ${VENV_DIR}\\Scripts\\activate
                    flake8 . --exclude=${VENV_DIR}
                """
            }
        }

        stage('Run App (Optional)') {
            when {
                expression { return false } 
            }
            steps {
                echo 'Running Flask App...'
                bat """
                    call ${VENV_DIR}\\Scripts\\activate
                    set FLASK_APP=app.py
                    flask run
                """
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            deleteDir()
        }
    }
}
>>>>>>> a646f736b71664bd941ca88ae72212c19c9b08c8
